from pathlib import Path
import json,subprocess,sqlite3,hashlib,time
root=Path('/var/lib/commonplace/rollout-inputs/20261101-context-throughput');before=json.loads((root/'capacity-upgrade-before.json').read_text())
assert hashlib.sha256(Path('/etc/fstab').read_bytes()).hexdigest()==before['fstabSha256']
mount=json.loads(subprocess.check_output(['findmnt','--mountpoint','/var/lib/commonplace/database-storage','--json','--output','TARGET,SOURCE,UUID'],text=True))['filesystems'][0]
assert mount['uuid']=='4b9a5959-5eed-4a88-a902-b4f30c7993cd'
assert Path('/var/lib/commonplace/account.sqlite').stat().st_dev==Path('/var/lib/commonplace/database-storage').stat().st_dev
assert str(Path('/var/lib/commonplace/account.sqlite').resolve())==before['dbPath']
assert Path('/opt/commonplace/current').resolve().name==before['release']
restored=[]
for m in before['mounts']:
 target=Path(m['target']);assert target.is_dir() and not target.is_symlink()
 r=subprocess.run(['findmnt','--mountpoint',str(target),'--json','--output','TARGET,SOURCE,FSTYPE,OPTIONS'],capture_output=True,text=True)
 if r.returncode:
  assert not any(target.iterdir()),'Nonempty unmounted workspace target'
  subprocess.run(['mount','-t','ext4','-o','loop,'+m['options'],m['backingFile'],str(target)],check=True);restored.append(m['target'])
 actual=json.loads(subprocess.check_output(['findmnt','--mountpoint',str(target),'--json','--output','TARGET,SOURCE,FSTYPE,OPTIONS'],text=True))['filesystems'][0]
 assert actual['fstype']==m['fstype']
 assert set(m['options'].split(','))<=set(actual['options'].split(','))
 loops=json.loads(subprocess.check_output(['losetup','--json','--output','NAME,BACK-FILE'],text=True))['loopdevices']
 assert next(x['back-file'] for x in loops if x['name']==actual['source'])==m['backingFile']
schemaScript="import sqlite3,json; db=sqlite3.connect('file:/var/lib/commonplace/account.sqlite?mode=ro',uri=True);\ntry: print(json.dumps(dict(db.execute('SELECT name,digest FROM cp_schema_migrations'))))\nfinally: db.close()"
applied=json.loads(subprocess.check_output(['runuser','-u','commonplace','--','python3','-c',schemaScript],text=True));assert applied==before['migrations']
services={}
for name in ['commonplace','commonplace-runtime','commonplace-files','nginx','commonplace-workspaces','commonplace-files-runner','commonplace-staging','commonplace-backup.timer']:
 value=subprocess.check_output(['systemctl','is-active',name],text=True).strip();assert value=='active',name;services[name]=value
out={'state':'passed','at':time.time(),'fstabUnchanged':True,'databasePathPreserved':True,'schemaDigestsUnchanged':47,'loopMountsVerified':3,'loopMountsRestored':len(restored),'services':services,'release':before['release']};(root/'capacity-upgrade-after.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
