from pathlib import Path
p=Path(__file__).parent/'output/index.html'
s=p.read_text(encoding='utf-8-sig')
s=s.replace("$('partlink').href=p.id+'.step'", "$('partlink').href=(p.id==='35'||p.id==='44')?'C'+(Math.round(10*Math.cbrt(6*mass/(Math.PI*rho))/2)*2)+'_'+(p.id==='35'?'lower':'upper')+'.step':p.id+'.step'")
s=s.replace("PARTS[i].dimensions=[cd+10,cd+10,cd/2+4.7];", "PARTS[i].dimensions=[cd+10,cd+10,cd/2+4.7];$('picker').options[i].textContent=PARTS[i].id+' · '+PARTS[i].name;$('partlist').children[i].textContent=PARTS[i].id+' / '+PARTS[i].name;")
s=s.replace("elapsed=0;running=false;$('play').textContent='▶ Run cycle'}", "elapsed=0;running=false;$('play').textContent='▶ Run cycle';if(selected>=0)select(selected)}")
s=s.replace('distance=1350,goalDistance=1350','distance=1600,goalDistance=1600').replace('goalDistance=1350','goalDistance=1600').replace('exploded?1900:1350','exploded?2100:1600')
s=s.replace('renderer.setPixelRatio', 'renderer.setPixelRatio',1)
p.write_text(s,encoding='utf-8')
