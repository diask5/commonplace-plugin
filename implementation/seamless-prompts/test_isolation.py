"""Focused, model-free tests for the benchmark isolation harness.
Run: python3 -I -m unittest implementation/seamless-prompts/test_isolation.py
(from the repo root, or `python3 test_isolation.py` inside this directory)."""
import json,subprocess,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import isolation as iso

def fake_run(features,servers,fail=None):
 calls=[]
 def run(cmd,**kw):
  calls.append(cmd);rest=[c for c in cmd if not c.startswith(('features.','mcp_servers.')) and c!='-c']
  if fail and fail in rest:return subprocess.CompletedProcess(cmd,1,'','')
  if 'features' in rest:
   if not features:return subprocess.CompletedProcess(cmd,0,'','')
   on=dict(features)
   for i,c in enumerate(cmd):
    if c.startswith('features.') and c.endswith('=false'):on[c[9:-6]]=False
   return subprocess.CompletedProcess(cmd,0,'\n'.join(f'{k}  stable  {str(v).lower()}' for k,v in on.items()),'')
  on=dict(servers)
  for c in cmd:
   if c.startswith('mcp_servers.') and c.endswith('.enabled=false'):on[c[12:-14]]=False
  return subprocess.CompletedProcess(cmd,0,json.dumps([{'name':k,'enabled':v} for k,v in on.items()]),'')
 return run,calls

class Construction(unittest.TestCase):
 def test_overrides_disable_apps_and_saved_servers_but_not_fixture(self):
  o=iso.process_overrides(['gmail','spec','figma'])
  self.assertIn('features.apps=false',o);self.assertIn('mcp_servers.gmail.enabled=false',o)
  self.assertNotIn('mcp_servers.spec.enabled=false',o)
  self.assertFalse([x for x in o if 'approval' in x],'must never touch approvals')
 def test_toml_names(self):
  self.assertEqual(iso.toml_names('[mcp_servers.a]\nx=1\n[mcp_servers.b.env]\n'),['a','b'])
 def test_preflight_passes_and_disables_extra_risky_features(self):
  run,_=fake_run({'apps':True,'computer_use':True,'shell_tool':True},{'spec':True,'gmail':True})
  o=iso.preflight('codex',iso.process_overrides(['gmail','spec']),{'spec'},{},'.',run=run)
  self.assertIn('features.computer_use=false',o);self.assertIn('features.shell_tool=false',o)
 def test_preflight_fails_closed(self):
  base=iso.process_overrides([])
  run,_=fake_run({'apps':True},{'spec':True},fail='features')
  with self.assertRaises(iso.IsolationError):iso.preflight('codex',base,{'spec'},{},'.',run=run)
  run,_=fake_run({},{'spec':True})   # unreadable feature list
  with self.assertRaises(iso.IsolationError):iso.preflight('codex',base,{'spec'},{},'.',run=run)
  run,_=fake_run({'apps':True},{'spec':True,'rogue':True})   # server not disabled by overrides
  with self.assertRaises(iso.IsolationError):iso.preflight('codex',base,{'spec'},{},'.',run=run)
  run,_=fake_run({'apps':True},{'rogue':True})   # fixture missing
  with self.assertRaises(iso.IsolationError):iso.preflight('codex',base,{'spec'},{},'.',run=run)

def item(**k):return {'type':'item.completed','item':k}
class Violations(unittest.TestCase):
 def test_allowed_fixture_call(self):
  self.assertIsNone(iso.violation(item(type='mcp_tool_call',server='spec',tool='request_space_context')))
 def test_unexpected_server_and_item_types(self):
  self.assertIn('unexpected MCP',iso.violation(item(type='mcp_tool_call',server='codex_apps',tool='x')))
  self.assertTrue(iso.violation(item(type='computer_use')))
  self.assertTrue(iso.violation(item(type='web_search')))
 def test_denied_approval(self):
  self.assertTrue(iso.violation(item(type='mcp_tool_call',server='spec',tool='t',error={'message':'tool requires approval'})))
 def test_commands(self):
  self.assertTrue(iso.violation(item(type='command_execution',command='open -a Safari https://x')))
  self.assertTrue(iso.violation(item(type='command_execution',command='curl https://x')))
  self.assertTrue(iso.violation(item(type='command_execution',command='ls',status='completed',exit_code=0)))
 def test_claude(self):
  ev={'message':{'content':[{'type':'tool_use','name':'mcp__other__x'}]}}
  self.assertTrue(iso.claude_violation(ev,['mcp__ok']));self.assertIsNone(iso.claude_violation(ev,['mcp__other__x']))
  self.assertTrue(iso.claude_violation({'type':'result','permission_denials':[1]},[]))

class Stop(unittest.TestCase):
 def test_guard_terminates_on_first_violation(self):
  bad=json.dumps(item(type='mcp_tool_call',server='apps',tool='x'));later=json.dumps(item(type='mcp_tool_call',server='spec',tool='y'))
  script=f'import sys,time\nprint({bad!r},flush=True)\ntime.sleep(30)\nprint({later!r})'
  with tempfile.TemporaryDirectory() as d:
   code,why=iso.guarded_run([sys.executable,'-I','-c',script],None,d,Path(d)/'s',Path(d)/'e',iso.violation,20)
   self.assertEqual(code,125);self.assertIn('unexpected MCP',why)
   self.assertNotIn('"y"',(Path(d)/'s').read_text())
 def test_clean_run_and_timeout(self):
  with tempfile.TemporaryDirectory() as d:
   ok=json.dumps(item(type='mcp_tool_call',server='spec',tool='t'))
   self.assertEqual(iso.guarded_run([sys.executable,'-I','-c',f'print({ok!r})'],None,d,Path(d)/'s',Path(d)/'e',iso.violation,20),(0,None))
   self.assertEqual(iso.guarded_run([sys.executable,'-I','-c','import time;time.sleep(30)'],None,d,Path(d)/'s',Path(d)/'e',iso.violation,1),(124,'timeout'))

class Skips(unittest.TestCase):
 def test_previously_denied_cases_skipped_and_prompts_unchanged(self):
  self.assertEqual(set(iso.SKIP_CASES),{'space-private','space-accept'})
  src=(Path(__file__).parent/'run-spaces.py').read_text()
  self.assertIn('iso.SKIP_CASES',src);self.assertIn('iso.preflight',src)
  self.assertLess(src.index('iso.preflight'),src.index("'exec'"),'preflight must precede model execution')
  r=(Path(__file__).parent/'runner.py').read_text();self.assertIn('codex_overrides()',r)
  self.assertNotIn('approval_mode="never"',src+r)
 def test_runners_do_not_add_hints_to_prompts(self):
  plan=json.loads((Path(__file__).parent/'plan.json').read_text())
  for c in plan['cases']:self.assertNotRegex(c['prompt'],r'(?i)\b(mcp|tool|search_shared|read_shared)\b')
if __name__=='__main__':unittest.main()
