from pathlib import Path
import os,json,subprocess,shutil,hashlib,time,sqlite3,urllib.request,traceback,stat,pwd
os.umask(0o077)
ROOT=Path('/var/tmp/commonplace-storage-20261101');ROOT.mkdir(parents=True,exist_ok=True)
DISK=Path('/dev/disk/by-id/google-commonplace-data-balanced-20261101');MOUNT=Path('/var/lib/commonplace-db');OLD=Path('/var/lib/commonplace/account.sqlite');NEW=MOUNT/'account.sqlite';BACKUP=Path('/var/lib/commonplace/storage-before-balanced-20261101')
assert not (ROOT/'started.json').exists(),'Migration already started; inspect saved result before any retry'
state={'startedAt':time.time(),'state':'preflight','oldDiskRetained':True,'databasePathPreserved':True,'hostPoliciesChanged':False};(ROOT/'started.json').write_text(json.dumps(state))
def flush(p):
 fd=os.open(p,os.O_RDONLY)
 try:os.fsync(fd)
 finally:os.close(fd)
def save(phase,**extra):
 state.update(state=phase,**extra);p=ROOT/'status.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(state,indent=2));flush(t);t.replace(p);flush(ROOT)
def run(*args,**kw):return subprocess.run(args,check=True,**kw)
def output(*args):return subprocess.check_output(args,text=True).strip()
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def copy(p,q):
 shutil.copy2(p,q);s=p.stat();os.chown(q,s.st_uid,s.st_gid);assert digest(p)==digest(q)
def dbfiles(base):return [p for suffix in ['', '-wal','-shm'] if (p:=Path(str(base)+suffix)).exists()]
def schema_as_user(file,user,quick=False):
 code="import sqlite3,json,sys;from contextlib import closing\nwith closing(sqlite3.connect('file:'+sys.argv[1]+'?mode=ro',uri=True)) as db:\n if sys.argv[2]=='1': assert db.execute('PRAGMA quick_check').fetchall()==[('ok',)]\n print(json.dumps(dict(db.execute('SELECT name,digest FROM cp_schema_migrations'))))"
 return json.loads(output('runuser','-u',user,'--','python3','-c',code,str(file),'1' if quick else '0'))
def checkpoint(file,user):
 js="import {DatabaseSync} from 'node:sqlite';const d=new DatabaseSync(process.argv[1]);try{if(d.prepare('PRAGMA wal_checkpoint(TRUNCATE)').get().busy!==0)throw Error('WAL is busy');}finally{d.close();}"
 run('runuser','-u',user,'--','/opt/node/bin/node','--input-type=module','-e',js,str(file),stdout=subprocess.DEVNULL)
 wal=Path(str(file)+'-wal');assert not wal.exists() or wal.stat().st_size==0
 for suffix in ['-wal','-shm']:
  p=Path(str(file)+suffix)
  if p.exists():p.unlink()
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
services=['nginx','commonplace-runtime','commonplace'];stopped=False;switched=False;fstabChanged=False;mounted=False
fstab=Path('/etc/fstab');originalFstab=fstab.read_bytes();fstabStat=fstab.stat();(ROOT/'fstab.before').write_bytes(originalFstab)
def setfstab(data):
 temp=Path('/etc/fstab.commonplace-storage.tmp');temp.write_bytes(data);os.chmod(temp,stat.S_IMODE(fstabStat.st_mode));os.chown(temp,fstabStat.st_uid,fstabStat.st_gid);flush(temp);temp.replace(fstab);flush(fstab.parent)
