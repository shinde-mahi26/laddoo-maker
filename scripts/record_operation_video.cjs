const fs=require('fs'),path=require('path'),{spawn}=require('child_process');
const {chromium}=require('C:/Users/shind/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out=path.resolve(__dirname,'../exports/operation_video');
(async()=>{const browser=await chromium.launch({headless:true,args:['--allow-file-access-from-files','--enable-unsafe-swiftshader']});const page=await browser.newPage({viewport:{width:1280,height:800}});page.on('pageerror',e=>console.error(e));
await page.goto('file:///'+out.replaceAll('\\','/')+'/animation.html');await page.waitForFunction(()=>window.ready===true);
const preview=process.argv.includes('--preview');
if(preview){for(const t of [1,9,16,23,30,38]){await page.evaluate(t=>draw(t),t);await page.locator('#movie').screenshot({path:path.join(out,'frame_'+t+'.png')});}await browser.close();return;}
const ff=spawn('C:/Users/shind/AppData/Local/ms-playwright/ffmpeg-1011/ffmpeg-win64.exe',['-y','-f','image2pipe','-c:v','mjpeg','-framerate','15','-i','pipe:0','-c:v','libvpx','-b:v','2400k',path.join(out,'LaddooMaker_Operating_Sequence.webm')]);let log='';ff.stderr.on('data',b=>{log+=b.toString()});const done=new Promise(resolve=>ff.on('close',resolve));
for(let i=0;i<630;i++){const b64=await page.evaluate(t=>{draw(t);return document.getElementById('movie').toDataURL('image/jpeg',.94).split(',')[1]},i/15);if(!ff.stdin.write(Buffer.from(b64,'base64')))await new Promise(r=>ff.stdin.once('drain',r));if(i%90===0)console.log('Frame',i,'/ 630');}
ff.stdin.end();const code=await done;fs.writeFileSync(path.join(out,'render_log.txt'),log);await browser.close();if(code)throw new Error('Encoder exit '+code);console.log('Video complete');})().catch(e=>{console.error(e);process.exit(1)});
