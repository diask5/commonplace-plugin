"""Extracted disposable regressions only: never execute the migration helper."""
import ast,concurrent.futures,hashlib,json,os,stat,subprocess,tempfile,threading,types,unittest,urllib.request,sqlite3,shutil
from pathlib import Path
HELPER=Path(__file__).with_name('migrate-database-storage69-r4.py')
TREE=ast.parse(HELPER.read_bytes())
FILES_READ_JS=next(ast.literal_eval(n.value) for n in TREE.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES_READ_JS' for t in n.targets)) if 'FILES_READ_JS=' in HELPER.read_text() else ''
def extracted(*names,**scope):
 nodes=[n for n in TREE.body if isinstance(n,ast.FunctionDef) and n.name in names]
 missing=set(names)-{n.name for n in nodes}
 if missing:raise AssertionError('Missing required safety helper: '+','.join(sorted(missing)))
 env=dict(Path=Path,os=os,json=json,stat=stat,hashlib=hashlib,subprocess=subprocess);env.update(scope)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(HELPER),'exec'),env)
 return env
def marker_helpers():
 if any(isinstance(n,ast.FunctionDef) and n.name=='claim_start' for n in TREE.body):return extracted('absent','flush','claim_start')
 # Run only the previous marker bootstrap, never preflight or migration.
 start=next(i for i,n in enumerate(TREE.body) if isinstance(n,ast.Assert) and ast.unparse(n.test)=='not ROOT.is_symlink()')
 end=next(i for i,n in enumerate(TREE.body[start:],start) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='fstab' for t in n.targets))
 code=compile(ast.Module(body=TREE.body[start:end],type_ignores=[]),str(HELPER),'exec')
 def claim(root,state):exec(code,dict(extracted('absent','flush'),ROOT=root,state=state))
 return {'claim_start':claim}