try:
 assert OLD.is_file() and not OLD.is_symlink() and not BACKUP.exists()
 assert output('findmnt','-rn','-M','/var/lib/commonplace','-o','SOURCE')=='/dev/sdb'
 assert DISK.resolve()==Path('/dev/sdc') and stat.S_ISBLK(DISK.stat().st_mode)
 info=json.loads(output('lsblk','-J','-o','NAME,TYPE,FSTYPE,MOUNTPOINTS',str(DISK)))['blockdevices'];assert len(info)==1 and info[0]['type']=='disk' and not info[0].get('fstype') and not info[0].get('children') and not any(info[0].get('mountpoints',[]))
 assert not MOUNT.exists() or not any(MOUNT.iterdir());assert all(output('systemctl','is-active',s)=='active' for s in services)
 assert b'/var/lib/commonplace-db' not in originalFstab
 save('formatting-new-empty-disk');run('mkfs.ext4','-F','-L','commonplace-db',str(DISK),stdout=subprocess.DEVNULL)
 MOUNT.mkdir(exist_ok=True);run('mount',str(DISK),str(MOUNT));mounted=True;assert MOUNT.stat().st_dev!=OLD.parent.stat().st_dev
 user=output('systemctl','show','commonplace','--property','User','--value');assert user=='commonplace' and output('systemctl','show','commonplace-runtime','--property','User','--value')==user
 identity=pwd.getpwnam(user);os.chown(MOUNT,identity.pw_uid,identity.pw_gid);os.chmod(MOUNT,0o750)
 uuid=output('blkid','-s','UUID','-o','value',str(DISK));assert uuid and '\n' not in uuid
 # Exercise the exact Node SQLite driver against a symlink across these filesystems.
 probe=OLD.parent/'.storage-probe69.sqlite';target=MOUNT/'probe.sqlite';assert not probe.exists() and not probe.is_symlink();probe.symlink_to(target)
 js="import {DatabaseSync} from 'node:sqlite';const a=new DatabaseSync(process.argv[1]),b=new DatabaseSync(process.argv[2]);a.exec('PRAGMA journal_mode=WAL; PRAGMA synchronous=FULL; CREATE TABLE t(v); INSERT INTO t VALUES (1)');if(b.prepare('SELECT v FROM t').get().v!==1)throw Error('Alias did not share WAL');b.exec('INSERT INTO t VALUES(2)');if(a.prepare('SELECT count(*) n FROM t').get().n!==2)throw Error('Reverse WAL alias mismatch');const p=a.prepare('PRAGMA database_list').get().file;if(p!==process.argv[2])throw Error('Driver did not canonicalize symlink');b.close();a.close();"
 run('runuser','-u',user,'--','/opt/node/bin/node','--input-type=module','-e',js,str(probe),str(target),stdout=subprocess.DEVNULL)
 probe.unlink()
 for p in dbfiles(target):p.unlink()
 save('stopping-services',sqliteAliasProbe=True,newDiskUuid=uuid);stopped=True;run('systemctl','stop',*services)
 assert all(output('systemctl','show',s,'--property','MainPID','--value')=='0' for s in services)
 # Reject any unexpected remaining process holding the database or its WAL.
 names={str(p) for p in dbfiles(OLD)}
 for proc in Path('/proc').iterdir():
  if not proc.name.isdigit() or int(proc.name)==os.getpid():continue
  try:
   for fd in (proc/'fd').iterdir():
    try:link=os.readlink(fd)
    except FileNotFoundError:continue
    assert link not in names,'Unexpected remaining database holder '+proc.name
  except (FileNotFoundError,PermissionError):continue
 checkpoint(OLD,user)
 save('copying-closed-database');files=dbfiles(OLD);assert files==[OLD];hashes={p.name:digest(p) for p in files}
 for p in files:copy(p,MOUNT/p.name)
 migrations=schema_as_user(NEW,user,quick=True);assert len(migrations)==47
 assert all(p.stat().st_uid==identity.pw_uid and p.stat().st_gid==identity.pw_gid for p in dbfiles(NEW)),'Unexpected database or sidecar ownership'
 # The old pathname stays usable by deployment, backup and read-only tools.
 BACKUP.mkdir(mode=0o700);copy(OLD,BACKUP/OLD.name)
 flush(NEW);flush(MOUNT);flush(BACKUP/OLD.name);flush(BACKUP);flush(BACKUP.parent)
 assert fstab.read_bytes()==originalFstab,'fstab changed concurrently'
 installedFstab=originalFstab+b'\nUUID='+uuid.encode()+b' /var/lib/commonplace-db ext4 defaults 0 2\n'
 setfstab(installedFstab);fstabChanged=True
 tempLink=OLD.parent/'.account.sqlite-balanced69.tmp';assert not tempLink.exists() and not tempLink.is_symlink();tempLink.symlink_to(NEW);os.replace(tempLink,OLD);switched=True;flush(OLD.parent)
 os.sync();save('starting-services',copiedFileHashes=hashes,migrations=47,originalDatabaseBackup=str(BACKUP));run('systemctl','start','commonplace','commonplace-runtime');waithealth()
 assert OLD.resolve()==NEW and output('findmnt','-rn','-M',str(MOUNT),'-o','SOURCE')==str(DISK.resolve())
 assert schema_as_user(OLD,user)==migrations
 run('systemctl','start','nginx');assert all(output('systemctl','is-active',s)=='active' for s in services);stopped=False
 save('passed',finishedAt=time.time(),durationSeconds=time.time()-state['startedAt'],services=['active']*3,originalMountUnchanged=True,sshWorkspaceMountsUntouched=True)
except Exception as error:
 state['failure']=type(error).__name__+': '+str(error);traceback.print_exc()
 try:
  if switched:
   stopped=True;run('systemctl','stop',*services)
   # Checkpoint and atomically publish a verified reverse copy, including any
   # work committed after startup; never expose a missing or partial database.
   checkpoint(NEW,user);assert OLD.is_symlink() and OLD.resolve()==NEW
   restored=OLD.parent/'.account.sqlite-rollback69.tmp';assert not restored.exists();copy(NEW,restored);assert schema_as_user(restored,user,quick=True)==migrations;flush(restored);os.replace(restored,OLD);flush(OLD.parent);switched=False
  if fstabChanged:
   assert fstab.read_bytes()==installedFstab,'fstab changed after cutover; preserve concurrent edits'
   setfstab(originalFstab)
  os.sync()
  if stopped:run('systemctl','start','commonplace','commonplace-runtime');waithealth();run('systemctl','start','nginx');stopped=False
  save('rolled-back',finishedAt=time.time())
 except Exception as recovery:
  state['recoveryFailure']=type(recovery).__name__+': '+str(recovery);save('requires-recovery');raise
else:print(json.dumps(state))
finally:(ROOT/'result.json').write_text(json.dumps(state,indent=2))
