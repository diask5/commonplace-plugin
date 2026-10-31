from pathlib import Path
import urllib.request,hashlib,json,subprocess,tempfile,base64,os,time
os.umask(0o077)
root=Path(tempfile.mkdtemp(prefix='meet-proxy-current-space-invite-'))
origin='https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-server-20261031-current-space-invite/'
files={'runtime-update.json': '6713cbe66af9bd8f00f38dbc0161051c8e0028b17548da4bd4c9ece590a656c9', 'runtime-update-manifest.json': '1ab1d37c76ab8d663de2fac4e631207fd6a97c38921bac951d5ba9d9ac21b16d', 'deploy-cloud-update.py': '6698a63da1841553cc112991386bf682b72a758eae9e910c7381cf07d603ff32'}
for name,digest in files.items():
 with urllib.request.urlopen(origin+name,timeout=60) as response:data=response.read()
 assert hashlib.sha256(data).hexdigest()==digest,name
 (root/name).write_bytes(data)
with urllib.request.urlopen('https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-server-20261031-setup-activation/runtime-update-manifest.json',timeout=60) as response:base=response.read()
assert hashlib.sha256(base).hexdigest()=='4af282abf315d35862ff04a5fdbec7bf6becacf20593627022f1c55c6a4781e8'
current=Path('/opt/commonplace/current').resolve();assert current.name=='20261031-setup-activation'
for name,digest in json.loads(base)['files'].items():assert hashlib.sha256((current/name).read_bytes()).hexdigest()==digest,('baseline mismatch',name)
values=json.loads((root/'runtime-update.json').read_text());changed=[name for name,value in values.items() if not (current/name).exists() or (current/name).read_bytes()!=base64.b64decode(value)]
assert sorted(changed)==['dist/standalone/account-runtime/context-assets/context-space-invitations.mjs', 'dist/standalone/account-runtime/context-product-ui.mjs'], changed
(root/'preflight.json').write_text(json.dumps({'baseline':current.name,'files':len(values),'changed':changed}))
runner="from pathlib import Path\nimport subprocess,json,hashlib,base64,time,traceback,sqlite3\nroot=Path(__file__).parent\ntry:\n subprocess.run(['python3',str(root/'deploy-cloud-update.py'),'--bundle',str(root/'runtime-update.json'),'--bundle-sha256','6713cbe66af9bd8f00f38dbc0161051c8e0028b17548da4bd4c9ece590a656c9','--baseline','20261031-setup-activation','--release','20261031-current-space-invite','--code-only'],check=True)\n active=Path('/opt/commonplace/current').resolve();assert active.name=='20261031-current-space-invite'\n values=json.loads((root/'runtime-update.json').read_text())\n for name,value in values.items():\n  assert (active/name).read_bytes()==base64.b64decode(value),name\n  subprocess.run(['runuser','-u','commonplace','--','test','-r',str(active/name)],check=True)\n health=subprocess.check_output(['systemctl','is-active','commonplace','commonplace-runtime','nginx'],text=True).splitlines();assert health==['active']*3\n result={'state':'passed','release':active.name,'filesVerified':len(values),'serviceReadableFiles':len(values),'services':health,'migrations':'unchanged; verified code-only activation','previous':'20261031-setup-activation'}\nexcept Exception as e:\n traceback.print_exc();result={'state':'failed','errorType':type(e).__name__,'currentRelease':Path('/opt/commonplace/current').resolve().name}\nresult['finishedAt']=time.time()\n(root/'result.json').write_text(json.dumps(result));print(json.dumps(result),flush=True)\n"
(root/'run.py').write_text(runner)
with (root/'deploy.log').open('w') as log:
 p=subprocess.Popen(['python3','-u',str(root/'run.py')],stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
print(json.dumps({'state':'started','pid':p.pid,'directory':str(root),'baselineFilesVerified':len(json.loads(base)['files']),'changedFiles':changed}),flush=True)
