"""Read-only extracted regressions for the one historical backup timeout."""
import copy,importlib.util,inspect,os,tempfile,unittest
from pathlib import Path
path=Path(__file__).with_name('storage69-r5-scheduler-checks.py')
spec=importlib.util.spec_from_file_location('scheduler_checks',path);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
HISTORY={'ActiveState':'failed','SubState':'failed','MainPID':'0','Result':'timeout','ExecMainStatus':'15','InvocationID':'b87cb0f36fe4490db77a36c6aff71f13','ExecMainStartTimestampMonotonic':'3827523228312','ExecMainExitTimestampMonotonic':'3827823218295','ExecMainStartTimestamp':'Sun 2026-11-01 04:03:23 UTC','ExecMainExitTimestamp':'Sun 2026-11-01 04:08:23 UTC','ExecMainPID':'883648','ExecMainCode':'2'}
def wait(f,snapshot):
 return f['wait_backup_idle'](snapshot) if inspect.signature(f['wait_backup_idle']).parameters else f['wait_backup_idle']()
class HistoricalTimeoutChecks(unittest.TestCase):
 def fixture(self,live=None):
  x=base.Fixture();x.live=copy.deepcopy(HISTORY if live is None else live);return x,x.scope()
 def test_unchanged_historical_timeout_captured_and_allowed_without_relabel(self):
  x,f=self.fixture();snapshot=f['backup_schedule_snapshot']()
  self.assertEqual(snapshot.get('preexistingTimeout'),HISTORY)
  f['pause_backup_timer'](snapshot);wait(f,snapshot);f['assert_backup_paused'](snapshot)
  self.assertEqual(snapshot['preexistingTimeout']['Result'],'timeout');self.assertEqual(x.live,HISTORY)
  f['restore_backup_timer'](snapshot);self.assertEqual(x.calls,[('systemctl','stop',base.TIMER),('systemctl','start',base.TIMER)])
 def test_initially_running_then_identical_timeout_fails_closed(self):
  x,f=self.fixture(dict(HISTORY,ActiveState='activating',SubState='start',MainPID='1234',Result='success',ExecMainStatus='0'))
  snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);x.live=copy.deepcopy(HISTORY)
  with self.assertRaises(AssertionError):wait(f,snapshot)
  f['restore_backup_timer'](snapshot);self.assertEqual(x.active,'active')
 def test_changed_invocation_start_or_exit_is_never_the_historical_exception(self):
  for key,value in [('InvocationID','b'*32),('ExecMainStartTimestampMonotonic','2000000'),('ExecMainExitTimestampMonotonic','302000000'),('ExecMainExitTimestamp','Sun 2026-11-01 04:09:23 UTC')]:
   with self.subTest(key=key):
    x,f=self.fixture();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);wait(f,snapshot)
    x.live[key]=value
    with self.assertRaises(AssertionError):wait(f,snapshot)
    with self.assertRaises(AssertionError):f['assert_backup_paused'](snapshot)
 def test_nonzero_pid_other_result_status_substate_or_date_not_allowed(self):
  for key,value in [('MainPID','123'),('Result','exit-code'),('ExecMainStatus','9'),('SubState','start'),('ExecMainExitTimestamp','Mon 2026-11-02 04:08:23 UTC'),('ExecMainStartTimestampMonotonic','0')]:
   with self.subTest(key=key):
    x,f=self.fixture(dict(HISTORY,**{key:value}))
    with self.assertRaises(AssertionError):
     snapshot=f['backup_schedule_snapshot']();wait(f,snapshot)
 def test_running_again_after_historical_failure_blocks_final_gate(self):
  x,f=self.fixture();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);wait(f,snapshot)
  x.live=dict(HISTORY,ActiveState='activating',SubState='start',MainPID='55',Result='success')
  with self.assertRaises(AssertionError):f['assert_backup_paused'](snapshot)
 def test_historical_exception_does_not_bypass_unknown_inode_holder(self):
  x,f=self.fixture();snapshot=f['backup_schedule_snapshot']();f['pause_backup_timer'](snapshot);wait(f,snapshot)
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);db=root/'db';db.write_text('synthetic');proc=root/'proc';fd=proc/'222/fd';fd.mkdir(parents=True);os.link(db,fd/'8');(fd.parent/'cgroup').write_text('0::/system.slice/commonplace-backup.service\n')
   functions=base.extract('expected_holders_only',Path=lambda p:proc if str(p)=='/proc' else Path(p),output=lambda *a:'/system.slice/'+a[2]+'.service')
   with self.assertRaisesRegex(AssertionError,'pre-pause database holder'):functions['expected_holders_only']([db])
 def test_historical_failure_evidence_and_fresh_migration_backup_remain_required(self):
  source=base.HELPER.read_text()
  self.assertTrue("state['preexistingBackupFailure']" in source,'Historical failure must remain in result evidence')
  self.assertIn('copy(OLD,BACKUP/OLD.name)',source);self.assertIn('schema_as_user(staged,user,quick=True)==migrations',source);self.assertIn('digest(staged)==sourceHash',source)
  for forbidden in ['reset-failed',"run('systemctl','stop',BACKUP_SERVICE)","run('kill'","run('systemctl','kill'","run('systemctl','start',BACKUP_SERVICE)"]:self.assertNotIn(forbidden,source)

 def test_timeout_evidence_durably_saved_before_timer_pause(self):
  import ast,json
  x,f=self.fixture();snapshot=f['backup_schedule_snapshot']()
  outer=next(n for n in base.TREE.body if isinstance(n,ast.Try))
  start=next(i for i,n in enumerate(outer.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='timerSnapshot' for t in n.targets))
  end=next(i for i,n in enumerate(outer.body) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mainPid' for t in n.targets))
  code=compile(ast.Module(body=outer.body[start:end],type_ignores=[]),str(base.HELPER),'exec')
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);state={};scope=base.extract('save','flush',ROOT=root,state=state)
   def pause(s):
    evidence=json.loads((root/'status.json').read_text())
    self.assertEqual(evidence['preexistingBackupFailure'],HISTORY);self.assertEqual(evidence['backupScheduleBefore']['preexistingTimeout'],HISTORY)
    f['pause_backup_timer'](s)
   scope.update(backup_schedule_snapshot=lambda:snapshot,pause_backup_timer=pause,wait_backup_idle=lambda s:wait(f,s))
   exec(code,scope)
   self.assertEqual(x.calls,[('systemctl','stop',base.TIMER)]);self.assertEqual(state['preexistingBackupFailure']['Result'],'timeout')

if __name__=='__main__':unittest.main(verbosity=2)

