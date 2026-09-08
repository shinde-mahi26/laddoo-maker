"""Independent source/download verification. No model rebuild or source mutation."""
from pathlib import Path
import json, hashlib, struct, os
import cadquery as cq

root=Path(__file__).resolve().parent
catalog=json.loads((root/'explorer/catalog.json').read_text(encoding='utf-8'))
raw=json.loads((root/'output/parts.js').read_text(encoding='utf-8').split('=',1)[1].rstrip(';\r\n '))
assert catalog['sourceSha256']==hashlib.sha256((root/'output/parts.js').read_bytes()).hexdigest()
assert len(catalog['parts'])==46
results=[]
for p in catalog['parts']:
    source=next(q for q in raw if q['id']==p['sourceId'])
    assert p['dimensions']['value']==source['dimensions']
    cad=root/'output'/f"{p['sourceId']}.step"
    assert hashlib.sha256(cad.read_bytes()).hexdigest()==p['downloads'][0]['sha256']
    text=cad.read_text(errors='replace')
    assert 'SI_UNIT(.MILLI.,.METRE.)' in text.replace(' ','')
    shape=cq.importers.importStep(str(cad)).val();b=shape.BoundingBox()
    bounds=[b.xlen,b.ylen,b.zlen]
    assert all(abs(bounds[k]-p['dimensions']['value'][k])<.02 for k in range(3)),p['id']
    mesh=(root/'explorer/meshes'/f"{p['id']}.stl").read_bytes()
    count=struct.unpack('<I',mesh[80:84])[0]
    assert count==len(source['triangles'])//3 and len(mesh)==84+50*count
    lo=[float('inf')]*3;hi=[float('-inf')]*3
    for i in range(count):
        tri=struct.unpack('<12fH',mesh[84+50*i:134+50*i])
        for j in (3,6,9):
            for k in range(3):lo[k]=min(lo[k],tri[j+k]);hi[k]=max(hi[k],tri[j+k])
    assert all(abs(lo[k]-p['bounds']['min'][k])<.001 and abs(hi[k]-p['bounds']['max'][k])<.001 for k in range(3))
    results.append({'id':p['id'],'STEP':'original hash and mm units verified','CAD bounds':'match','STL':'source triangles and bounds match'})
report={'source_preserved':True,'parts':46,'types':catalog['typeCount'],'results':results}
(root/'explorer/asset-verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('PASS: 46 original STEP files, mm units, CAD bounding boxes, and per-part STL meshes.',flush=True)
# This checkout's OpenCascade runtime can hang during native interpreter teardown.
# All files are closed and assertions completed before this clean process exit.
os._exit(0)
