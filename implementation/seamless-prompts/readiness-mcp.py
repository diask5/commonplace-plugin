"""Observe synthetic seed visibility through the installed, owner-authorized MCP.

Uses only the benchmark's already-approved search/read tools, no model, fake
native identity, setup actions or permission changes. Private receipts stay local.
"""
from pathlib import Path
import json,os,subprocess,threading,queue,time,sys
h=Path.home();root=Path(os.environ['MEET_PROXY_BENCHMARK_DIR'])
os.umask(0o077)
plan=json.loads((root/'plan.json').read_text());projects=[c['project'] for c in plan['cases']]
version=plan.get('nativeVersion','0.4.26');revision=plan.get('runtimeRevision',59)
assert version in {'0.4.26','0.4.27'} and revision in {59,60}
plugin=h/'Library/Application Support/Meet Proxy/plugins'/version
seeds={key:json.loads((root/'evidence'/key/'result.json').read_text()) for key in ['seed-plan','seed-update']}
assert all(v['exitCode']==0 and not v['calls'] and not v['stoppedReason'] for v in seeds.values()),'Seed generation did not complete cleanly'
assert json.loads((h/'.commonplace/runtime.json').read_text())['revision']==revision
account=json.loads((h/'.commonplace/account-client.json').read_text())['session']
assert (account.get('humanAccount') or account.get('account'))['email']=='diaskyle10@gmail.com'
env=os.environ.copy()
for key in list(env):
 if key.startswith(('CLAUDE_','CONDUCTOR_','CODEX_')):del env[key]
if env.get('COMMONPLACE_DATA_DIR'):assert Path(env['COMMONPLACE_DATA_DIR']).resolve()==(h/'.commonplace').resolve()
assert not any('WORKSPACE' in k and k.startswith('COMMONPLACE_') and v for k,v in env.items()),'Keep any existing workspace scope intact'
started=time.monotonic();replies=queue.Queue();seq=0
with (root/'readiness-mcp.stderr.log').open('w') as err,(root/'readiness-receipts.private.jsonl').open('w') as evidence:
 p=subprocess.Popen([str(plugin/'runtime/node'),str(plugin/'server/plugin.mjs')],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,env=env,text=True,bufsize=1,cwd=root)
 def receive():
  for line in p.stdout:
   try:replies.put(json.loads(line))
   except ValueError:pass
  replies.put(None)
 threading.Thread(target=receive,daemon=True).start()
 def rpc(method,params):
  global seq
  seq+=1;ident=seq;t=time.monotonic();p.stdin.write(json.dumps({'jsonrpc':'2.0','id':ident,'method':method,'params':params})+'\n');p.stdin.flush()
  while True:
   reply=replies.get(timeout=max(0.1,60-(time.monotonic()-t)))
   if reply is None:raise RuntimeError('Installed MCP exited')
   if reply.get('id')!=ident:continue
   evidence.write(json.dumps({'method':method,'params':params,'seconds':round(time.monotonic()-t,3),'reply':reply})+'\n');evidence.flush()
   if reply.get('error'):raise RuntimeError('MCP protocol error')
   return reply['result']
 def call(name,args):
  assert name in {'search_shared_context','read_shared_context'}
  result=rpc('tools/call',{'name':name,'arguments':args})
  if result.get('isError'):raise RuntimeError('Readiness tool returned an error; inspect private receipt before any retry')
  return json.loads(next(b['text'] for b in result['content'] if b['type']=='text'))
 result={'ready':False}
 try:
  rpc('initialize',{'protocolVersion':'2025-03-26','capabilities':{},'clientInfo':{'name':'Owner read-only benchmark readiness','version':'1'}})
  p.stdin.write(json.dumps({'jsonrpc':'2.0','method':'notifications/initialized'})+'\n');p.stdin.flush()
  while time.monotonic()-started<360:
   search=call('search_shared_context',{'query':projects[0]});found=[]
   for key,seed in seeds.items():
    rows=[r for r in search.get('results',[]) if seed['session'] in json.dumps(r)]
    if not rows:continue
    row=rows[0];args={'documentId':row['documentId'],'offset':0,'limit':16000}
    if isinstance(search.get('revision'),int):args['revision']=search['revision']
    read=call('read_shared_context',args)
    if read.get('changed'):continue
    body=json.dumps(read)
    marker='Planning note, 2026-10-20' if key=='seed-plan' else 'Decision update, 2026-10-25'
    if marker in body and all(project in body for project in projects):found.append(key)
   result={'ready':len(found)==2,'seedsVisible':found,'runtimeRevision':revision,'waitSeconds':round(time.monotonic()-started,2),'method':'real installed MCP search and supporting source reads; optional mirror not required'}
   (root/'ingestion-ready.json').write_text(json.dumps(result,indent=2)+'\n')
   if result['ready']:break
   time.sleep(15)
 except Exception as e:result={'ready':False,'error':str(e),'waitSeconds':round(time.monotonic()-started,2)}
 finally:
  try:p.stdin.close();p.wait(timeout=10)
  except subprocess.TimeoutExpired:p.terminate();p.wait(timeout=10)
  (root/'ingestion-ready.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
 if not result['ready']:sys.exit(1)
