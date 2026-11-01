from pathlib import Path
import os,json,subprocess,shutil,hashlib,time,urllib.request,traceback,stat,pwd

if not __debug__:raise RuntimeError('Safety assertions require Python without -O')
if os.geteuid()!=0:raise RuntimeError('Run the reviewed helper as root')
os.umask(0o077)
ROOT=Path('/var/tmp/commonplace-storage-20261101-r5')
PREVIOUS=Path('/var/tmp/commonplace-storage-20261101-r4')
PREVIOUS_HASH='3aab196a49f859a0716b7c99a28fe72b0d0f4a7a3f9a81ed07e6b249a00f0eb3'
DISK=Path('/dev/disk/by-id/google-commonplace-data-balanced-20261101')
UUID='4b9a5959-5eed-4a88-a902-b4f30c7993cd'
PRIOR_MOUNT=Path('/var/lib/commonplace-db')
OLD=Path('/var/lib/commonplace/account.sqlite')
MOUNT=OLD.parent/'database-storage'
NEW=MOUNT/'account.sqlite'
PRESERVED=MOUNT/'account.before-r4.sqlite'
BACKUP=OLD.parent/'storage-before-balanced-20261101-r5'
BACKUP_TIMER='commonplace-backup.timer';BACKUP_SERVICE='commonplace-backup.service'
services=['nginx','commonplace-files','commonplace-runtime','commonplace']
stopped=False;switched=False;fstabChanged=False;timerSnapshot=None
state={'startedAt':time.time(),'state':'preflight','oldDiskRetained':True,'databasePathPreserved':True,'hostPoliciesChanged':False}

def run(*args,**kw):return subprocess.run(args,check=True,**kw)
def output(*args):return subprocess.check_output(args,text=True).strip()
def absent(p):return not p.exists() and not p.is_symlink()
def regular(p):return p.is_file() and not p.is_symlink()
def flush(p):
 fd=os.open(p,os.O_RDONLY)
 try:os.fsync(fd)
 finally:os.close(fd)
def claim_start(root,initial):
 assert not root.is_symlink(),'Evidence ROOT must not be a symlink'
 root.mkdir(mode=0o700,parents=True,exist_ok=True)
 info=root.stat()
 assert stat.S_ISDIR(info.st_mode) and info.st_uid==os.geteuid()==0 and stat.S_IMODE(info.st_mode)==0o700,'Evidence ROOT must be root-owned/private'
 assert all(absent(root/name) for name in ['started.json','status.json','result.json']),'r5 already started; inspect evidence before retry'
 # O_EXCL elects exactly one direct launcher, even after concurrent absence checks.
 with (root/'started.json').open('x') as marker:
  marker.write(json.dumps(initial));marker.flush();os.fsync(marker.fileno())
 flush(root);flush(root.parent)

def save(phase,**extra):
 state.update(state=phase,**extra);p=ROOT/'status.json';t=p.with_suffix('.tmp')
 t.write_text(json.dumps(state,indent=2));flush(t);t.replace(p);flush(ROOT)
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def copy(p,q):
 assert regular(p) and absent(q),'Copy must not overwrite an existing file'
 shutil.copy2(p,q);s=p.stat();os.chown(q,s.st_uid,s.st_gid);assert digest(p)==digest(q)
def dbfiles(base):return [p for suffix in ['', '-wal','-shm'] if (p:=Path(str(base)+suffix)).exists()]
def stopped_services():
 assert all(output('systemctl','show',s,'--property','MainPID','--value')=='0' for s in services)
def no_holders(files):
 identities={(p.stat().st_dev,p.stat().st_ino) for p in files}
 for proc in Path('/proc').iterdir():
  if not proc.name.isdigit() or int(proc.name)==os.getpid():continue
  try:
   for fd in (proc/'fd').iterdir():
    try:s=fd.stat()
    except FileNotFoundError:continue
    assert (s.st_dev,s.st_ino) not in identities,'Unexpected database holder PID '+proc.name
  except FileNotFoundError:continue
  # Permission errors fail closed; aliases/deleted names are matched by inode.
