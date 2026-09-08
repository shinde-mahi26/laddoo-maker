from pathlib import Path
root=Path(__file__).parent/'output'
for name in ['index.html','DESIGN.md']:
    p=root/name
    s=p.read_text(encoding='utf-8')
    # Recover a single accidental Windows legacy decode, leaving new Unicode text intact.
    for source,target in [('Â·','·'),('Â³','³'),('Ã—','×'),('Ã˜','Ø'),('â†’','→'),('â€“','–'),('â€”','—'),('â‰¤','≤'),('â‰¥','≥'),('âˆ’','−'),('âˆš','√'),('Âµ','µ'),('Â°','°'),('â€“','–'),('â–¶','▶'),('â…¡','Ⅱ'),('â†»','↻'),('â‰ˆ','≈'),('â€²','′'),('â€˜','‘'),('â€™','’')]:
        s=s.replace(source,target)
    if name=='index.html':
        s=s.replace("PARTS[i].name=(k?'Upper':'Lower')+' forming insert Ø'+cd;PARTS[i].dimensions=[cd+10,cd+10,cd/2+4.7];", "PARTS[i].name=k===2?'Upper tool spacer C'+cd:(k?'Upper':'Lower')+' forming insert Ø'+cd;PARTS[i].dimensions=k===2?[24,24,35-cd/2]:[cd+10,cd+10,cd/2+4.7];")
    s=s.replace('Â²','²').replace('Â±','±')
    p.write_text(s,encoding='utf-8')
