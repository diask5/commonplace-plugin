from pathlib import Path, PurePosixPath
import hashlib,json,os,subprocess,urllib.request,zipfile,tempfile,shutil
os.umask(0o077)
h=Path.home();root=Path(__file__).parent
version='0.4.31';expected='968f1157f0942c660eb5325cb287cfb70f54be2da0b8d7334d004eb7ad944c33'
target=h/'Library/Application Support/Meet Proxy/plugins'/version
permissions=lambda:{str(p):hashlib.sha256(json.dumps(json.loads(p.read_text()).get('permissions',{}),sort_keys=True).encode()).hexdigest() if p.exists() else None for p in [h/'.claude/settings.json',h/'.claude/settings.local.json']}
def identity():
 s=json.loads((h/'.commonplace/account-client.json').read_text())['session'];return {k:s.get(k) for k in ['origin','account','humanAccount','device']}
before=identity();perm=permissions();assert (before['humanAccount'] or before['account'])['email']=='diaskyle10@gmail.com'
archive=root/'meet-proxy-0.4.31.zip'
if not archive.exists():
 with urllib.request.urlopen('https://github.com/diask5/commonplace-plugin/releases/download/meet-proxy-v0.4.31/meet-proxy-0.4.31.zip',timeout=60) as r,archive.with_suffix('.partial').open('wb') as f:shutil.copyfileobj(r,f)
 archive.with_suffix('.partial').rename(archive)
assert hashlib.sha256(archive.read_bytes()).hexdigest()==expected,'ZIP checksum mismatch'
target.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(archive) as z:
 assert len(z.namelist())==len(set(z.namelist()))
 for i in z.infolist():
  p=PurePosixPath(i.filename);assert not p.is_absolute() and '..' not in p.parts and str(p)==i.filename and not i.is_dir();assert (i.external_attr>>16)&0o170000!=0o120000,'No symlinks'
 if not target.exists():
  staging=Path(tempfile.mkdtemp(prefix='.0.4.31-',dir=target.parent))
  try:
   for i in z.infolist():
    p=staging/i.filename;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(i));p.chmod((i.external_attr>>16)&0o777)
   staging.rename(target)
  finally:
   if staging.exists():shutil.rmtree(staging)
 for i in z.infolist():assert (target/i.filename).read_bytes()==z.read(i),'Installed bytes differ'
env=os.environ.copy()
for key in list(env):
 if key.startswith(('CLAUDE_','CONDUCTOR_')) or key.startswith('CODEX_') and key!='CODEX_HOME':del env[key]
assert not env.get('CODEX_HOME') or Path(env['CODEX_HOME']).resolve()==(h/'.codex').resolve(),'Unexpected Codex profile'
cli=h/'Library/Application Support/com.conductor.app/bin/codex';env['PATH']=str(cli.parent)+os.pathsep+env.get('PATH','')
config=h/'.codex/config.toml';old=config.read_text();(root/'codex-before.private.toml').write_text(old)
with (root/'configure-codex.log').open('w') as log:subprocess.run([str(target/'runtime/node'),str(target/'server/configure-codex.mjs')],env=env,stdout=log,stderr=subprocess.STDOUT,check=True,timeout=60)
assert config.read_text()==old.replace('/plugins/0.4.28/','/plugins/0.4.31/'),'Unexpected Codex configuration delta'
claude=h/'.local/bin/claude'
for name,args in [('marketplace',['plugin','marketplace','update','commonplace']),('plugin',['plugin','update','meet-proxy@commonplace'])]:
 with (root/(name+'-update.log')).open('w') as log:subprocess.run([str(claude),*args],env=env,stdout=log,stderr=subprocess.STDOUT,check=True,timeout=90)
installed=json.loads((h/'.claude/plugins/installed_plugins.json').read_text())['plugins']['meet-proxy@commonplace'];assert any(p['version']==version for p in installed),'Claude plugin registry still old'
assert identity()==before,'Account changed';assert permissions()==perm,'Saved permissions changed'
result={'state':'passed','installedVersion':version,'zipSha256':expected,'accountPreserved':True,'savedPermissionsPreserved':True,'codexOnlyPluginPathsChanged':True,'claudePluginManagerUpdated':True}
(root/'install-result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