def expected_holders_only(files):
 allowed={s+'.service':output('systemctl','show',s,'--property','ControlGroup','--value') for s in ['commonplace','commonplace-files','commonplace-runtime']}
 assert all(path=='/system.slice/'+unit for unit,path in allowed.items()),'Unexpected application cgroup layout'
 identities={(p.stat().st_dev,p.stat().st_ino) for p in files};holders=[]
 for proc in Path('/proc').iterdir():
  if not proc.name.isdigit() or int(proc.name)==os.getpid():continue
  try:
   for fd in (proc/'fd').iterdir():
    try:info=fd.stat()
    except FileNotFoundError:continue
    if (info.st_dev,info.st_ino) not in identities:continue
    paths=[line.split(':',2)[-1] for line in (proc/'cgroup').read_text().splitlines()]
    matches=[unit for unit,path in allowed.items() if any(p==path or p.startswith(path+'/') for p in paths)]
    assert len(matches)==1,'Unexpected pre-pause database holder PID '+proc.name
    holders.append({'pid':int(proc.name),'unit':matches[0]});break
  except FileNotFoundError:continue
  # Permission errors fail closed; no processes are signaled.
 return holders

def unit_properties(unit,names):
 rows=output('systemctl','show',unit,*['--property='+k for k in names]).splitlines()
 values=dict(row.split('=',1) for row in rows)
 assert set(values)==set(names),'Incomplete unit metadata for '+unit
 return values

def backup_schedule_contract():
 timer=unit_properties(BACKUP_TIMER,['Unit','Triggers','PartOf','BindsTo','StopWhenUnneeded','PropagatesStopTo','UnitFileState'])
 backup=unit_properties(BACKUP_SERVICE,['Type','Restart','TimeoutStartUSec','PartOf','BindsTo','StopWhenUnneeded','TriggeredBy','Requires'])
 assert timer['Unit']==BACKUP_SERVICE and timer['Triggers']==BACKUP_SERVICE
 assert all(timer[k]=='' for k in ['PartOf','BindsTo','PropagatesStopTo']) and timer['StopWhenUnneeded']=='no','Stopping timer could stop another unit'
 assert backup['Type']=='oneshot' and backup['Restart']=='no' and backup['TimeoutStartUSec']=='5min'
 assert all(backup[k]=='' for k in ['PartOf','BindsTo']) and backup['StopWhenUnneeded']=='no'
 assert backup['TriggeredBy']==BACKUP_TIMER and BACKUP_TIMER not in backup['Requires'].split(),'Backup service is coupled to timer stop'
 return {'timer':timer,'backup':backup}

def backup_live_state():
 return unit_properties(BACKUP_SERVICE,['ActiveState','SubState','MainPID','Result','ExecMainStatus','InvocationID','ExecMainStartTimestampMonotonic','ExecMainExitTimestampMonotonic','ExecMainStartTimestamp','ExecMainExitTimestamp','ExecMainPID','ExecMainCode'])

def backup_schedule_snapshot():
 snapshot=backup_schedule_contract()
 live=unit_properties(BACKUP_TIMER,['ActiveState','SubState'])
 assert live['ActiveState'] in ['active','inactive'],'Backup timer is transitioning or failed'
 snapshot['timerState']=live
 before=backup_live_state();snapshot['backupState']=before
 if before['ActiveState']=='failed':
  # Only the owner-observed failure completed before r5 is authorized here.
  expected={'ActiveState':'failed','SubState':'failed','MainPID':'0','Result':'timeout','ExecMainStatus':'15','InvocationID':'b87cb0f36fe4490db77a36c6aff71f13','ExecMainStartTimestampMonotonic':'3827523228312','ExecMainExitTimestampMonotonic':'3827823218295','ExecMainStartTimestamp':'Sun 2026-11-01 04:03:23 UTC','ExecMainExitTimestamp':'Sun 2026-11-01 04:08:23 UTC','ExecMainPID':'883648','ExecMainCode':'2'}
  assert before==expected,'Unapproved preexisting backup failure/fingerprint'
  snapshot['preexistingTimeout']=dict(before)
 return snapshot

def check_backup_contract(snapshot):
 assert backup_schedule_contract()=={k:snapshot[k] for k in ['timer','backup']},'Backup timer/service configuration changed'

