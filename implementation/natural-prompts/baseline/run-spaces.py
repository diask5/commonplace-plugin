from pathlib import Path
import os,json,subprocess,time,re,hashlib,urllib.request,base64
h=Path.home();root=Path(os.environ.get('MEET_PROXY_BENCHMARK_DIR',h/'.commonplace-code-verification/natural-prompts-0.4.24'));os.umask(0o077)
assert not (root/'fixture/state.sqlite').exists(),'Use a new directory; existing fixture state must not be reused'
bundle=urllib.request.urlopen('https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-v0.4.24/runtime-update.json',timeout=60).read()
assert hashlib.sha256(bundle).hexdigest()=='b0d3308ebb59df1ad0e4b3a4008b4b318de329378fdb2c0dc899ab6a2102e6da'
for name,data in json.loads(bundle).items():
 dest=root/'fixture'/name
 assert '..' not in Path(name).parts and not Path(name).is_absolute()
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(base64.b64decode(data))
node=h/'Library/Application Support/Meet Proxy/plugins/0.4.24/runtime/node'
env=os.environ.copy()
for k in list(env):
 if k.startswith(('CLAUDE_','CONDUCTOR_','CODEX_')) or k in ['PERPLEXITY_API_KEY']:del env[k]
with (root/'space-server.log').open('w') as log:
 server=subprocess.Popen([str(node),str(root/'space-server.mjs')],env=env,cwd=root,stdin=subprocess.PIPE,stdout=log,stderr=log)
 try:
  for _ in range(100):
   if (root/'space-ready.json').exists():break
   if server.poll() is not None:raise RuntimeError('Fixture did not start; see space-server.log')
   time.sleep(.2)
  plan=json.loads((root/'space-plan.private.json').read_text());env['BENCH_ENDPOINT']=plan['endpoint'];env['BENCH_BEARER']=plan['token']
  config=h/'.codex/config.toml';before=hashlib.sha256(config.read_bytes()).hexdigest()
  names=re.findall(r'^\[mcp_servers\.([^].]+)\]',config.read_text(),re.M);overrides=[]
  for n in names:overrides+=['-c',f'mcp_servers.{n}.enabled=false']
  overrides+=['-c','mcp_servers.spec.command="python3"','-c','mcp_servers.spec.args='+json.dumps([str(root/'space-bridge.py')]),'-c','mcp_servers.spec.env_vars=["BENCH_ENDPOINT","BENCH_BEARER"]']
  results=[]
  for case in plan['cases']:
   server.stdin.write((json.dumps({'case':case['id']})+'\n').encode());server.stdin.flush();d=root/'space-evidence'/case['id'];d.mkdir(parents=True,exist_ok=True);work=root/'space-work'/case['id'];work.mkdir(parents=True,exist_ok=True)
   args=[str(h/'Library/Application Support/com.conductor.app/bin/codex'),'exec','--skip-git-repo-check','--sandbox','read-only','--json',*overrides,'--output-last-message',str(d/'final.txt'),case['prompt']];start=time.time()
   with (d/'stream.jsonl').open('w') as out,(d/'stderr.log').open('w') as err:
    try:r=subprocess.run(args,env=env,cwd=work,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=180);code=r.returncode
    except subprocess.TimeoutExpired:code=124
   events=[]
   for l in (d/'stream.jsonl').read_text().splitlines():
    try:events.append(json.loads(l))
    except:pass
   calls=[x['item'] for x in events if x.get('type')=='item.completed' and x.get('item',{}).get('type')=='mcp_tool_call']
   result={**case,'exitCode':code,'elapsedSeconds':round(time.time()-start,2),'final':(d/'final.txt').read_text() if (d/'final.txt').exists() else '', 'calls':calls,'configUnchanged':before==hashlib.sha256(config.read_bytes()).hexdigest(),'evidenceSha256':hashlib.sha256((d/'stream.jsonl').read_bytes()).hexdigest()};(d/'result.json').write_text(json.dumps(result,indent=2));results.append(result)
   print(json.dumps({'case':case['id'],'exitCode':code,'tools':[c.get('tool') for c in calls],'elapsedSeconds':result['elapsedSeconds']}),flush=True)
   if any('requires approval' in json.dumps(c.get('error',{})).lower() for c in calls):break
  server.stdin.write(b'{"snapshot":true}\n');server.stdin.flush();time.sleep(1)
  (root/'space-results.private.json').write_text(json.dumps(results,indent=2))
 finally:server.terminate();server.wait(timeout=15)
