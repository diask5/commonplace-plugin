import os,json,sys,urllib.request,urllib.error
for line in sys.stdin:
 try:
  rpc=json.loads(line)
  if 'id' not in rpc:continue
  request=urllib.request.Request(os.environ['BENCH_ENDPOINT'],data=line.encode(),headers={'Content-Type':'application/json','Accept':'application/json','Authorization':'Bearer '+os.environ['BENCH_BEARER']})
  with urllib.request.urlopen(request,timeout=40) as response:result=response.read().decode()
  print(result,flush=True)
 except Exception as error:print(json.dumps({'jsonrpc':'2.0','id':rpc.get('id'),'error':{'code':-32603,'message':'Fixture transport unavailable: '+type(error).__name__}}),flush=True)