def pause_backup_timer(snapshot):
 check_backup_contract(snapshot)
 assert unit_properties(BACKUP_TIMER,['ActiveState'])['ActiveState']==snapshot['timerState']['ActiveState'],'Backup timer state changed before pause'
 if snapshot['timerState']['ActiveState']=='active':run('systemctl','stop',BACKUP_TIMER)
 assert unit_properties(BACKUP_TIMER,['ActiveState'])['ActiveState']=='inactive','Backup timer did not pause'

def wait_backup_idle(snapshot):
 # Existing oneshot timeout is five minutes; do not signal/stop its service.
 deadline=time.monotonic()+315
 while time.monotonic()<deadline:
  live=backup_live_state()
  if snapshot.get('preexistingTimeout') is not None:
   assert live==snapshot['preexistingTimeout'],'Historical backup timeout changed after snapshot'
   return
  if live['ActiveState']=='inactive':
   assert live['MainPID']=='0' and live['Result']=='success','Backup did not finish successfully'
   return
  assert live['ActiveState'] in ['active','activating','deactivating'],'Backup service failed; inspect before migration'
  time.sleep(1)
 raise RuntimeError('Backup still running after bounded wait; not signaled')

def assert_backup_paused(snapshot):
 check_backup_contract(snapshot)
 assert unit_properties(BACKUP_TIMER,['ActiveState'])['ActiveState']=='inactive','Backup timer resumed before pause'
 live=backup_live_state()
 if snapshot.get('preexistingTimeout') is not None:
  assert live==snapshot['preexistingTimeout'],'Historical backup timeout changed before pause'
 else:assert all(live[k]==v for k,v in {'ActiveState':'inactive','MainPID':'0','Result':'success'}.items()),'Backup restarted before pause'

def restore_backup_timer(snapshot):
 check_backup_contract(snapshot)
 current=unit_properties(BACKUP_TIMER,['ActiveState'])['ActiveState'];expected=snapshot['timerState']['ActiveState']
 assert current in ['active','inactive'],'Backup timer entered an unexpected state'
 if current!=expected:run('systemctl','start' if expected=='active' else 'stop',BACKUP_TIMER)
 assert unit_properties(BACKUP_TIMER,['ActiveState'])['ActiveState']==expected,'Backup timer active state not restored'
 check_backup_contract(snapshot)

def mount_records(mount):
 data=json.loads(output('findmnt','-J','-R','-M',str(mount),'-o','TARGET,SOURCE,FSTYPE,OPTIONS'))
 def flatten(rows):
  for row in rows:
   yield {k:row[k] for k in ['target','source','fstype','options']}
   yield from flatten(row.get('children',[]))
 return sorted(flatten(data['filesystems']),key=lambda r:r['target'])
def is_mount(p):
 r=subprocess.run(['findmnt','-rn','-M',str(p),'-o','TARGET'],capture_output=True,text=True)
 assert r.returncode in [0,1],r.stderr
 return r.returncode==0
def check_original_mounts():
 current=mount_records(OLD.parent)
 assert [r for r in current if r['target']!=str(MOUNT)]==originalMounts,'Original/SSH mounts changed'
 assert not any(r['target'].startswith(str(MOUNT)+'/') for r in current),'Unexpected balanced-disk submount'
def unit_roles():
 keys=['User','Group','ProtectSystem','ReadWritePaths','ReadOnlyPaths','BindPaths','BindReadOnlyPaths','InaccessiblePaths','PrivateMounts']
 return {s:output('systemctl','show',s,*['--property='+k for k in keys]) for s in services[1:]}
def schema_as_user(file,user,quick=False):
 code="import sqlite3,json,sys;from contextlib import closing\nwith closing(sqlite3.connect('file:'+sys.argv[1]+'?mode=ro',uri=True)) as db:\n if sys.argv[2]=='1': assert db.execute('PRAGMA quick_check').fetchall()==[('ok',)]\n print(json.dumps(dict(db.execute('SELECT name,digest FROM cp_schema_migrations'))))"
 return json.loads(output('runuser','-u',user,'--','python3','-c',code,str(file),'1' if quick else '0'))
