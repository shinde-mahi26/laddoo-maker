const fs=require('fs'),path=require('path'),{spawn}=require('child_process');
const {chromium}=require('C:/Users/shind/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out=path.resolve(__dirname,'../rev_b/transform');
(async()=>{
 const browser=await chromium.launch({headless:true,args:['--enable-gpu','--use-gl=angle','--use-angle=d3d11','--ignore-gpu-blocklist']});
 const page=await browser.newPage({viewport:{width:1280,height:720}}),errors=[];
 page.on('pageerror',e=>errors.push(String(e)));
 await page.goto('http://127.0.0.1:8767/transform/?record');await page.waitForFunction(()=>window.studioReady);
 for(const t of [0,9,19,29,36]){const data=await page.evaluate(t=>renderFilmFrame(t),t);fs.writeFileSync(path.join(out,'preview-'+t+'.jpg'),Buffer.from(data,'base64'));}
 const state=await page.evaluate(()=>studioState);if(state.types!==55)throw Error('Missing 3D types: '+JSON.stringify(state));
 if(process.argv.includes('--preview')){console.log(JSON.stringify({state,errors}));await browser.close();return;}
 const fps=30,frames=36*fps;
 const ff=spawn('C:/Users/shind/AppData/Local/ms-playwright/ffmpeg-1011/ffmpeg-win64.exe',['-y','-f','image2pipe','-c:v','mjpeg','-framerate',String(fps),'-i','pipe:0','-c:v','libvpx','-deadline','realtime','-cpu-used','6','-lag-in-frames','0','-b:v','3500k','-threads','4',path.join(out,'transformation.webm')]);
 let log='';ff.stderr.on('data',d=>log+=d);const done=new Promise(r=>ff.on('close',r));ff.stdin.on('error',e=>errors.push(String(e)));
 for(let i=0;i<frames;i++){const data=await page.evaluate(t=>renderFilmFrame(t),i/fps);if(!ff.stdin.write(Buffer.from(data,'base64')))await new Promise(r=>ff.stdin.once('drain',r));if(i%150===0)console.log('Rendered',i,'/',frames);}
 ff.stdin.end();const code=await done;await browser.close();if(code||errors.length)throw Error('Render failed '+code+' '+errors+' '+log.slice(-1500));
 fs.writeFileSync(path.join(out,'video-verification.json'),JSON.stringify({width:1280,height:720,fps,frames,duration:36,types:state.types,visualInstances:state.count,browserErrors:errors,bytes:fs.statSync(path.join(out,'transformation.webm')).size,geometry:'46 source CAD instances plus illustrative proposed fittings',motion:'Cinematic paths, not collision validated'},null,2));console.log('FILM COMPLETE');
})().catch(e=>{console.error(e);process.exit(1)});
