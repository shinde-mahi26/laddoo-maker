"""Index separately generated concept illustrations without modifying CAD."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'part_images'
parts = json.loads((ROOT / 'explorer/catalog.json').read_text(encoding='utf-8'))['parts']
proposed = {'14','17','21','23','300','32','33','36','41','43','61','62','63','64'}
entries = []
seen = set()
for p in parts:
    id = p['typeId']
    if id in seen:
        continue
    seen.add(id)
    entries.append(dict(id=id, name=p['name'], group=p['assembly'],
        status='Proposed detail' if id[4:] in proposed else 'CAD-guided illustration',
        quantity=p['typeQuantity'], material=p['material']['value'],
        dimensions=p['dimensions']['value'], description=p['function'],
        image=id+'.png', reference='references/'+id+'.png'))
names = ['Socket-head cap screw','Hex nut','Flat washer','Sealed radial bearing',
    'Shaft lip seal','Flexible shaft coupling','Linear guide block','Timing pulley',
    'Compression spring','Guard hinge','Captive latch','Proximity sensor',
    'Protective bellows','Wiring harness','Levelling stud','Trunnion shaft']
for i,name in enumerate(names,1):
    id=f'P-{i:02d}'
    entries.append(dict(id=id,name=name,group='Small hardware',status='Proposed hardware',
        quantity=None,material='Proposed; final specification needed',dimensions=None,
        description='Generic proposed component. Size, quantity, material grade and fit are not yet specified in the CAD. This is not a purchasing or fabrication specification.',
        image=id+'.png',reference=None))
(OUT/'manifest.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False),encoding='utf-8')
missing=[p['image'] for p in entries if not (OUT/p['image']).exists()]
print(f'{len(entries)} catalogue entries; missing images: {missing}')