def checkpoint(file,user):
 assert regular(file)
 js="import {DatabaseSync} from 'node:sqlite';const d=new DatabaseSync(process.argv[1]);try{if(d.prepare('PRAGMA wal_checkpoint(TRUNCATE)').get().busy!==0)throw Error('WAL is busy');}finally{d.close();}"
 run('runuser','-u',user,'--','/opt/node/bin/node','--input-type=module','-e',js,str(file),stdout=subprocess.DEVNULL)
 wal=Path(str(file)+'-wal');assert not wal.exists() or regular(wal) and wal.stat().st_size==0
 for suffix in ['-wal','-shm']:
  p=Path(str(file)+suffix)
  if p.exists():assert regular(p);p.unlink()
 flush(file);flush(file.parent)
def waithealth():
 until=time.monotonic()+90
 while time.monotonic()<until:
  try:
   with urllib.request.urlopen('http://127.0.0.1:3000/healthz',timeout=5) as r:v=json.load(r)
   if v.get('ready') is True:return
  except Exception:pass
  time.sleep(1)
 raise RuntimeError('Internal health did not become ready')
# Match the Files authorizer's existing node:sqlite read-only contract exactly.
# This runs in the restarted Files mount namespace, under its existing service UID.
FILES_READ_JS="""
import {DatabaseSync} from 'node:sqlite';
import {statSync,realpathSync} from 'node:fs';
import {createHash} from 'node:crypto';
const [configured,selected,device,inode,metadata]=process.argv.slice(1);
const expected=JSON.parse(metadata);
function checkIdentity(){
 const file=realpathSync(configured),s=statSync(file,{bigint:true});
 if(file!==selected||s.dev.toString()!==device||s.ino.toString()!==inode||!s.isFile())throw Error('Files auth DB selected identity mismatch');
}
checkIdentity();
const db=new DatabaseSync(configured,{readOnly:true});
try{
 db.exec('PRAGMA query_only=ON; PRAGMA busy_timeout=5000;');
 db.exec('BEGIN');
 if(db.prepare('PRAGMA database_list').get().file!==selected)throw Error('Files driver selected a different auth DB');
 const actual=db.prepare('SELECT name,digest FROM cp_schema_migrations ORDER BY name').all().map(r=>[r.name,r.digest]);
 if(actual.length!==47||JSON.stringify(actual)!==JSON.stringify(expected))throw Error('Files auth DB migration identity mismatch');
 for(const table of ['cp_workspace_agent_tokens','cp_devices','cp_workspace_members']){
  if(!db.prepare('SELECT name FROM sqlite_schema WHERE type=? AND name=?').get('table',table))throw Error('Files auth schema missing');
  db.prepare('SELECT * FROM '+table+' LIMIT 0').all();
 }
 checkIdentity();
 console.log(JSON.stringify({readOnly:true,walAware:true,selectedDatabase:true,schemaMatches:true,migrations:actual.length,schemaSha256:createHash('sha256').update(JSON.stringify(actual)).digest('hex')}));
}finally{db.close();}
"""
def files_process(identity):
 assert unit_roles()==originalRoles,'Unit sandbox/role metadata changed'
 assert output('systemctl','is-active','commonplace-files')=='active'
 pid=int(output('systemctl','show','commonplace-files','--property','MainPID','--value'));assert pid>1
 proc=Path('/proc')/str(pid)
 assert (proc/'exe').resolve()==Path('/opt/node/bin/node').resolve(),'Files executable changed'
 assert (proc.stat().st_uid,proc.stat().st_gid)==(identity.pw_uid,identity.pw_gid),'Files process role changed'
 assert any(line.split(':',2)[-1].endswith('/commonplace-files.service') for line in (proc/'cgroup').read_text().splitlines()),'Files cgroup changed'
 # Whitelist this single setting; never log or return the process environment.
 values=[v.split(b'=',1)[1].decode() for v in (proc/'environ').read_bytes().split(b'\0') if v.startswith(b'FILES_ACCOUNT_DB=')]
 assert values==[str(OLD)],'Files configured account DB path changed'
 started=(proc/'stat').read_text().rsplit(')',1)[1].split()[19]
 return pid,started,values[0]
