"""Process-only isolation and guards for the seamless-prompt harnesses.

Nothing here edits saved Codex/Claude configuration or weakens an approval. It
only builds per-process `-c` overrides, checks them without a model, and
evaluates the JSON event stream while a run is in flight.
"""
import json,re,subprocess,threading,time

FIXTURE_SERVER='spec'
SKIP_CASES={'space-private':'Provider safety rejection previously recorded; not retried or rephrased.',
 'space-accept':'Browser approval was previously denied; not retried or rephrased.'}
# Feature names that expose connectors, browsers or computer use. Matched against
# the *live* `codex features list`, so names this file does not know are still caught.
RISKY_FEATURE=re.compile(r'(^|_)(apps|connectors?|computer|cua|browser|chrome|desktop|plugins?|shell_tool|multi_agent|image_generation)(_|$)',re.I)
DENIAL=re.compile(r'requires? approval|approval (was )?(denied|rejected|declined|required)|denied|declined|rejected by user|user (cancel|reject|declin)|not approved|permission',re.I)
# Commands that reach outside the disposable working directory (UI, browser, network).
EXTERNAL_COMMAND=re.compile(r'(^|[\s/;&|(])(open|osascript|screencapture|cliclick|chrome|google-chrome|safari|firefox|curl|wget|gh|cua)(\s|$)|computer[-_ ]use|--remote-debugging|\bbrowser\b',re.I)

class IsolationError(RuntimeError):pass

def toml_names(text):
 return list(dict.fromkeys(re.findall(r'^\[mcp_servers\.([^].]+)[.\]]',text,re.M)))

def process_overrides(server_names,extra_features=()):
 """Disable apps and every saved MCP server for this process only.
 The fixture server is configured separately and is not in this list."""
 o=['-c','features.apps=false','-c','features.shell_tool=false',
    '-c','features.multi_agent=false','-c','features.image_generation=false',
    '-c','web_search="disabled"']
 for f in extra_features:o+=['-c',f'features.{f}=false']
 for n in server_names:
  if n!=FIXTURE_SERVER:o+=['-c',f'mcp_servers.{n}.enabled=false']
 return o

def parse_features(text):
 """Parse `codex features list` rows: `name  stage  true|false` (JSON also accepted)."""
 try:
  data=json.loads(text)
  if isinstance(data,dict):return {str(k):bool(v if not isinstance(v,dict) else v.get('enabled')) for k,v in data.items()}
  return {str(x['name']):bool(x.get('enabled')) for x in data}
 except (ValueError,KeyError,TypeError):pass
 out={}
 for line in text.splitlines():
  m=re.match(r'^\s*([A-Za-z0-9_.-]+)\s+.*?\b(true|false)\s*$',line)
  if m:out[m.group(1)]=m.group(2)=='true'
 return out

def parse_mcp_list(text):
 """Return {name: enabled}. Accepts JSON list/dict from `codex mcp list --json`."""
 data=json.loads(text)
 if isinstance(data,dict):data=data.get('servers',data)
 if isinstance(data,dict):data=[{'name':k,**(v if isinstance(v,dict) else {})} for k,v in data.items()]
 return {x['name']:bool(x.get('enabled',True)) for x in data}

