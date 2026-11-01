"""Disposable extracted helper checks only; never execute migration/preflight."""
import ast,json,os,subprocess,tempfile,time,types,unittest
from pathlib import Path
HELPER=Path(__file__).with_name('migrate-database-storage69-r5.py')
TREE=ast.parse(HELPER.read_bytes())
TIMER='commonplace-backup.timer';SERVICE='commonplace-backup.service'
def extract(*names,**scope):
 nodes=[n for n in TREE.body if isinstance(n,ast.FunctionDef) and n.name in names]
 missing=set(names)-{n.name for n in nodes}
 if missing:raise AssertionError('Missing backup/holder safety helper: '+','.join(sorted(missing)))
 env=dict(Path=Path,os=os,json=json,time=time,BACKUP_TIMER=TIMER,BACKUP_SERVICE=SERVICE,subprocess=subprocess);env.update(scope)
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(HELPER),'exec'),env);return env
SCHEDULER_NAMES=['backup_live_state','backup_schedule_contract','backup_schedule_snapshot','check_backup_contract','pause_backup_timer','wait_backup_idle','assert_backup_paused','restore_backup_timer']
class Fixture:
 def __init__(self,active='active',states=None):
  self.active=active;self.calls=[];self.now=0
  self.timer={'Unit':SERVICE,'Triggers':SERVICE,'PartOf':'','BindsTo':'','StopWhenUnneeded':'no','PropagatesStopTo':'','UnitFileState':'enabled'}
  self.backup={'Type':'oneshot','Restart':'no','TimeoutStartUSec':'5min','PartOf':'','BindsTo':'','StopWhenUnneeded':'no','TriggeredBy':TIMER,'Requires':'sysinit.target'}
  self.states=iter(states or []);self.live={'ActiveState':'inactive','SubState':'dead','MainPID':'0','Result':'success'}
 def properties(self,unit,names):
  if unit==TIMER:values=dict(self.timer,ActiveState=self.active,SubState='waiting' if self.active=='active' else 'dead')
  else:
   if 'ActiveState' in names:self.live=next(self.states,self.live)
   defaults={'ExecMainStatus':'0','InvocationID':'','ExecMainStartTimestampMonotonic':'0','ExecMainExitTimestampMonotonic':'0','ExecMainExitTimestamp':'','ExecMainStartTimestamp':'','ExecMainPID':'0','ExecMainCode':'0'}
   values=dict(self.backup,**dict(defaults,**self.live))
  return {k:values[k] for k in names}
 def run(self,*args):
  self.calls.append(args)
  assert args[:1]==('systemctl',) and args[-1]==TIMER,'Only timer start/stop permitted'
  assert args[1] in ['start','stop']
  self.active='active' if args[1]=='start' else 'inactive'
 def sleep(self,n):self.now+=n
 def scope(self):return extract(*SCHEDULER_NAMES,unit_properties=self.properties,run=self.run,time=types.SimpleNamespace(monotonic=lambda:self.now,sleep=self.sleep))
