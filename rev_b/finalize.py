from pathlib import Path
p=Path(__file__).parent/'output/index.html'
s=p.read_text()
s=s.replace('[35,44].forEach','[35,44,45].forEach')
s=s.replace("PARTS[i].name=(k?'Upper':'Lower')+' forming insert Ø'+cd;PARTS[i].dimensions=[cd+10,cd+10,cd/2+4.7];", "PARTS[i].name=k===2?'Upper tool spacer C'+cd:(k?'Upper':'Lower')+' forming insert Ø'+cd;PARTS[i].dimensions=k===2?[24,24,35-cd/2]:[cd+10,cd+10,cd/2+4.7];")
s=s.replace("(p.id==='35'||p.id==='44')?", "(['35','44','45'].includes(p.id))?").replace("(p.id==='35'?'lower':'upper')", "(p.id==='35'?'lower':p.id==='44'?'upper':'spacer')")
s=s.replace('45 / 45 components','46 / 46 components').replace('max="45" value="45"','max="46" value="46"')
p.write_text(s,encoding='utf-8')
p=Path(__file__).parent/'output/DESIGN.md'
s=p.read_text().replace('all 45 modelled items','all 46 modelled items')
s=s.replace('Maximum rigid cup overlap is zero in those sampled aligned states.', 'Maximum rigid cup overlap is zero in those sampled aligned states. Rear support and matched upper spacer are also checked against the nominal food sphere for all 15 sizes; no intrusion is allowed. Visual review exposed an earlier support/rod intrusion; the final revision moves the support behind the cup and terminates the rod above the head load module.')
p.write_text(s,encoding='utf-8')
