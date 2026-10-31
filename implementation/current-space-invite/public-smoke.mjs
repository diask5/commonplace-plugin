import {chromium,request} from '../commonplace-source/node_modules/playwright/index.mjs';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const origin='https://34.27.253.220',out=new URL('./',import.meta.url),api=await request.newContext({ignoreHTTPSErrors:false}),summary={};
for(const path of ['/healthz','/.well-known/oauth-authorization-server','/.well-known/agent-configuration']){const r=await api.get(origin+path);summary[path]=r.status();if(r.status()!==200)throw Error(path+': '+r.status());}
const auth=await api.get(origin+'/authorize',{maxRedirects:0});summary.authorize={status:auth.status(),redirect:auth.headers().location?.split('?')[0]};if(![302,303].includes(auth.status()))throw Error('Compiled authorize unavailable');
const mcp=await api.post(origin+'/mcp',{data:{jsonrpc:'2.0',id:1,method:'tools/list'}});summary.unauthenticatedMcp=mcp.status();if(mcp.status()!==401)throw Error('MCP authentication not required');
summary.assets=[];
for(const name of ['context-space-invitations.mjs','context-product.mjs','context-conversations.mjs','context-native-setup.mjs','context-setup-request.mjs','personal-assistant-setup.mjs','mcp-resource-source-setup.mjs']){
 const r=await api.get(origin+'/context/assets/'+name),data=await r.body(),expected=await readFile(new URL('../commonplace-source/apps/commonplace-account/server/context-assets/'+name,import.meta.url));if(r.status()!==200||!data.equals(expected))throw Error('Live asset differs: '+name);summary.assets.push({name,sha256:createHash('sha256').update(data).digest('hex')});}
const browser=await chromium.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});summary.screens=[];
try{for(const [name,width,height] of [['desktop',1440,1000],['phone',390,844]]){
 const ctx=await browser.newContext({ignoreHTTPSErrors:false,viewport:{width,height}}),page=await ctx.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto(origin,{waitUntil:'domcontentloaded'});await page.getByRole('button',{name:/continue with google/i}).waitFor({state:'visible',timeout:20000});
 if(await page.locator('#invite-people').count()!==1||await page.locator('#invite-people').isVisible())throw Error('Invitation action must exist and stay hidden until signed in');
 if(await page.locator('#quick-invite-permission').count()!==1||await page.locator('#quick-invite-members').count()!==1)throw Error('Context-aware invitation controls missing');if(await page.locator('#setup-activate').count()!==1)throw Error('Activation action missing');const setupDetail=await page.locator('#setup-details').textContent();if(!setupDetail.includes('new chat in the same workspace')||setupDetail.includes('reload the plugin'))throw Error('Stale GUI reload guidance');
 const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);if(overflow||errors.length)throw Error(JSON.stringify({width,overflow,errors}));await page.screenshot({path:new URL('production-'+name+'.png',out).pathname,fullPage:true});summary.screens.push({name,width,googleButtonVisible:true,invitePresent:true,inviteHiddenUntilSignedIn:true,overflow,errors});await ctx.close();
}}finally{await browser.close();await api.dispose();}
await writeFile(new URL('public-smoke.json',out),JSON.stringify(summary,null,2)+'\n');console.log(JSON.stringify(summary));