def files_namespace_read(database,user,identity):
 selected=database.resolve(strict=True);assert regular(selected)
 info=selected.stat();expected=sorted(schema_as_user(database,user).items());assert len(expected)==47
 metadata=json.dumps(expected,separators=(',',':'),ensure_ascii=False)
 proof={'readOnly':True,'walAware':True,'selectedDatabase':True,'schemaMatches':True,'migrations':47,'schemaSha256':hashlib.sha256(metadata.encode()).hexdigest()}
 process=files_process(identity);pid,_,configured=process
 result=json.loads(output('nsenter','-t',str(pid),'-m','--','runuser','-u',user,'--','/opt/node/bin/node','--input-type=module','-e',FILES_READ_JS,configured,str(selected),str(info.st_dev),str(info.st_ino),metadata))
 assert result==proof,'Files auth DB read proof differs'
 assert files_process(identity)==process,'Files restarted/configuration changed during auth DB proof'
 assert database.resolve(strict=True)==selected and (selected.stat().st_dev,selected.stat().st_ino)==(info.st_dev,info.st_ino),'Selected auth DB changed during Files proof'
 return proof

def start_app_services(database,user,identity):
 assert unit_roles()==originalRoles,'Unit sandbox/role metadata changed'
 run('systemctl','start','commonplace');waithealth()
 assert all(p.stat().st_uid==identity.pw_uid and p.stat().st_gid==identity.pw_gid for p in dbfiles(database.resolve())),'Main-created sidecar ownership differs'
 started=int(time.time()*1000);run('systemctl','start','commonplace-runtime');deadline=time.monotonic()+60
 code="import sqlite3,json,sys;from contextlib import closing\nwith closing(sqlite3.connect('file:'+sys.argv[1]+'?mode=ro',uri=True)) as db:\n r=db.execute('SELECT seen_at FROM cp_cloud_runtime WHERE id=1').fetchone();print(json.dumps(r[0] if r else 0))"
 while time.monotonic()<deadline:
  seen=json.loads(output('runuser','-u',user,'--','python3','-c',code,str(database)))
  if seen>=started and output('systemctl','is-active','commonplace-runtime')=='active':break
  time.sleep(1)
 else:raise RuntimeError('Worker has no fresh heartbeat')
 run('systemctl','start','commonplace-files');until=time.monotonic()+45
 while time.monotonic()<until:
  try:
   with urllib.request.urlopen('http://127.0.0.1:8789/files/config',timeout=5) as r:
    available=r.status==200 and output('systemctl','is-active','commonplace-files')=='active'
  except Exception:available=False
  if available:
   state['filesAuthDatabaseProof']=files_namespace_read(database,user,identity);return
  time.sleep(1)
 raise RuntimeError('Files service did not recover')

