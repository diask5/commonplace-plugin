// Verify and extract the published server runtime bundle into fixture/.
// Expected bundle: server release 20261026-current-read (0.4.28/runtime61 baseline).
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(process.env.BENCH_ROOT||path.dirname(fileURLToPath(import.meta.url))+'/..');
const EXPECTED='429bed64cdb57f2bbcd58ba5f3b273bbd4739ed6cb1e8c72c1c891182097dbe5';
const file=process.argv[2]||path.join(root,'artifacts/runtime-update.json');
const raw=await readFile(file);
const actual=createHash('sha256').update(raw).digest('hex');
if(actual!==EXPECTED)throw Error('Unexpected runtime bundle digest '+actual+'; expected the published '+EXPECTED);
const bundle=JSON.parse(raw);
let count=0;
for(const [name,data] of Object.entries(bundle)){
 const parts=path.parse(name);
 if(name.includes('..')||path.isAbsolute(name))throw Error('Refusing bundle path '+name);
 const dest=path.join(root,'fixture',name);
 await mkdir(path.dirname(dest),{recursive:true});
 await writeFile(dest,Buffer.from(data,'base64'),{mode:0o600});
 count++;void parts;
}
process.stdout.write(JSON.stringify({bundleSha256:actual,files:count})+'\n');
