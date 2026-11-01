import json,time,threading,subprocess,shutil,os,urllib.request
from pathlib import Path
root=Path('/var/lib/commonplace/rollout-inputs/20261101-resumable-context');pid=subprocess.check_output(['systemctl','show','commonplace','--property','MainPID','--value'],text=True).strip();start=time.monotonic();deadline=start+45
stop=threading.Event();samples=[];health=[];wchan={};trace=None
if shutil.which('strace'):
 trace=subprocess.Popen(['timeout','45','strace','-qq','-tt','-T','-e','trace=fsync,fdatasync','-p',pid,'-o',str(root/'flush69.log')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def sample():
 while time.monotonic()<deadline:
  try:
   w=Path('/proc/'+pid+'/wchan').read_text().strip();wchan[w]=wchan.get(w,0)+1
   if len(samples)<1 or time.monotonic()-samples[-1]['at']>1:
    samples.append({'at':time.monotonic(),'cpu':Path('/proc/stat').read_text().splitlines()[0],'disk':next(l for l in Path('/proc/diskstats').read_text().splitlines() if l.split()[2]=='sdb'),'io':Path('/proc/'+pid+'/io').read_text(),'stat':Path('/proc/'+pid+'/stat').read_text(),'memoryPressure':Path('/proc/pressure/memory').read_text(),'ioPressure':Path('/proc/pressure/io').read_text()})
  except FileNotFoundError:break
  time.sleep(.1)
t=threading.Thread(target=sample);t.start()
while time.monotonic()<deadline-5:
 s=time.monotonic()
 try:
  with urllib.request.urlopen('http://127.0.0.1:3000/healthz',timeout=12) as r:v=json.load(r)
  health.append({'elapsed':time.monotonic()-s,'ready':v.get('ready')})
 except Exception as e:health.append({'elapsed':time.monotonic()-s,'error':type(e).__name__})
 time.sleep(1)
t.join()
if trace:
 try:trace.wait(timeout=2)
 except subprocess.TimeoutExpired:pass
out={'pid':int(pid),'duration':time.monotonic()-start,'health':health,'wchan':wchan,'samples':samples,'traceCollected':trace is not None};(root/'capacity69.json').write_text(json.dumps(out))
a=samples[0];b=samples[-1];ca=list(map(int,a['cpu'].split()[1:]));cb=list(map(int,b['cpu'].split()[1:]));delta=[y-x for x,y in zip(ca,cb)];total=sum(delta[:8]);diskA=list(map(int,a['disk'].split()[3:]));diskB=list(map(int,b['disk'].split()[3:]));d=[y-x for x,y in zip(diskA,diskB)];elapsed=b['at']-a['at'];n=d[0]+d[4];jiffies=int(subprocess.check_output(['getconf','CLK_TCK'],text=True));pa=a['stat'].split();pb=b['stat'].split();pcpu=sum(int(pb[i])-int(pa[i]) for i in [13,14])/jiffies/elapsed*100
summary={'seconds':round(elapsed,2),'health':health,'wchan':wchan,'cpu':{'userPercent':delta[0]/total*100,'systemPercent':delta[2]/total*100,'idlePercent':delta[3]/total*100,'iowaitPercent':delta[4]/total*100,'stealPercent':delta[7]/total*100,'mainProcessPercent':pcpu},'disk':{'readIOPS':d[0]/elapsed,'writeIOPS':d[4]/elapsed,'awaitMs':(d[3]+d[7])/n if n else 0,'utilPercent':d[9]/(elapsed*10),'weightedQueue':d[10]/(elapsed*1000)},'traceCollected':trace is not None}
if trace:
 import re
 lines=(root/'flush69.log').read_text().splitlines();dur=[float(x) for line in lines for x in re.findall(r'<([0-9.]+)>',line)];summary['flush']={'count':len(dur),'maxSeconds':max(dur,default=0),'totalSeconds':sum(dur),'over100ms':sum(x>.1 for x in dur)}
(root/'capacity69-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary))
