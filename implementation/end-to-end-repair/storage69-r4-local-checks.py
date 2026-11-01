"""Exercise extracted helpers with synthetic local files; never execute migration."""
import ast,hashlib,json,os,shutil,sqlite3,subprocess,tempfile,types,unittest
from pathlib import Path

HELPER=Path(__file__).with_name('migrate-database-storage69-r4.py')
TREE=ast.parse(HELPER.read_bytes(),filename=str(HELPER))
PROBE=next(ast.literal_eval(n.value) for n in TREE.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PROBE_JS' for t in n.targets))
NAMES={'absent','regular','flush','digest','copy','dbfiles','schema_as_user','checkpoint','no_holders','namespace_probe'}
def helpers():
 scope={'Path':Path,'os':os,'hashlib':hashlib,'shutil':shutil,'json':json,'subprocess':subprocess,'PROBE_JS':PROBE}
 def local_command(args):
  assert args[:2]==('runuser','-u') and args[3]=='--'
  command=list(args[4:])
  if command[0]=='/opt/node/bin/node':command[0]=shutil.which('node')
  return command
 scope['run']=lambda *args,**kw:subprocess.run(local_command(args),check=True,**kw)
 scope['output']=lambda *args:subprocess.check_output(local_command(args),text=True).strip()
 exec(compile(ast.Module(body=[n for n in TREE.body if isinstance(n,ast.FunctionDef) and n.name in NAMES],type_ignores=[]),str(HELPER),'exec'),scope)
 return scope

class LocalChecks(unittest.TestCase):
 def test_syntax_and_no_format_or_sandbox_mutation(self):
  subprocess.run(['node','--check','--input-type=module'],input=PROBE,text=True,check=True)
  commands=[]
  for node in ast.walk(TREE):
   if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in ['run','output'] and node.args and isinstance(node.args[0],ast.Constant):commands.append(node.args[0].value)
  self.assertNotIn('mkfs.ext4',commands);self.assertNotIn('chmod',commands)
  self.assertNotIn('systemd-run',commands);self.assertNotIn('daemon-reload',HELPER.read_text())

 def test_exact_probe_cross_filesystem_alias_wal_and_cleanup(self):
  with tempfile.TemporaryDirectory() as original,tempfile.TemporaryDirectory(dir='/dev/shm') as balanced:
   old=Path(original);new=Path(balanced);self.assertNotEqual(old.stat().st_dev,new.stat().st_dev)
   result=subprocess.run(['node','--input-type=module','-e',PROBE,str(old/'probe.sqlite'),str(new/'probe.sqlite'),str(new.stat().st_dev),str(old.stat().st_dev)],check=True,capture_output=True,text=True)
   self.assertEqual(json.loads(result.stdout),{'device':new.stat().st_dev,'namespaceWrite':True,'sqliteAlias':True,'walShared':True})
   self.assertEqual(list(old.iterdir()),[]);self.assertEqual(list(new.iterdir()),[])

 def test_missing_namespace_mount_fails_before_any_probe_write(self):
  with tempfile.TemporaryDirectory() as original,tempfile.TemporaryDirectory(dir='/dev/shm') as balanced:
   old=Path(original);new=Path(balanced);wrong=new.stat().st_dev+1
   if wrong==old.stat().st_dev:wrong+=1
   result=subprocess.run(['node','--input-type=module','-e',PROBE,str(old/'probe.sqlite'),str(new/'probe.sqlite'),str(wrong),str(old.stat().st_dev)],capture_output=True,text=True)
   self.assertNotEqual(result.returncode,0);self.assertIn('Nested balanced mount absent',result.stderr)
   self.assertEqual(list(old.iterdir()),[]);self.assertEqual(list(new.iterdir()),[])

 def test_staged_copy_and_atomic_rollback_preserve_latest_committed_data(self):
  f=helpers()
  with tempfile.TemporaryDirectory() as original,tempfile.TemporaryDirectory(dir='/dev/shm') as balanced:
   old=Path(original)/'account.sqlite';new=Path(balanced)/'account.sqlite';backup=Path(original)/'backup.sqlite';stage=Path(balanced)/'copy.tmp'
   db=sqlite3.connect(old)
   try:
    db.execute('PRAGMA journal_mode=WAL');db.execute('CREATE TABLE cp_schema_migrations(name TEXT,digest TEXT)');db.executemany('INSERT INTO cp_schema_migrations VALUES(?,?)',[(str(i),'digest'+str(i)) for i in range(47)]);db.execute('CREATE TABLE t(value TEXT)');db.execute("INSERT INTO t VALUES('before')");db.commit()
   finally:db.close()
   migrations=f['schema_as_user'](old,'synthetic');f['checkpoint'](old,'synthetic');source=f['digest'](old)
   f['copy'](old,backup);f['copy'](old,stage)
   self.assertEqual(f['schema_as_user'](stage,'synthetic',quick=True),migrations);f['checkpoint'](stage,'synthetic');self.assertEqual(f['digest'](stage),source)
   f['flush'](stage);os.replace(stage,new);f['flush'](new.parent)
   alias=old.parent/'switch.tmp';alias.symlink_to(new);os.replace(alias,old)
   db=sqlite3.connect(new)
   try:db.execute("UPDATE t SET value='latest committed'");db.commit()
   finally:db.close()
   f['checkpoint'](new,'synthetic');restored=old.parent/'rollback.tmp';f['copy'](new,restored)
   self.assertEqual(f['schema_as_user'](restored,'synthetic',quick=True),migrations);f['checkpoint'](restored,'synthetic');self.assertEqual(f['digest'](restored),f['digest'](new))
   f['flush'](restored);os.replace(restored,old);f['flush'](old.parent)
   self.assertFalse(old.is_symlink())
   for file,value in [(old,'latest committed'),(backup,'before')]:
    db=sqlite3.connect(file)
    try:self.assertEqual(db.execute('SELECT value FROM t').fetchone()[0],value)
    finally:db.close()
   with self.assertRaises(AssertionError):f['copy'](new,old)

 def test_holder_guard_matches_inode_aliases_and_fails_closed_on_permissions(self):
  f=helpers()
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);db=root/'db';db.write_text('synthetic');proc=root/'proc';fd=proc/'1/fd';fd.mkdir(parents=True);os.link(db,fd/'3')
   f['Path']=lambda p:proc if str(p)=='/proc' else Path(p)
   with self.assertRaisesRegex(AssertionError,'holder PID 1'):f['no_holders']([db])
   (fd/'3').unlink();f['no_holders']([db])
   class Denied:
    name='1'
    def __truediv__(self,part):return self
    def iterdir(self):raise PermissionError('synthetic denied')
   class Proc:
    def iterdir(self):return iter([Denied()])
   f['Path']=lambda p:Proc() if str(p)=='/proc' else Path(p)
   with self.assertRaises(PermissionError):f['no_holders']([db])

 def test_namespace_command_targets_verified_main_pid_and_drops_user(self):
  f=helpers()
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);proc=root/'proc/2222';proc.mkdir(parents=True);node=root/'node';node.write_text('synthetic');(proc/'exe').symlink_to(node);(proc/'cgroup').write_text('0::/system.slice/commonplace.service\n')
   old=root/'original';new=root/'balanced';old.mkdir();new.mkdir();captured=[]
   def path(value):
    if str(value).startswith('/proc/'):return root/str(value).lstrip('/')
    if str(value)=='/opt/node/bin/node':return node
    return Path(value)
   def output(*args):
    if args[0]=='systemctl':return '2222'
    self.assertEqual(args[0],'nsenter');captured.append(args)
    return json.dumps({'device':123,'namespaceWrite':True,'sqliteAlias':True,'walShared':True})
   f.update(Path=path,output=output,OLD=old/'account.sqlite',MOUNT=new,identity=types.SimpleNamespace(pw_uid=os.getuid()),balancedDevice=123,oldDevice=456)
   f['namespace_probe'](2222,'commonplace')
   self.assertEqual(captured[0][:11],('nsenter','-t','2222','-m','--','runuser','-u','commonplace','--','/opt/node/bin/node','--input-type=module'))
   self.assertEqual(captured[0][-2:],('123','456'))

if __name__=='__main__':unittest.main(verbosity=2)
