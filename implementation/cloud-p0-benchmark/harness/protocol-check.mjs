// Model-free verification of the published remote /mcp retrieval surface.
// Speaks JSON-RPC over HTTP with the fixture reader bearer. No model is called;
// this proves the service path, never a model answer.
import {readFile,writeFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(process.env.BENCH_ROOT||path.dirname(fileURLToPath(import.meta.url))+'/..');
const session=JSON.parse(await readFile(path.join(root,'harness/fixture-session.private.json'),'utf8'));
const plan=JSON.parse(await readFile(path.join(root,'harness/plan.json'),'utf8'));
let id=0;const steps=[];
async function rpc(method,params){
 const body={jsonrpc:'2.0',id:++id,method,...(params?{params}:{})};
 const started=Date.now();
 const response=await fetch(session.endpoint,{method:'POST',headers:{'content-type':'application/json',accept:'application/json, text/event-stream',authorization:'Bearer '+session.token,'MCP-Protocol-Version':'2025-06-18'},body:JSON.stringify(body)});
 const text=await response.text();
 let value=null;
 const data=text.split('\n').filter(l=>l.startsWith('data: ')).map(l=>l.slice(6)).join('');
 try{value=JSON.parse(data||text);}catch{}
 const step={method,params:params??null,status:response.status,milliseconds:Date.now()-started,value};
 steps.push(step);return step;
}
const payload=step=>{const text=step.value?.result?.content?.[0]?.text;if(typeof text!=='string')return null;try{return JSON.parse(text);}catch{return {unparsed:text};}};
const call=(name,args)=>rpc('tools/call',{name,arguments:args});

const init=await rpc('initialize',{protocolVersion:'2025-06-18',capabilities:{},clientInfo:{name:'retrieval-protocol-check',version:'1.0.0'}});
await rpc('notifications/initialized');
const tools=await rpc('tools/list');
const names=(tools.value?.result?.tools||[]).map(t=>t.name);

const findings=[];
for(const c of plan.cases){
 const search=await call('archive_search',{query:c.project+' pilot'});
 const found=payload(search);
 const hits=found?.results||[];
 const reads=[];
 for(const documentId of [...new Set(hits.map(h=>h.documentId))]){
  const read=await call('archive_read',{documentId,offset:0});
  const value=payload(read);
  reads.push({documentId,isError:!!read.value?.result?.isError,changed:!!value?.changed,restart:!!value?.restart,
   citations:value?.citations||[],characters:value?.text?.length??null,totalCharacters:value?.totalCharacters??null,
   nextOffset:value?.nextOffset??null,revision:value?.revision??null,
   containsLatestDate:typeof value?.text==='string'&&value.text.includes(c.date),
   containsOwner:typeof value?.text==='string'&&value.text.includes(c.owner),
   containsReason:typeof value?.text==='string'&&value.text.includes(c.reason),
   milliseconds:read.milliseconds});
 }
 findings.push({case:c.id,project:c.project,searchRevision:found?.revision??null,searchMode:found?.mode??null,
  searchMilliseconds:search.milliseconds,hitDocumentIds:hits.map(h=>h.documentId),hitTitles:hits.map(h=>h.title),
  snippetsOnlyCarryCitation:hits.every(h=>typeof h.citation==='string'),reads});
}

// Multi-page read: follow nextOffset with the revision that read returned,
// exactly as the published instructions direct, and accumulate citations.
const logistics=payload(await call('archive_search',{query:'Logistics checklist'}));
const logisticsDocument=(logistics?.results||[])[0]?.documentId??null;
const pages=[];
if(logisticsDocument){
 let offset=0,revision,reachedClosing=false,guardCount=0;
 while(guardCount++<20){
  const read=await call('archive_read',{documentId:logisticsDocument,offset,...(offset?{revision}:{})});
  const value=payload(read);
  if(!value||value.changed||read.value?.result?.isError){pages.push({offset,failed:true,value});break;}
  revision=value.revision;
  if(typeof value.text==='string'&&value.text.includes('Closing statement: start time and timezone remain undecided'))reachedClosing=true;
  pages.push({offset,characters:value.text?.length??null,citations:value.citations||[],nextOffset:value.nextOffset,revision:value.revision,milliseconds:read.milliseconds});
  if(value.nextOffset==null)break;
  offset=value.nextOffset;
 }
 pages.push({reachedClosingStatement:reachedClosing});
}

// Bounds and fences, recorded exactly as the service answers them.
const oversize=await call('archive_read',{documentId:findings[0].reads[0]?.documentId,offset:0,limit:16001});
const zero=await call('archive_read',{documentId:findings[0].reads[0]?.documentId,offset:0,limit:0});
const maxPage=await call('archive_read',{documentId:findings[0].reads[0]?.documentId,offset:0,limit:16000});
const staleSearch=await call('archive_search',{query:plan.cases[0].project,revision:1});
const staleRead=await call('archive_read',{documentId:findings[0].reads[0]?.documentId,revision:1});
const unknownDocument=await call('archive_read',{documentId:'unified-000000000000000000000000'});
const badArgument=await call('archive_search',{query:plan.cases[0].project,notAnArgument:true});

// Write guard: the model token holds commonplace:read only. Every tool the
// published catalog marks readOnlyHint:false must be refused by the service.
const catalog=tools.value?.result?.tools||[];
const writeTools=catalog.filter(t=>t.annotations?.readOnlyHint!==true).map(t=>t.name);
const guard=[];
for(const name of ['create_context_space','request_space_context','run_cloud_task'].filter(n=>writeTools.includes(n))){
 const attempt=await call(name,name==='create_context_space'?{name:'Write guard probe'}:name==='request_space_context'?{groupId:'none',contributorId:'none',query:'write guard probe'}:{prompt:'write guard probe',nonce:'0123456789abcdef01234567'});
 guard.push({name,httpStatus:attempt.status,isError:!!attempt.value?.result?.isError,jsonRpcError:attempt.value?.error?.message??null,text:attempt.value?.result?.content?.[0]?.text??null});
}

const report={
 baseline:plan.baseline,
 serverInfo:init.value?.result?.serverInfo??null,
 protocolVersion:init.value?.result?.protocolVersion??null,
 instructionsSha256:null,
 instructionsCharacters:(init.value?.result?.instructions||'').length,
 toolCount:names.length,toolNames:names,
 archiveToolsPresent:['archive_list','archive_search','archive_read'].every(n=>names.includes(n)),
 archiveToolDescriptions:(tools.value?.result?.tools||[]).filter(t=>t.name.startsWith('archive_')).map(t=>({name:t.name,readOnlyHint:t.annotations?.readOnlyHint??null,maxLimit:t.inputSchema?.properties?.limit?.maximum??null})),
 cases:findings,
 bounds:{
  limit16001:{isError:!!oversize.value?.result?.isError,text:oversize.value?.result?.content?.[0]?.text??null},
  limit0:{isError:!!zero.value?.result?.isError,text:zero.value?.result?.content?.[0]?.text??null},
  limit16000:{isError:!!maxPage.value?.result?.isError,characters:payload(maxPage)?.text?.length??null},
 },
 fences:{
  staleSearchRevision1:payload(staleSearch),
  staleReadRevision1:payload(staleRead),
  unknownDocument:{isError:!!unknownDocument.value?.result?.isError,text:unknownDocument.value?.result?.content?.[0]?.text??null,jsonRpcErrorCode:unknownDocument.value?.error?.code??null,jsonRpcErrorMessage:unknownDocument.value?.error?.message??null},
  unknownArgument:{isError:!!badArgument.value?.result?.isError,text:badArgument.value?.result?.content?.[0]?.text??null,jsonRpcErrorCode:badArgument.value?.error?.code??null},
 },
 paging:{documentId:logisticsDocument,pages},
 writeGuard:{modelTokenScope:session.tokenScope??null,readOnlyToolsInCatalog:catalog.filter(t=>t.annotations?.readOnlyHint===true).map(t=>t.name).length,writeToolsInCatalog:writeTools.length,probes:guard},
 currentArchiveRevision:session.archiveRevision,
};
const {createHash}=await import('node:crypto');
report.instructionsSha256=createHash('sha256').update(init.value?.result?.instructions||'').digest('hex');
await writeFile(path.join(root,'evidence/protocol-check.json'),JSON.stringify(report,null,2),{mode:0o600});
await writeFile(path.join(root,'evidence/protocol-steps.private.json'),JSON.stringify(steps,null,2),{mode:0o600});
process.stdout.write(JSON.stringify({toolCount:names.length,archiveToolsPresent:report.archiveToolsPresent,cases:findings.map(f=>({case:f.case,hits:f.hitDocumentIds.length,reads:f.reads.length,latest:f.reads.some(r=>r.containsLatestDate)}))},null,1)+'\n');