def preflight(codex,base_overrides,allowed_servers,env,cwd,timeout=60,run=subprocess.run):
 """No-model checks of the effective configuration. Returns final overrides.
 Fails closed (IsolationError) if a check cannot be performed or does not hold."""
 def cli(args):
  try:r=run([codex,*base_overrides,*args],env=env,cwd=cwd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
  except (OSError,subprocess.SubprocessError) as e:raise IsolationError(f'preflight command failed: {args}: {type(e).__name__}')
  if r.returncode!=0:raise IsolationError(f'preflight command {args} exited {r.returncode}; cannot verify isolation')
  return r.stdout
 feats=parse_features(cli(['features','list']))
 if not feats:raise IsolationError('could not read effective feature flags; cannot verify apps/computer-use are off')
 if feats.get('apps') is not False:raise IsolationError('features.apps is not effectively false')
 extra=sorted(n for n,on in feats.items() if on and RISKY_FEATURE.search(n))
 final=list(base_overrides)
 for n in extra:final+=['-c',f'features.{n}=false']
 if extra:
  feats=parse_features(cli_with(run,codex,final,['features','list'],env,cwd,timeout))
  still=sorted(n for n,on in feats.items() if on and RISKY_FEATURE.search(n))
  if still:raise IsolationError(f'features still enabled after override: {still}')
 try:servers=parse_mcp_list(cli_with(run,codex,final,['mcp','list','--json'],env,cwd,timeout))
 except (ValueError,KeyError,TypeError):raise IsolationError('could not parse effective MCP server list')
 bad=sorted(n for n,on in servers.items() if on and n not in allowed_servers)
 if bad:raise IsolationError(f'unexpected MCP servers enabled: {bad}')
 if not all(s in servers and servers[s] for s in allowed_servers):raise IsolationError('fixture server is not effectively enabled')
 return final

def cli_with(run,codex,overrides,args,env,cwd,timeout):
 try:r=run([codex,*overrides,*args],env=env,cwd=cwd,capture_output=True,text=True,timeout=timeout,stdin=subprocess.DEVNULL)
 except (OSError,subprocess.SubprocessError) as e:raise IsolationError(f'preflight command failed: {args}: {type(e).__name__}')
 if r.returncode!=0:raise IsolationError(f'preflight command {args} exited {r.returncode}')
 return r.stdout

def violation(event,allowed_servers=(FIXTURE_SERVER,),allowed_tools=None,strict_commands=True):
 """Return a reason string if a Codex JSON event is an unexpected external tool or
 a denied approval; otherwise None. Looks at started and completed items."""
 if not isinstance(event,dict):return None
 t=str(event.get('type',''))
 item=event.get('item') if isinstance(event.get('item'),dict) else {}
 it=str(item.get('type',''))
 if 'approval' in t.lower() and ('den' in t.lower() or 'reject' in t.lower()):return f'approval denied event: {t}'
 if it=='mcp_tool_call':
  s,tool=item.get('server'),item.get('tool')
  if s not in allowed_servers:return f'unexpected MCP server {s!r} tool {tool!r}'
  if allowed_tools is not None and tool not in allowed_tools:return f'unexpected tool {tool!r} on {s!r}'
  if DENIAL.search(json.dumps(item.get('error') or '')):return f'denied approval on {s}.{tool}'
 elif it=='command_execution':
  cmd=str(item.get('command',''))
  if strict_commands:return f'command outside MCP-only benchmark: {cmd[:120]}'
  if EXTERNAL_COMMAND.search(cmd):return f'external-looking command: {cmd[:120]}'
  if item.get('status')=='declined' or (item.get('exit_code') not in (None,0,'0') and DENIAL.search(str(item.get('aggregated_output','')))):return f'command denied: {cmd[:120]}'
 elif it in {'web_search','collab_tool_call','computer_use','browser','app_tool_call','connector_tool_call'} or re.search(r'browser|computer|connector|app_',it):
  return f'unexpected item type {it!r}'
 elif it=='error' and DENIAL.search(str(item.get('message',''))):return 'denied approval reported as error item'
 return None

def claude_violation(event,allowed):
 """Claude stream-json: any tool_use outside the allowlist, or permission denials."""
 if not isinstance(event,dict):return None
 if event.get('type')=='result' and event.get('permission_denials'):return 'permission denied'
 msg=event.get('message')
 for b in (msg.get('content') if isinstance(msg,dict) and isinstance(msg.get('content'),list) else []):
  if isinstance(b,dict) and b.get('type')=='tool_use' and b.get('name') not in allowed:return f"unexpected tool {b.get('name')!r}"
 return None

def guarded_run(args,env,cwd,stream_path,err_path,check,timeout,popen=subprocess.Popen,now=time.time):
 """Run a process, write the stream, and terminate on the first violation.
 Returns (exit_code, stop_reason). 124 = timeout, 125 = stopped by guard."""
 reason=None
 with open(stream_path,'w') as out,open(err_path,'w') as err:
  p=popen(args,cwd=cwd,env=env,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=err,text=True)
  timed=[];timer=threading.Timer(timeout,lambda:(timed.append(1),p.terminate()));timer.daemon=True;timer.start()
  try:
   for line in p.stdout:
    out.write(line);out.flush()
    try:ev=json.loads(line)
    except ValueError:ev=None
    reason=check(ev)
    if reason:p.terminate();break
  finally:
   timer.cancel()
   try:code=p.wait(timeout=15)
   except subprocess.TimeoutExpired:p.kill();code=p.wait()
 if timed and not reason:return 124,'timeout'
 return (125,reason) if reason else (code,None)
