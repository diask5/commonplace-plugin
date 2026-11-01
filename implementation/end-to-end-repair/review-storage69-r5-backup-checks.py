"""Disposable extracted regressions; never execute privileged migration code."""
import ast,collections,json,os,stat,tempfile,types,unittest
from pathlib import Path
HELPER=Path(os.environ.get('STORAGE69_HELPER',str(Path(__file__).with_name('migrate-database-storage69-r5.py'))))
TREE=ast.parse(HELPER.read_bytes())
TIMER='commonplace-backup.timer';SERVICE='commonplace-backup.service'
def extracted(*names,**scope):
 nodes=[n for n in TREE.body if isinstance(n,ast.FunctionDef) and n.name in names]
 missing=set(names)-{n.name for n in nodes}
 if missing:raise AssertionError('Required safety behavior missing: '+','.join(sorted(missing)))
 env=dict(Path=Path,os=os,json=json,stat=stat,BACKUP_TIMER=TIMER,BACKUP_SERVICE=SERVICE,BACKUP_WAIT_SECONDS=10,backupTimerTouched=False,backupTimerOriginal=None,state={})
 env.update(scope);exec(compile(ast.Module(body=nodes,type_ignores=[]),str(HELPER),'exec'),env);return env
class BackupFixture:
 def __init__(self,active='active',states=None):
  self.active=active;self.prior=active;self.events=[];self.now=0
  self.states=collections.deque(states or [{'ActiveState':'inactive','SubState':'dead','MainPID':'0','ControlPID':'0','Result':'success','Job':'0'}])
  self.config={'timer':{'UnitFileState':'enabled','Unit':SERVICE,'Triggers':SERVICE,'PartOf':'','BindsTo':'','StopWhenUnneeded':'no','LoadState':'loaded'},'service':{'Type':'oneshot','Restart':'no','PartOf':'','BindsTo':'','StopWhenUnneeded':'no','TriggeredBy':TIMER,'LoadState':'loaded'}}
 def values(self,unit,keys):
  if unit==TIMER:return {key:({'ActiveState':self.active,'SubState':'waiting' if self.active=='active' else 'dead'}|self.config['timer'])[key] for key in keys}
  row=self.states[0]
  if len(self.states)>1:self.states.popleft()
  self.events.append(('backup-observed',row['ActiveState'],row['Job']))
  return {key:(row|self.config['service'])[key] for key in keys}
 def run(self,*args,**kw):
  self.events.append(args)
  if args==('systemctl','stop',TIMER):self.active='inactive'
  elif args==('systemctl','start',TIMER):self.active='active'
  else:raise AssertionError('Unexpected service mutation '+str(args))
 def sleep(self,n):self.now+=n
 def scope(self):
  return extracted('pause_backup_timer','wait_for_backup_completion','assert_backup_quiescent','restore_backup_timer',backup_configuration=lambda:self.config,unit_values=self.values,run=self.run,save=lambda *a,**kw:self.events.append(('save',a[0])),time=types.SimpleNamespace(monotonic=lambda:self.now,sleep=self.sleep))
def row(active='activating',pid='73',job='0',result='success'):
 return {'ActiveState':active,'SubState':'start' if active=='activating' else 'dead','MainPID':pid,'ControlPID':'0','Result':result,'Job':job}