class SchedulerChecks(unittest.TestCase):
 def test_finally_restores_timer_after_all_post_cutover_checks(self):
  outer=next(n for n in TREE.body if isinstance(n,ast.Try))
  self.assertIn('restore_backup_timer',ast.unparse(ast.Module(body=outer.finalbody,type_ignores=[])))
  self.assertNotIn('restore_backup_timer',ast.unparse(ast.Module(body=outer.body,type_ignores=[])))
 def test_prepared_nested_disk_is_reused_without_mount_or_format_or_renames(self):
  commands=[n.args[0].value for n in ast.walk(TREE) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in ['run','output'] and n.args and isinstance(n.args[0],ast.Constant)]
  for forbidden in ['mount','umount','mkfs.ext4']:self.assertNotIn(forbidden,commands)
  code=HELPER.read_text();self.assertNotIn('p.rename(saved)',code);self.assertIn("PRESERVED=MOUNT/'account.before-r4.sqlite'",code)
 def test_timer_helpers_exist(self):extract('backup_schedule_snapshot','pause_backup_timer','wait_backup_idle','assert_backup_paused','restore_backup_timer')
 def test_pre_pause_holder_gate_exists(self):extract('expected_holders_only')

 def test_active_timer_paused_running_backup_finishes_and_prior_active_restored(self):
  states=[{'ActiveState':'activating','SubState':'start','MainPID':'1234','Result':'success'},{'ActiveState':'active','SubState':'running','MainPID':'1234','Result':'success'},{'ActiveState':'inactive','SubState':'dead','MainPID':'0','Result':'success'}]
  x=Fixture(states=states);f=x.scope();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);f['wait_backup_idle'](snapshot);f['assert_backup_paused'](snapshot)
  self.assertEqual(x.calls,[('systemctl','stop',TIMER)]);self.assertEqual(x.now,1)
  f['restore_backup_timer'](snapshot);self.assertEqual(x.active,'active');self.assertEqual(x.calls,[('systemctl','stop',TIMER),('systemctl','start',TIMER)])

 def test_original_inactive_timer_stays_inactive_without_enable_or_disable(self):
  x=Fixture(active='inactive');f=x.scope();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);f['wait_backup_idle'](snapshot);f['restore_backup_timer'](snapshot)
  self.assertEqual(x.calls,[]);self.assertEqual(x.active,'inactive')

 def test_backup_timeout_is_bounded_without_signals_or_service_stop(self):
  x=Fixture();x.live={'ActiveState':'activating','SubState':'start','MainPID':'1234','Result':'success'};f=x.scope();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot)
  with self.assertRaisesRegex(RuntimeError,'not signaled'):f['wait_backup_idle'](snapshot)
  self.assertEqual(x.now,315);f['restore_backup_timer'](snapshot);self.assertEqual(x.active,'active');self.assertTrue(all(c[-1]==TIMER for c in x.calls))

 def test_backup_failure_or_remaining_pid_aborts_without_app_pause(self):
  for live in [{'ActiveState':'failed','SubState':'failed','MainPID':'0','Result':'timeout'},{'ActiveState':'inactive','SubState':'dead','MainPID':'44','Result':'success'},{'ActiveState':'inactive','SubState':'dead','MainPID':'0','Result':'exit-code'}]:
   with self.subTest(live=live):
    x=Fixture();x.live=live;f=x.scope()
    with self.assertRaises(AssertionError):
     snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);f['wait_backup_idle'](snapshot)
    self.assertTrue(all(c[-1]==TIMER for c in x.calls))

 def test_stopping_timer_dependency_coupling_is_rejected_before_mutation(self):
  for section,key,value in [('timer','PropagatesStopTo',SERVICE),('timer','BindsTo',SERVICE),('backup','PartOf',TIMER),('backup','Requires',TIMER),('backup','Restart','always'),('backup','Type','simple')]:
   with self.subTest(key=key):
    x=Fixture();getattr(x,section)[key]=value
    with self.assertRaises(AssertionError):x.scope()['backup_schedule_snapshot']()
    self.assertEqual(x.calls,[])

 def test_changed_contract_or_timer_or_backup_restart_blocks_app_pause(self):
  for change in ['timer','backup','contract']:
   with self.subTest(change=change):
    x=Fixture();f=x.scope();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot)
    if change=='timer':x.active='active'
    elif change=='backup':x.live={'ActiveState':'activating','SubState':'start','MainPID':'33','Result':'success'}
    else:x.timer['UnitFileState']='disabled'
    with self.assertRaises(AssertionError):f['assert_backup_paused'](snapshot)
    self.assertEqual(x.calls,[('systemctl','stop',TIMER)])

 def test_finally_restores_on_pass_rollback_preflight_and_failed_recovery(self):
  outer=next(n for n in TREE.body if isinstance(n,ast.Try));code=compile(ast.Module(body=outer.finalbody,type_ignores=[]),str(HELPER),'exec')
  for phase in ['post-cutover-checks-passed','rolled-back','preflight-failed','requires-recovery']:
   with self.subTest(phase=phase),tempfile.TemporaryDirectory() as directory:
    calls=[];state={'state':phase};root=Path(directory)
    def save(phase,**kw):state.update(state=phase,**kw);calls.append('save')
    scope=dict(timerSnapshot={'present':True},restore_backup_timer=lambda s:calls.append('restore'),save=save,state=state,ROOT=root,json=json,flush=lambda p:calls.append('flush'))
    exec(code,scope)
    self.assertEqual(calls[:2],['restore','save']);result=json.loads((root/'result.json').read_text());self.assertEqual(result['state'],'passed' if phase=='post-cutover-checks-passed' else phase);self.assertTrue(result['backupTimerRestored'])
  with tempfile.TemporaryDirectory() as directory:
   def fail(s):raise OSError('timer restore denied')
   state={'state':'post-cutover-checks-passed'}
   def save(phase,**kw):state.update(state=phase,**kw)
   scope=dict(timerSnapshot={},restore_backup_timer=fail,state=state,save=save,ROOT=Path(directory),json=json,flush=lambda p:None)
   with self.assertRaises(OSError):exec(code,scope)
   result=json.loads((Path(directory)/'result.json').read_text());self.assertEqual(result['state'],'requires-recovery');self.assertIn('timer restore denied',result['timerRestoreFailure'])

 def test_timer_restore_failure_is_not_a_false_pass(self):
  x=Fixture();f=x.scope();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot)
  def fail(*a):raise OSError('start timer failed')
  f['run']=fail
  with self.assertRaises(OSError):f['restore_backup_timer'](snapshot)
  self.assertEqual(x.active,'inactive')

 def test_pre_pause_holder_allowed_exact_units_and_subgroups(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);db=root/'db';db.write_text('synthetic');proc=root/'proc';proc.mkdir()
   for i,unit in enumerate(['commonplace','commonplace-files','commonplace-runtime'],200):
    item=proc/str(i);(item/'fd').mkdir(parents=True);os.link(db,item/'fd/9');(item/'cgroup').write_text('0::/system.slice/'+unit+'.service'+('/child' if i==202 else '')+'\n')
   path=lambda value:proc if str(value)=='/proc' else Path(value)
   f=extract('expected_holders_only',Path=path,output=lambda *a:'/system.slice/'+a[2]+'.service')
   holders=f['expected_holders_only']([db]);self.assertEqual({x['unit'] for x in holders},{'commonplace.service','commonplace-files.service','commonplace-runtime.service'})
   for value in ['/system.slice/commonplace-backup.service','/system.slice/commonplace.service-unrelated','/foreign/commonplace.service']:
    (proc/'200/cgroup').write_text('0::'+value+'\n')
    with self.subTest(value=value),self.assertRaisesRegex(AssertionError,'pre-pause database holder'):f['expected_holders_only']([db])

 def test_holder_permission_error_and_unexpected_controlgroup_fail_closed(self):
  with tempfile.TemporaryDirectory() as directory:
   db=Path(directory)/'db';db.write_text('synthetic')
   class Denied:
    name='222'
    def __truediv__(self,x):return self
    def iterdir(self):raise PermissionError('no proc inspection')
   class Proc:
    def iterdir(self):return iter([Denied()])
   f=extract('expected_holders_only',Path=lambda p:Proc(),output=lambda *a:'/system.slice/'+a[2]+'.service')
   with self.assertRaises(PermissionError):f['expected_holders_only']([db])
   f['output']=lambda *a:'/'
   with self.assertRaisesRegex(AssertionError,'cgroup layout'):f['expected_holders_only']([db])

 def test_unit_property_parser_rejects_incomplete_metadata(self):
  f=extract('unit_properties',output=lambda *a:'ActiveState=active')
  self.assertEqual(f['unit_properties'](TIMER,['ActiveState']),{'ActiveState':'active'})
  with self.assertRaisesRegex(AssertionError,'Incomplete'):f['unit_properties'](TIMER,['ActiveState','SubState'])

 def test_exact_r4_predecessor_and_pre_pause_order(self):
  code=HELPER.read_text();self.assertIn("PREVIOUS=Path('/var/tmp/commonplace-storage-20261101-r4')",code);self.assertIn('3aab196a49f859a0716b7c99a28fe72b0d0f4a7a3f9a81ed07e6b249a00f0eb3',code)
  body=next(n for n in TREE.body if isinstance(n,ast.Try));body=ast.unparse(ast.Module(body=body.body,type_ignores=[]))
  self.assertLess(body.index('pause_backup_timer(timerSnapshot)'),body.index('wait_backup_idle(timerSnapshot)'))
  self.assertLess(body.index('wait_backup_idle(timerSnapshot)'),body.index('expected_holders_only(dbfiles(OLD))'))
  self.assertLess(body.index('expected_holders_only(dbfiles(OLD))'),body.index("run('systemctl', 'stop', *services)"))
  self.assertNotIn("run('systemctl', 'stop', BACKUP_SERVICE)",code)

if __name__=='__main__':unittest.main(verbosity=2)

