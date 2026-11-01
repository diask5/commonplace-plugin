import base64,hashlib,json,os,subprocess,sys,time,urllib.request
from pathlib import Path
os.umask(0o077)
root=Path('/var/lib/commonplace/rollout-inputs/20261101-archive-visibility')
root.mkdir(parents=True,exist_ok=True)
base='https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-server-20261101-archive-visibility/'
hashes={'runtime-update.json':'1c5e63036293377470484bc0aa46b752d2cae875c1ede402a0d90b2d01ad134d','runtime-update-manifest.json':'af7aa91a50edd6b7944924e0da952b9cdb5e15ab19235edff87b11509130569c','deploy-cloud-update.py':'6698a63da1841553cc112991386bf682b72a758eae9e910c7381cf07d603ff32'}
for name,digest in hashes.items():
    content=urllib.request.urlopen(base+name,timeout=30).read()
    assert hashlib.sha256(content).hexdigest()==digest,name
    (root/name).write_bytes(content)
current=Path('/opt/commonplace/current').resolve()
assert current.name=='20261101-context-throughput','Baseline changed'
old=urllib.request.urlopen('https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-server-20261101-context-throughput/runtime-update-manifest.json',timeout=30).read()
assert hashlib.sha256(old).hexdigest()=='2932d0200e258cddd2375574c70f3efa7a1ed83ac5a9114cdd9b4fd8c79f5b51'
old=json.loads(old)
for name,digest in old['files'].items():
    assert hashlib.sha256((current/name).read_bytes()).hexdigest()==digest,'Baseline differs: '+name
bundle=json.loads((root/'runtime-update.json').read_text())
manifest=json.loads((root/'runtime-update-manifest.json').read_text())
assert set(bundle)==set(manifest['files'])
for name,content in bundle.items():
    assert hashlib.sha256(base64.b64decode(content,validate=True)).hexdigest()==manifest['files'][name]
old_migrations={p for p in old['files'] if p.startswith('drizzle/')}
new_migrations={p for p in bundle if p.startswith('drizzle/')}
assert new_migrations==old_migrations
assert not old_migrations-new_migrations
for name in old_migrations:assert manifest['files'][name]==old['files'][name],name
preflight={'baseline':current.name,'baselineFilesVerified':len(old['files']),'candidateFilesVerified':len(bundle),'newMigrations':sorted(new_migrations-old_migrations),'hashes':hashes}
(root/'preflight.json').write_text(json.dumps(preflight,indent=2))
runner='''import json,subprocess,time
from pathlib import Path
root=Path(__file__).parent
started=time.time()
with (root/'deployment.log').open('w') as log:
    p=subprocess.run(['python3',str(root/'deploy-cloud-update.py'),'--bundle',str(root/'runtime-update.json'),'--bundle-sha256','1c5e63036293377470484bc0aa46b752d2cae875c1ede402a0d90b2d01ad134d','--baseline','20261101-context-throughput','--release','20261101-archive-visibility','--code-only'],stdout=log,stderr=subprocess.STDOUT)
(root/'result.json').write_text(json.dumps({'exitCode':p.returncode,'seconds':time.time()-started}))
'''
assert not (root/'runner.py').exists(),'Runner already exists; inspect instead of retrying'
(root/'runner.py').write_text(runner)
with open(os.devnull,'rb') as inp, (root/'runner.log').open('wb') as out:
    process=subprocess.Popen(['python3',str(root/'runner.py')],stdin=inp,stdout=out,stderr=subprocess.STDOUT,start_new_session=True,close_fds=True)
print(json.dumps({'state':'started','pid':process.pid,'preflight':preflight}))