class BackupChecks(unittest.TestCase):
 def test_active_backup_finishes_without_stop_or_kill_and_timer_restores(self):
  f=BackupFixture(states=[row(),row('active'),row('inactive','0')]);s=f.scope();s['pause_backup_timer']()
  self.assertEqual(f.active,'inactive');self.assertGreater(f.now,0);self.assertTrue(s['backupTimerTouched']);s['restore_backup_timer']()
  self.assertEqual(f.active,'active');self.assertFalse(s['backupTimerTouched'])
  self.assertEqual([e for e in f.events if e[0]=='systemctl'],[('systemctl','stop',TIMER),('systemctl','start',TIMER)])
 def test_original_inactive_timer_stays_inactive_and_enabled_state_unchanged(self):
  f=BackupFixture(active='inactive');s=f.scope();s['pause_backup_timer']();s['restore_backup_timer']()
  self.assertEqual(f.active,'inactive');self.assertEqual(f.config['timer']['UnitFileState'],'enabled');self.assertNotIn(('systemctl','start',TIMER),f.events)
 def test_timeout_does_not_signal_active_backup_and_restores_timer(self):
  f=BackupFixture(states=[row()]);s=f.scope()
  with self.assertRaisesRegex(RuntimeError,'finish'):s['pause_backup_timer']()
  self.assertEqual(f.active,'inactive');s['restore_backup_timer']();self.assertEqual(f.active,'active')
  self.assertTrue(all(e[2]==TIMER for e in f.events if e[0]=='systemctl'))
 def test_failed_backup_fails_before_app_pause_and_timer_restores(self):
  f=BackupFixture(states=[row('failed','0',result='exit-code')]);s=f.scope()
  with self.assertRaises((RuntimeError,AssertionError)):s['pause_backup_timer']()
  s['restore_backup_timer']();self.assertEqual(f.active,'active')
 def test_queued_backup_job_is_not_mistaken_for_idle(self):
  f=BackupFixture(states=[row('inactive','0',job='42'),row(),row('inactive','0')]);s=f.scope();s['pause_backup_timer']()
  self.assertGreaterEqual(f.now,2);s['restore_backup_timer']()
 def test_partial_timer_stop_failure_still_records_restoration_obligation(self):
  f=BackupFixture();s=f.scope();original=f.run
  def fail(*a,**kw):
   original(*a,**kw)
   if a==('systemctl','stop',TIMER):raise RuntimeError('synthetic partial stop')
  s['run']=fail
  with self.assertRaisesRegex(RuntimeError,'partial stop'):s['pause_backup_timer']()
  self.assertTrue(s['backupTimerTouched']);s['restore_backup_timer']();self.assertEqual(f.active,'active')
 def test_configuration_drift_fails_closed_without_enable_disable_or_override(self):
  f=BackupFixture();s=f.scope();s['pause_backup_timer']();f.config={'timer':dict(f.config['timer'],UnitFileState='disabled'),'service':f.config['service']}
  with self.assertRaises(AssertionError):s['restore_backup_timer']()
  self.assertEqual([e for e in f.events if e[0]=='systemctl'],[('systemctl','stop',TIMER)])
 def test_backup_cannot_reappear_immediately_before_pause(self):
  f=BackupFixture();s=f.scope();s['pause_backup_timer']();f.states=collections.deque([row()])
  with self.assertRaises((RuntimeError,AssertionError)):s['assert_backup_quiescent']()
  s['restore_backup_timer']()
 def test_relation_guard_rejects_timer_or_backup_stop_dependencies(self):
  for section,key,value in [('timer','PartOf','commonplace.service'),('service','BindsTo','commonplace-backup.timer'),('service','Restart','always'),('service','TriggeredBy','other.timer')]:
   f=BackupFixture();f.config[section][key]=value
   s=extracted('backup_configuration',unit_values=f.values)
   with self.subTest(section=section,key=key),self.assertRaises(AssertionError):s['backup_configuration']()
 def test_preflight_holders_accept_expected_cgroups_and_reject_backup_or_unknown(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);db=root/'db';db.write_text('synthetic');proc=root/'proc';fd=proc/'123/fd';fd.mkdir(parents=True);os.link(db,fd/'4');cgroup=proc/'123/cgroup'
   cgroup.write_text('0::/system.slice/commonplace.service\n')
   def path(value):return proc if str(value)=='/proc' else Path(value)
   s=extracted('assert_expected_holders',Path=path,output=lambda *a:'/system.slice/'+a[2])
   self.assertEqual(s['assert_expected_holders']([db]),[{'pid':123,'unit':'commonplace.service'}])
   for name in ['commonplace-backup.service','foreign.service','commonplace.service-forged']:
    cgroup.write_text('0::/system.slice/'+name+'\n')
    with self.subTest(name=name),self.assertRaisesRegex(AssertionError,'holder'):s['assert_expected_holders']([db])
 def test_no_mount_reformat_backup_stop_or_policy_commands(self):
  text=HELPER.read_text();commands=[]
  for n in ast.walk(TREE):
   if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in ['run','output'] and n.args and isinstance(n.args[0],ast.Constant):commands.append(n.args[0].value)
  self.assertNotIn('mount',commands);self.assertNotIn('umount',commands);self.assertNotIn('mkfs.ext4',commands)
  self.assertNotIn('daemon-reload',text);self.assertNotIn('os.kill',text)
  self.assertIn("PREVIOUS_HASH='3aab196a49f859a0716b7c99a28fe72b0d0f4a7a3f9a81ed07e6b249a00f0eb3'",text)
 def test_timer_restoration_is_finally_after_checks_and_holders_before_pause(self):
  body=next(n for n in TREE.body if isinstance(n,ast.Try) and any(isinstance(x,ast.Assert) and 'PREVIOUS_HASH' in ast.unparse(x) for x in n.body))
  rendered=[ast.unparse(x) for x in body.body]
  pause=next(i for i,x in enumerate(rendered) if "run('systemctl', 'stop', *services)" in x)
  self.assertTrue(any('pause_backup_timer()' in x for x in rendered[:pause]));self.assertTrue(any('assert_expected_holders(' in x for x in rendered[:pause]));self.assertTrue(any('assert_backup_quiescent()' in x for x in rendered[:pause]))
  self.assertIn('restore_backup_timer()',ast.unparse(ast.Module(body=body.finalbody,type_ignores=[])))
if __name__=='__main__':unittest.main(verbosity=2)