# This code runs only in the live main unit's mount namespace, after dropping to
# its existing UID. Device checks precede every disposable filesystem mutation.
PROBE_JS="""
import {DatabaseSync} from 'node:sqlite';
import {statSync,lstatSync,realpathSync,symlinkSync,unlinkSync} from 'node:fs';
import {dirname} from 'node:path';
const [alias,target,device,oldDevice]=process.argv.slice(1);
const expected=Number(device),original=Number(oldDevice);
if(!Number.isSafeInteger(expected)||!Number.isSafeInteger(original)||expected===original)throw Error('Invalid device guard');
if(realpathSync(dirname(target))!==dirname(target)||statSync(dirname(target)).dev!==expected)throw Error('Nested balanced mount absent from main namespace');
if(realpathSync(dirname(alias))!==dirname(alias)||statSync(dirname(alias)).dev!==original)throw Error('Original mount differs in main namespace');
const files=[alias,target,target+'-wal',target+'-shm'];
for(const file of files){try{lstatSync(file);throw Error('Disposable probe already exists');}catch(e){if(e.code!=='ENOENT')throw e;}}
let a,b,linked=false;
try{
 symlinkSync(target,alias);linked=true;
 a=new DatabaseSync(alias);b=new DatabaseSync(target);
 a.exec('PRAGMA journal_mode=WAL; PRAGMA synchronous=FULL; CREATE TABLE t(v); INSERT INTO t VALUES (1)');
 b.exec('PRAGMA synchronous=FULL');
 if(b.prepare('SELECT v FROM t').get().v!==1)throw Error('Alias did not share WAL');
 b.exec('INSERT INTO t VALUES(2)');
 if(a.prepare('SELECT count(*) n FROM t').get().n!==2)throw Error('Reverse WAL alias mismatch');
 for(const db of [a,b])if(db.prepare('PRAGMA database_list').get().file!==target)throw Error('Driver did not canonicalize symlink');
 if(statSync(target).dev!==expected)throw Error('Probe was not on balanced disk');
 console.log(JSON.stringify({device:expected,namespaceWrite:true,sqliteAlias:true,walShared:true}));
}finally{
 try{b?.close();}finally{try{a?.close();}finally{
  if(linked)for(const file of files){try{unlinkSync(file);}catch(e){if(e.code!=='ENOENT')throw e;}}
 }}
}
"""
def namespace_probe(pid,user):
 nonce=os.urandom(8).hex();alias=OLD.parent/('.storage-probe69-r5-'+nonce+'.sqlite');target=MOUNT/alias.name
 assert int(output('systemctl','show','commonplace','--property','MainPID','--value'))==pid
 assert Path('/proc/'+str(pid)+'/exe').resolve()==Path('/opt/node/bin/node').resolve(),'Main executable changed'
 assert Path('/proc/'+str(pid)).stat().st_uid==identity.pw_uid
 assert any(line.split(':',2)[-1].endswith('/commonplace.service') for line in Path('/proc/'+str(pid)+'/cgroup').read_text().splitlines())
 result=json.loads(output('nsenter','-t',str(pid),'-m','--','runuser','-u',user,'--','/opt/node/bin/node','--input-type=module','-e',PROBE_JS,str(alias),str(target),str(balancedDevice),str(oldDevice)))
 assert result=={'device':balancedDevice,'namespaceWrite':True,'sqliteAlias':True,'walShared':True}
 assert all(absent(p) for base in [alias,target] for p in [base,Path(str(base)+'-wal'),Path(str(base)+'-shm')])
 assert int(output('systemctl','show','commonplace','--property','MainPID','--value'))==pid,'Main restarted during namespace probe'
 return result

claim_start(ROOT,state)
fstab=Path('/etc/fstab');originalFstab=fstab.read_bytes();fstabStat=fstab.stat()
(ROOT/'fstab.before').write_bytes(originalFstab);flush(ROOT/'fstab.before');flush(ROOT)
def setfstab(data):
 temp=Path('/etc/fstab.commonplace-storage-r5.tmp');assert absent(temp)
 temp.write_bytes(data);os.chmod(temp,stat.S_IMODE(fstabStat.st_mode));os.chown(temp,fstabStat.st_uid,fstabStat.st_gid)
 flush(temp);temp.replace(fstab);flush(fstab.parent)

