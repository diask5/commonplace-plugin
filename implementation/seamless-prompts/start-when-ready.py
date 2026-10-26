from pathlib import Path
import time,json,subprocess,os,sys
h=Path.home();root=Path(os.environ.get('MEET_PROXY_BENCHMARK_DIR',h/'.commonplace-code-verification/seamless-prompts-0.4.25'));start=time.time();observations=[]
plan=json.loads((root/'plan.json').read_text())
projects=[case['project'] for case in plan['cases']]
while time.time()-start<600:
 items=[]
 try:
  ctx=h/'.commonplace/context/current';status=json.loads((h/'.commonplace/context-mirror.json').read_text())
  for f in (ctx/'documents').rglob('*.txt'):
   text=f.read_text()
   if all(project in text for project in projects) and ('Planning note, 2026-10-20' in text or 'Decision update, 2026-10-25' in text):items.append({'id':str(f.relative_to(ctx)),'planning':'Planning note, 2026-10-20' in text,'update':'Decision update, 2026-10-25' in text,'characters':len(text)})
  runtime=json.loads((h/'.commonplace/runtime.json').read_text())
  result={'checkedAt':time.time(),'documents':items,'revision':status.get('revision'),'lastSyncedAt':status.get('lastSyncedAt'),'runtimeRevision':runtime.get('revision')};observations.append(result)
  (root/'ingestion-observations.json').write_text(json.dumps(observations,indent=2))
  if runtime.get('revision',0)>=58 and any(x['planning'] for x in items) and any(x['update'] for x in items):
   (root/'ingestion-ready.json').write_text(json.dumps(result,indent=2));print(json.dumps({'ready':True,'documents':len(items),'waitSeconds':time.time()-start}),flush=True)
   if '--start-score' in sys.argv:
    with (root/'score-run.log').open('w') as out:subprocess.run(['python3',str(root/'runner.py'),'score'],stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT)
   break
 except Exception as e:print(type(e).__name__,flush=True)
 time.sleep(5)
else:print(json.dumps({'ready':False,'timedOut':True,'waitSeconds':600}),flush=True)
