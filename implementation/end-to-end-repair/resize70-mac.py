from pathlib import Path
import json,subprocess,time,os,sys
os.umask(0o077)
root=Path.home()/'.commonplace-code-verification/live-context-recovery-0.4.44/capacity70';root.mkdir(parents=True,exist_ok=True)
base=['gcloud','compute','instances'];scope=['--project','vertical-web-313417','--zone','us-central1-a','--quiet']
def run(args):
 p=subprocess.run(args,capture_output=True,text=True,timeout=65)
 if p.returncode:raise RuntimeError(p.stderr[-3000:])
 return json.loads(p.stdout)
def describe():return run(base+['describe','commonplace',*scope,'--format=json(id,selfLink,name,status,machineType,disks,networkInterfaces)'])
def pending(before):return run(['gcloud','compute','operations','list','--project','vertical-web-313417','--filter=targetLink='+before['selfLink']+' AND status!=DONE','--format=json(name,status,operationType)'])
def completed(stage):
 v=json.loads((root/(stage+'.json')).read_text());assert v.get('operation'),'Uncertain prior operation; manual reconciliation required'
 o=run(['gcloud','compute','operations','describe',v['operation'],*scope,'--format=json(name,status,error,operationType)'])
 assert o['status']=='DONE' and not o.get('error'),o
stage=sys.argv[1];current=describe()
if stage=='preflight':
 assert not (root/'before.json').exists(),'Existing preflight; inspect it'
 assert current['status']=='RUNNING' and current['machineType'].endswith('/e2-small')
 assert current['networkInterfaces'][0]['accessConfigs'][0]['natIP']=='34.27.253.220'
 addresses=run(['gcloud','compute','addresses','list','--project','vertical-web-313417','--filter=address=34.27.253.220','--format=json(address,status,addressType)']);assert len(addresses)==1 and addresses[0]['status']=='IN_USE' and addresses[0]['addressType']=='EXTERNAL'
 assert not pending(current)
 
 with (root/'before.json').open('x') as f:f.write(json.dumps(current,indent=2))
 print(json.dumps({'state':'preflight-passed','machine':'e2-small','reservedIpVerified':True,'disks':len(current['disks'])}));sys.exit()
before=json.loads((root/'before.json').read_text())
if stage=='status':
 operations={}
 for name in ['stop','resize','start']:
  p=root/(name+'.json')
  if p.exists():
   v=json.loads(p.read_text());operations[name]=run(['gcloud','compute','operations','describe',v['operation'],*scope,'--format=json(name,status,error,operationType)']) if v.get('operation') else v
 result={'state':current['status'],'machine':current['machineType'].split('/')[-1],'sameNetwork':before['networkInterfaces']==current['networkInterfaces'],'sameDisks':before['disks']==current['disks'],'pending':pending(before),'operations':operations}
 (root/'status.json').write_text(json.dumps(result,indent=2));print(json.dumps(result));sys.exit()
assert stage in ['stop','resize','start'] and not (root/(stage+'.json')).exists(),'Stage already issued or invalid; inspect instead of retry'
assert not pending(before),'Provider operation pending; no mutation issued'
if stage=='stop':assert current['status']=='RUNNING' and current['machineType'].endswith('/e2-small');args=['stop','commonplace']
elif stage=='resize':completed('stop');assert current['status']=='TERMINATED' and current['machineType'].endswith('/e2-small');args=['set-machine-type','commonplace','--machine-type=e2-standard-2']
else:completed('resize');assert current['status']=='TERMINATED' and current['machineType'].endswith('/e2-standard-2');args=['start','commonplace']
p=root/(stage+'.json')
with p.open('x') as f:f.write(json.dumps({'stage':stage,'state':'issuing','at':time.time()}))
try:
 o=run(base+args+scope+['--async','--format=json']);assert o.get('name') and o.get('targetLink')==before['selfLink'],o
 result={'stage':stage,'state':'submitted','operation':o['name'],'status':o['status']};p.write_text(json.dumps(result));print(json.dumps(result))
except Exception as e:
 (root/(stage+'-error.json')).write_text(json.dumps({'stage':stage,'state':'uncertain','errorType':type(e).__name__,'at':time.time()}))
 # Never infer that a timed-out command was unsubmitted, retry it, or launch a
 # recovery mutation. Inspect provider operations and instance first.
 print(json.dumps({'stage':stage,'state':'uncertain-reconcile-provider-operations'}));raise