try:
 assert digest(PREVIOUS/'migrate.py')==PREVIOUS_HASH,'r4 helper differs from reviewed source'
 previous=json.loads((PREVIOUS/'result.json').read_text())
 assert previous['state']=='rolled-back' and not previous.get('recoveryFailure') and not previous.get('timerRestoreFailure'),'r4 rollback is not complete'
 assert previous.get('failure','').startswith('AssertionError: Unexpected database holder PID ') and 'sourceSha256' not in previous,'Unexpected r4 stopping point'
 assert previous.get('balancedMountRetained')==str(MOUNT) and previous.get('namespaceProbe',{}).get('namespaceWrite') is True
 assert previous.get('filesAuthDatabaseProof',{}).get('selectedDatabase') is True
 assert regular(OLD) and OLD.parent.resolve()==OLD.parent and absent(BACKUP)
 assert all(output('systemctl','is-active',s)=='active' for s in services)
 assert DISK.resolve()==Path('/dev/sdc') and stat.S_ISBLK(DISK.stat().st_mode)
 assert output('findmnt','-rn','-M',str(OLD.parent),'-o','SOURCE')=='/dev/sdb'
 assert output('blkid','-s','UUID','-o','value',str(DISK))==UUID
 assert MOUNT.resolve()==MOUNT and not is_mount(PRIOR_MOUNT)
 info=json.loads(output('lsblk','-J','-o','NAME,TYPE,FSTYPE,UUID,MOUNTPOINTS',str(DISK)))['blockdevices']
 assert len(info)==1 and info[0]['type']=='disk' and info[0].get('fstype')=='ext4' and info[0].get('uuid')==UUID and not info[0].get('children') and info[0].get('mountpoints')==[str(MOUNT)]
 preparedMounts=mount_records(MOUNT)
 assert len(preparedMounts)==1 and preparedMounts[0]['source']==str(DISK.resolve()) and preparedMounts[0]['fstype']=='ext4'
 preparedEntries=list(MOUNT.iterdir())
 assert {p.name for p in preparedEntries}<=set(['lost+found','account.before-r4.sqlite','account.before-r4.sqlite-wal','account.before-r4.sqlite-shm'])
 assert all(regular(p) for p in preparedEntries if p.name!='lost+found')
 assert (MOUNT/'lost+found').is_dir() and not (MOUNT/'lost+found').is_symlink()
 prepared=dbfiles(PRESERVED);assert prepared and prepared[0]==PRESERVED and all(regular(p) for p in prepared)
 assert all(absent(MOUNT/name) for name in ['account.sqlite','account.sqlite-wal','account.sqlite-shm'])
 assert UUID.encode() not in originalFstab and str(MOUNT).encode() not in originalFstab and str(PRIOR_MOUNT).encode() not in originalFstab
 user=output('systemctl','show','commonplace','--property','User','--value');assert user=='commonplace'
 assert output('systemctl','show','commonplace','--property','Group','--value')=='commonplace'
 assert output('systemctl','show','commonplace','--property','ProtectSystem','--value')=='strict'
 assert str(OLD.parent) in output('systemctl','show','commonplace','--property','ReadWritePaths','--value').split()
 assert output('systemctl','show','commonplace-runtime','--property','User','--value')=='root'
 assert output('systemctl','show','commonplace-files','--property','User','--value')=='commonplace'
 assert '/var/lib/commonplace-files' in output('systemctl','show','commonplace-files','--property','ReadWritePaths','--value').split()
 originalRoles=unit_roles();identity=pwd.getpwnam(user)
 assert OLD.stat().st_uid==identity.pw_uid and OLD.stat().st_gid==identity.pw_gid
 assert all(p.stat().st_uid==identity.pw_uid and p.stat().st_gid==identity.pw_gid for p in prepared)
 oldDevice=OLD.stat().st_dev;oldInode=OLD.stat().st_ino;balancedDevice=prepared[0].stat().st_dev;assert oldDevice!=balancedDevice
 originalMounts=[r for r in mount_records(OLD.parent) if r['target']!=str(MOUNT)];assert originalMounts==previous['originalMounts']
 assert sum(r['source'].startswith('/dev/loop') for r in originalMounts)==3,'Expected exactly three existing SSH loop mounts'
 assert MOUNT.stat().st_dev==balancedDevice and (MOUNT.stat().st_uid,MOUNT.stat().st_gid)==(identity.pw_uid,identity.pw_gid) and stat.S_IMODE(MOUNT.stat().st_mode)==0o750
 no_holders(prepared);check_original_mounts()
 preparedHashes={p.name:{'sha256':digest(p),'bytes':p.stat().st_size} for p in prepared}
 assert preparedHashes=={k.replace('account.sqlite','account.before-r4.sqlite',1):v for k,v in previous['preparedFiles'].items()},'Preserved r3 target changed'
 save('prepared-nested-mount-verified',r4HelperSha256=PREVIOUS_HASH,preparedFiles=preparedHashes,originalMounts=originalMounts,unitRoles=originalRoles)
 timerSnapshot=backup_schedule_snapshot()
 if timerSnapshot.get('preexistingTimeout') is not None:state['preexistingBackupFailure']=dict(timerSnapshot['preexistingTimeout'])
 save('pausing-backup-timer',backupScheduleBefore=timerSnapshot)
 pause_backup_timer(timerSnapshot);wait_backup_idle(timerSnapshot)
 mainPid=int(output('systemctl','show','commonplace','--property','MainPID','--value'));assert mainPid>1
 probe=namespace_probe(mainPid,user)
 save('namespace-probe-passed',mainPid=mainPid,namespaceProbe=probe)
 assert regular(OLD) and (OLD.stat().st_dev,OLD.stat().st_ino)==(oldDevice,oldInode)
 assert all(output('systemctl','is-active',s)=='active' for s in services)
 assert unit_roles()==originalRoles and fstab.read_bytes()==originalFstab
 check_original_mounts()
 holders=expected_holders_only(dbfiles(OLD));assert_backup_paused(timerSnapshot)
 state['holdersBeforePause']=holders
 save('stopping-services');stopped=True;run('systemctl','stop',*services);stopped_services();no_holders(dbfiles(OLD))
 migrations=schema_as_user(OLD,user);assert len(migrations)==47
 checkpoint(OLD,user);assert dbfiles(OLD)==[OLD]
 sourceHash=digest(OLD);save('copying-closed-database',sourceSha256=sourceHash)
 staged=MOUNT/'.account.sqlite-copy-r5.tmp';copy(OLD,staged)
 assert schema_as_user(staged,user,quick=True)==migrations;checkpoint(staged,user);assert digest(staged)==sourceHash
 flush(staged);assert absent(NEW);os.replace(staged,NEW);flush(MOUNT)
 assert all(p.stat().st_uid==identity.pw_uid and p.stat().st_gid==identity.pw_gid for p in dbfiles(NEW))
 BACKUP.mkdir(mode=0o700);copy(OLD,BACKUP/OLD.name)
 flush(BACKUP/OLD.name);flush(BACKUP);flush(BACKUP.parent)
 assert fstab.read_bytes()==originalFstab
 installedFstab=originalFstab+('\nUUID='+UUID+' '+str(MOUNT)+' ext4 defaults 0 2\n').encode()
 setfstab(installedFstab);fstabChanged=True
 tempLink=OLD.parent/'.account.sqlite-balanced69-r5.tmp';assert absent(tempLink)
 tempLink.symlink_to(NEW);os.replace(tempLink,OLD);switched=True;flush(OLD.parent)
 os.sync();save('starting-services',originalDatabaseBackup=str(BACKUP),sourceSha256=sourceHash,migrations=47,newDiskUuid=UUID)
 start_app_services(OLD,user,identity)
 assert OLD.resolve()==NEW and schema_as_user(OLD,user)==migrations
 check_original_mounts();assert unit_roles()==originalRoles
 run('systemctl','start','nginx');assert all(output('systemctl','is-active',s)=='active' for s in services);stopped=False
 save('post-cutover-checks-passed',finishedAt=time.time(),durationSeconds=time.time()-state['startedAt'],services=['active']*4,originalMountUnchanged=True,sshWorkspaceMountsUntouched=True)
