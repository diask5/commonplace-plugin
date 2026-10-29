from pathlib import Path
import json,hashlib,re,time,os
h=Path.home();r=Path(os.environ.get('MEET_PROXY_BENCHMARK_DIR',h/'.commonplace-code-verification/natural-prompts-0.4.24'));plan=json.loads((r/'plan.json').read_text());results=[]
for case in plan['cases']:
 d=r/'evidence'/case['id'];p=d/'stream.jsonl'
 if not p.exists():results.append({'id':case['id'],'state':'not_run'});continue
 events=[]
 for line in p.read_text().splitlines():
  try:events.append(json.loads(line))
  except:pass
 tools=[];reads=[];errors=[];denials=[];final='';model=None;completed=False
 if case['host']=='claude':
  for e in events:
   if e.get('type')=='system' and e.get('subtype')=='init':model=e.get('model')
   m=e.get('message');blocks=m.get('content',[]) if isinstance(m,dict) else []
   if not isinstance(blocks,list):continue
   for b in blocks:
    if not isinstance(b,dict):continue
    if b.get('type')=='tool_use':tools.append({'name':b.get('name'),'arguments':b.get('input')})
    if b.get('type')=='tool_result' and b.get('is_error'):errors.append({'tool_use_id':b.get('tool_use_id'),'error':str(b.get('content'))[:1000]})
  f=next((e for e in reversed(events) if e.get('type')=='result'),{})
  final=f.get('result','');denials=f.get('permission_denials',[]);completed=bool(f)
 else:
  for e in events:
   item=e.get('item',{})
   if e.get('type')=='turn.completed':completed=True
   if e.get('type')=='item.completed' and item.get('type')=='mcp_tool_call':
    tools.append({'name':item.get('tool'),'status':item.get('status'),'arguments':item.get('arguments')})
    if item.get('error'):errors.append({'tool':item.get('tool'),'error':item.get('error')})
   if e.get('type')=='item.completed' and item.get('type')=='command_execution':
    cmd=item.get('command','');out=item.get('aggregated_output','');reads.append({'command':cmd,'exitCode':item.get('exit_code'),'outputBytes':len(out),'containsProject':case['project'] in out,'containsLatestDate':case['date'] in out,'containsOwner':case['owner'] in out,'containsReason':case['reason'] in out,'containsUndecided':bool(re.search(r'not been (chosen|decided)|remain undecided',out))})
  final=(d/'final.txt').read_text() if (d/'final.txt').exists() else ''
 result={'id':case['id'],'host':case['host'],'prompt':case['prompt'],'state':'completed' if completed else 'in_progress','model':model,'tools':tools,'fileReads':reads,'toolErrors':errors,'permissionDenials':denials,'final':final,'evidenceSha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 if (d/'result.json').exists():result.update({k:v for k,v in json.loads((d/'result.json').read_text()).items() if k in ['elapsedSeconds','exitCode','configUnchanged']})
 results.append(result)
report={'collectedAt':time.time(),'cases':results,'ingestion':json.loads((r/'ingestion-ready.json').read_text()) if (r/'ingestion-ready.json').exists() else None}
(r/'retrieval-results.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