class ReviewFixChecks(unittest.TestCase):
 def test_exclusive_marker_two_synchronized_contenders_exactly_one_claim(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory)/'r4';root.mkdir(mode=0o700);(root/'migrate.py').write_text('launcher')
   barrier=threading.Barrier(2)
   class SyncPath(type(root)):
    def open(self,*args,**kw):
     if self.name=='started.json':barrier.wait(timeout=5)
     return super().open(*args,**kw)
   f=marker_helpers();root=SyncPath(root)
   def claim(n):
    try:f['claim_start'](root,{'contender':n});return True
    except FileExistsError:return False
   with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(claim,[1,2]))
   self.assertEqual(sorted(results),[False,True]);self.assertIn(json.loads((Path(root)/'started.json').read_text())['contender'],[1,2])
 def test_marker_existing_evidence_denies_rerun_launcher_only_allowed(self):
  f=marker_helpers()
  for filename in ['started.json','status.json','result.json']:
   with self.subTest(filename=filename),tempfile.TemporaryDirectory() as directory:
    root=Path(directory)/'r4';root.mkdir(mode=0o700);(root/filename).write_text('prior evidence')
    with self.assertRaises((AssertionError,FileExistsError)):f['claim_start'](root,{})
    self.assertEqual((root/filename).read_text(),'prior evidence')
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory)/'r4';root.mkdir(mode=0o700);(root/'migrate.py').write_text('launcher');f['claim_start'](root,{})
   self.assertTrue((root/'started.json').is_file())
 def test_marker_rejects_nonprivate_root_and_symlink_without_permissions_change(self):
  f=marker_helpers()
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory)/'r4';root.mkdir(mode=0o755);before=root.stat().st_mode
   with self.assertRaises(AssertionError):f['claim_start'](root,{})
   self.assertEqual(root.stat().st_mode,before);self.assertFalse((root/'started.json').exists())
   os.chmod(root,0o700);alias=Path(directory)/'alias';alias.symlink_to(root)
   with self.assertRaises(AssertionError):f['claim_start'](alias,{})
 def test_files_readiness_requires_actual_namespace_read(self):
  calls=[]
  class Reply:
   status=200
   def __enter__(self):return self
   def __exit__(self,*args):pass
  clock=types.SimpleNamespace(time=lambda:123,monotonic=lambda:0,sleep=lambda n:None)
  scope=extracted('start_app_services',time=clock,unit_roles=lambda:{},originalRoles={},run=lambda *a:None,waithealth=lambda:None,dbfiles=lambda p:[],output=lambda *a:'active' if a[0]=='systemctl' else '123000',urllib=types.SimpleNamespace(request=types.SimpleNamespace(urlopen=lambda *a,**k:Reply())),files_namespace_read=lambda *a:calls.append(a) or {},state={})
  scope['start_app_services'](Path('/synthetic/db'),'synthetic',types.SimpleNamespace(pw_uid=1,pw_gid=1))
  self.assertEqual(len(calls),1,'config200 must not bypass namespace auth DB proof')

 def test_config200_active_but_denied_or_stale_proof_fails_startup(self):
  class Reply:
   status=200
   def __enter__(self):return self
   def __exit__(self,*args):pass
  clock=types.SimpleNamespace(time=lambda:123,monotonic=lambda:0,sleep=lambda n:None)
  for error in [PermissionError('denied namespace'),AssertionError('wrong-device or stale DB')]:
   with self.subTest(error=str(error)):
    def fail(*args):raise error
    scope=extracted('start_app_services',time=clock,unit_roles=lambda:{},originalRoles={},run=lambda *a:None,waithealth=lambda:None,dbfiles=lambda p:[],output=lambda *a:'active' if a[0]=='systemctl' else '123000',urllib=types.SimpleNamespace(request=types.SimpleNamespace(urlopen=lambda *a,**k:Reply())),files_namespace_read=fail,state={})
    with self.assertRaises(type(error)):scope['start_app_services'](Path('/synthetic/db'),'synthetic',types.SimpleNamespace(pw_uid=1,pw_gid=1))

 def make_database(self,path,auth=True):
  db=sqlite3.connect(path)
  db.execute('CREATE TABLE cp_schema_migrations(name TEXT,digest TEXT)')
  rows=[['%02d'%n,'digest'+str(n)] for n in range(47)]
  db.executemany('INSERT INTO cp_schema_migrations VALUES(?,?)',rows)
  if auth:
   for table in ['cp_workspace_agent_tokens','cp_devices','cp_workspace_members']:
    db.execute('CREATE TABLE '+table+'(id TEXT)');db.execute('INSERT INTO '+table+" VALUES('PRIVATE-NEVER-READ')")
  db.commit();db.close();return rows
 def node_probe(self,configured,selected,rows,device=None,inode=None,script=None,**kw):
  info=selected.stat()
  return subprocess.run(['node','--input-type=module','-e',script or FILES_READ_JS,str(configured),str(selected),str(info.st_dev if device is None else device),str(info.st_ino if inode is None else inode),json.dumps(rows,separators=(',',':'))],capture_output=True,text=True,**kw)

 def test_files_exact_readonly_contract_syntax_and_no_fs_mutation_apis(self):
  subprocess.run(['node','--check','--input-type=module'],input=FILES_READ_JS,text=True,check=True)
  self.assertIn('new DatabaseSync(configured,{readOnly:true})',FILES_READ_JS)
  self.assertIn('PRAGMA query_only=ON; PRAGMA busy_timeout=5000;',FILES_READ_JS)
  self.assertNotIn('immutable',FILES_READ_JS)
  self.assertIn("import {statSync,realpathSync} from 'node:fs'",FILES_READ_JS)
  for forbidden in ['writeFile','mkdir','unlink','chmod','INSERT','UPDATE','DELETE','CREATE TABLE']:
   self.assertNotIn(forbidden,FILES_READ_JS)

 def test_current_symlink_and_rollback_regular_old_read_without_file_changes(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);old=root/'account.sqlite';target=root/'new.sqlite';rows=self.make_database(target);old.symlink_to(target)
   before={p.name:(p.read_bytes(),p.stat().st_mtime_ns) for p in root.iterdir() if not p.is_symlink()}
   result=self.node_probe(old,target,rows);self.assertEqual(result.returncode,0,result.stderr)
   proof=json.loads(result.stdout);self.assertTrue(proof['readOnly']);self.assertEqual(proof['migrations'],47);self.assertNotIn('PRIVATE',result.stdout)
   self.assertEqual(before,{p.name:(p.read_bytes(),p.stat().st_mtime_ns) for p in root.iterdir() if not p.is_symlink()})
   old.unlink();shutil.copy2(target,old);before={p.name:p.read_bytes() for p in root.iterdir()}
   result=self.node_probe(old,old,rows);self.assertEqual(result.returncode,0,result.stderr)
   self.assertEqual(before,{p.name:p.read_bytes() for p in root.iterdir()})

 def test_wrong_device_inode_path_stale_metadata_and_missing_auth_schema_fail(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);selected=root/'db';stale=root/'stale';rows=self.make_database(selected);self.make_database(stale)
   cases=[(selected,rows,{'device':selected.stat().st_dev+1}),(selected,rows,{'inode':selected.stat().st_ino+1}),(stale,rows,{}),(selected,[['stale','digest']],{})]
   for configured,metadata,options in cases:
    with self.subTest(options=options,configured=configured.name):
     result=self.node_probe(configured,selected,metadata,**options);self.assertNotEqual(result.returncode,0);self.assertEqual(result.stdout,'')
   broken=root/'broken';self.make_database(broken,auth=False)
   result=self.node_probe(broken,broken,rows);self.assertNotEqual(result.returncode,0);self.assertIn('auth schema missing',result.stderr)

 def test_readonly_driver_and_query_only_reject_sql_write(self):
  with tempfile.TemporaryDirectory() as directory:
   db=Path(directory)/'db';rows=self.make_database(db);before=db.read_bytes()
   injected=FILES_READ_JS.replace("db.exec('BEGIN');","db.exec('CREATE TABLE forbidden_write(v)');")
   result=self.node_probe(db,db,rows,script=injected);self.assertNotEqual(result.returncode,0);self.assertIn('readonly',result.stderr);self.assertEqual(db.read_bytes(),before)

 def test_unprivileged_denied_db_fails_without_any_writes(self):
  self.assertEqual(os.geteuid(),0,'Run extracted bootstrap tests with sudo; never run migration')
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);os.chmod(root,0o755);db=root/'db';rows=self.make_database(db);os.chmod(db,0o600);before=db.read_bytes()
   result=self.node_probe(db,db,rows,preexec_fn=lambda:os.setuid(65534));self.assertNotEqual(result.returncode,0);self.assertEqual(result.stdout,'');self.assertEqual(db.read_bytes(),before);self.assertEqual(len(list(root.iterdir())),1)

 def test_live_wal_schema_is_seen_without_immutable_or_checkpoint(self):
  with tempfile.TemporaryDirectory() as directory:
   db=Path(directory)/'db';rows=self.make_database(db,auth=False);writer=sqlite3.connect(db)
   try:
    writer.execute('PRAGMA journal_mode=WAL');writer.execute('PRAGMA wal_autocheckpoint=0')
    for table in ['cp_workspace_agent_tokens','cp_devices','cp_workspace_members']:writer.execute('CREATE TABLE '+table+'(id TEXT)')
    writer.execute("UPDATE cp_schema_migrations SET digest='fresh-in-wal' WHERE name='00'");writer.commit();rows[0][1]='fresh-in-wal'
    self.assertTrue(Path(str(db)+'-wal').is_file())
    result=self.node_probe(db,db,rows);self.assertEqual(result.returncode,0,result.stderr);self.assertTrue(json.loads(result.stdout)['walAware'])
   finally:writer.close()

 def test_namespace_dispatch_drops_user_and_rejects_pid_restart(self):
  with tempfile.TemporaryDirectory() as directory:
   db=Path(directory)/'db';rows=self.make_database(db);calls=[];process=(2222,'start','/configured/db')
   proof={'readOnly':True,'walAware':True,'selectedDatabase':True,'schemaMatches':True,'migrations':47,'schemaSha256':hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}
   scope=extracted('regular','files_namespace_read',FILES_READ_JS=FILES_READ_JS,schema_as_user=lambda *a:dict(rows),files_process=lambda *a:process,output=lambda *a:calls.append(a) or json.dumps(proof))
   self.assertEqual(scope['files_namespace_read'](db,'commonplace',None),proof)
   self.assertEqual(calls[0][:11],('nsenter','-t','2222','-m','--','runuser','-u','commonplace','--','/opt/node/bin/node','--input-type=module'))
   self.assertEqual(calls[0][-5:-3],('/configured/db',str(db)))
   answers=iter([process,(2223,'restart','/configured/db')]);scope['files_process']=lambda *a:next(answers)
   with self.assertRaisesRegex(AssertionError,'restarted'):scope['files_namespace_read'](db,'commonplace',None)
   answers=iter([process,(2222,'different-start','/configured/db')]);scope['files_process']=lambda *a:next(answers)
   with self.assertRaisesRegex(AssertionError,'restarted'):scope['files_namespace_read'](db,'commonplace',None)

 def test_files_process_exact_pid_executable_uid_cgroup_and_env_whitelist(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);proc=root/'proc/2222';proc.mkdir(parents=True);node=root/'node';node.write_text('synthetic');(proc/'exe').symlink_to(node);(proc/'cgroup').write_text('0::/system.slice/commonplace-files.service\n')
   configured=root/'account.sqlite';(proc/'environ').write_bytes(b'UNRELATED_SECRET=do-not-return\0FILES_ACCOUNT_DB='+str(configured).encode()+b'\0');(proc/'stat').write_text('2222 (node file) S '+' '.join(['0']*18+['birth']+['0']*4))
   def path(value):
    if str(value)=='/proc':return root/'proc'
    if str(value)=='/opt/node/bin/node':return node
    return Path(value)
   scope=extracted('files_process',unit_roles=lambda:{},originalRoles={},Path=path,OLD=configured,output=lambda *a:'active' if a[1]=='is-active' else '2222')
   identity=types.SimpleNamespace(pw_uid=os.getuid(),pw_gid=os.getgid())
   self.assertEqual(scope['files_process'](identity),(2222,'birth',str(configured)))
   for name,value in [('environ',b'FILES_ACCOUNT_DB=/wrong\0'),('cgroup',b'0::/system.slice/foreign.service\n')]:
    file=proc/name;before=file.read_bytes();file.write_bytes(value)
    with self.subTest(name=name),self.assertRaises(AssertionError):scope['files_process'](identity)
    file.write_bytes(before)
   with self.assertRaises(AssertionError):scope['files_process'](types.SimpleNamespace(pw_uid=os.getuid()+1,pw_gid=os.getgid()))
   scope['unit_roles']=lambda:{'changed':'role'}
   with self.assertRaises(AssertionError):scope['files_process'](identity)

if __name__=='__main__':unittest.main(verbosity=2)