except Exception as error:
 state['failure']=type(error).__name__+': '+str(error);traceback.print_exc()
 try:
  if switched:
   stopped=True;run('systemctl','stop',*services);stopped_services();no_holders(dbfiles(NEW))
   checkpoint(NEW,user);assert OLD.is_symlink() and OLD.resolve()==NEW
   restored=OLD.parent/'.account.sqlite-rollback69-r5.tmp';copy(NEW,restored)
   assert schema_as_user(restored,user,quick=True)==migrations;checkpoint(restored,user);assert digest(restored)==digest(NEW)
   flush(restored);os.replace(restored,OLD);flush(OLD.parent);switched=False
  if fstabChanged:
   assert fstab.read_bytes()==installedFstab,'fstab changed after cutover; preserve concurrent edits'
   setfstab(originalFstab)
  if stopped:
   os.sync();start_app_services(OLD,user,identity);run('systemctl','start','nginx')
   assert all(output('systemctl','is-active',s)=='active' for s in services);stopped=False
   save('rolled-back',finishedAt=time.time(),balancedMountRetained=str(MOUNT))
  else:save('preflight-failed',finishedAt=time.time(),servicesUnchanged=True,balancedMountRetained=str(MOUNT))
 except Exception as recovery:
  state['recoveryFailure']=type(recovery).__name__+': '+str(recovery);save('requires-recovery');raise
finally:
 try:
  if timerSnapshot is not None:
   restore_backup_timer(timerSnapshot)
   save('passed' if state['state']=='post-cutover-checks-passed' else state['state'],backupTimerRestored=True)
 except Exception as timerError:
  state['timerRestoreFailure']=type(timerError).__name__+': '+str(timerError);save('requires-recovery');raise
 finally:
  result=ROOT/'result.json';result.write_text(json.dumps(state,indent=2));flush(result);flush(ROOT)
print(json.dumps(state))
