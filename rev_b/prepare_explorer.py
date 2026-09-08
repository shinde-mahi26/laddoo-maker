"""Prepare the engineering explorer from existing Rev-B tessellation; never alter CAD.

Run after build.py when CAD changes. Mesh STL exports retain assembly coordinates,
in millimetres; they are visualization meshes, not manufacturing drawings.
"""
from pathlib import Path
import json, struct, math, csv, hashlib

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'explorer'
OUT.mkdir(exist_ok=True)
(OUT / 'meshes').mkdir(exist_ok=True)
source = ROOT / 'output' / 'parts.js'
parts = json.loads(source.read_text(encoding='utf-8').split('=', 1)[1].rstrip(';\n\r '))
UNKNOWN = 'Not specified'
assembly_notes = {
 'Frame': 'Weld/finish base and rear frame in a fixture; confirm flatness and squareness. Fit feet.',
 'Electrical': 'Fit partition and rear enclosure; bond metalwork. Install modules with mains isolated.',
 'Dosing': 'Install feed cassette and hopper; hand-check scraper and shaft clearance. Fit seals and catch trays.',
 'Weighing': 'Fit weighed cradle and tip axis, then cell to frame. Check parasitic contact and calibrate with traceable masses.',
 'Transfer': 'Align rails, blocks, belt drive and travel stops. Hand-check the full 160 mm stroke.',
 'Forming': 'Fit lower-cup yoke, servo and keyed tooling. Set head hard stop with largest cavity first.',
 'Drives': 'Verify selected drive ratings, couplings and current limits; procurement interfaces remain unfinished.',
 'Output': 'Install chute and tray; verify output path before enabling motion.',
 'Guarding': 'Complete guards and interlocks; verify reach distances and fault behaviour before enabling motion.'
}
features = {
 '10': {'Throat X':95, 'Throat Y':110},
 '12': {'Shaft diameter':12},
 '160': {'Roller diameter':20, 'Roller length':106},
 '161': {'Roller diameter':20, 'Roller length':106},
 '20': {'Outer diameter':96, 'Wall thickness':1.5, 'Floor thickness':2},
 '35': {'Cavity diameter':46, 'Radial shell':5, 'Equatorial relief':0.3},
 '44': {'Cavity diameter':46, 'Radial shell':5, 'Equatorial relief':0.3},
 '60': {'Sheet thickness':3}
}
records=[]
for p in parts:
    points=list(zip(*[iter(p['vertices'])]*3))
    lo=[min(v[k] for v in points) for k in range(3)]
    hi=[max(v[k] for v in points) for k in range(3)]
    measured=[hi[k]-lo[k] for k in range(3)]
    assert all(abs(measured[k]-p['dimensions'][k])<0.05 for k in range(3)), p['id']
    pid='RB-'+p['id']
    same=[q for q in parts if (q['name'],q['material'],q['dimensions'])==(p['name'],p['material'],p['dimensions'])]
    step=ROOT/'output'/f"{p['id']}.step"
    assert step.is_file()
    downloads=[{'label':'Original concept CAD · STEP · mm','url':f"../output/{p['id']}.step",'kind':'CAD','sha256':hashlib.sha256(step.read_bytes()).hexdigest()},
               {'label':'Visualization mesh · STL · mm','url':f'meshes/{pid}.stl','kind':'Visualization mesh'}]
    with (OUT/'meshes'/f'{pid}.stl').open('wb') as f:
        f.write(f'{pid} Rev-B | mm | assembly coordinates | visualization only'.encode().ljust(80,b' '))
        f.write(struct.pack('<I',len(p['triangles'])//3))
        for a,b,c in zip(*[iter(p['triangles'])]*3):
            v=[points[k] for k in (a,b,c)]
            u=[v[1][k]-v[0][k] for k in range(3)];w=[v[2][k]-v[0][k] for k in range(3)]
            n=[u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0]]
            length=math.sqrt(sum(x*x for x in n)) or 1
            f.write(struct.pack('<12fH',*[x/length for x in n],*[x for point in v for x in point],0))
    record={
      'id':pid,'sourceId':p['id'],'typeId':'RBT-'+same[0]['id'],'name':p['name'],
      'assembly':p['group'],'quantity':1,'typeQuantity':len(same),'function':p['info'],
      'material':{'value':p['material'],'status':'Documented concept'},
      'dimensions':{'value':p['dimensions'],'units':'mm','kind':'Axis-aligned CAD bounding box','status':'Calculated from source CAD'},
      'features':features.get(p['id'],{}),'mass':{'value':None,'source':'unknown'},
      'manufacturing':UNKNOWN,'finish':UNKNOWN,'mates':UNKNOWN,'fasteners':UNKNOWN,
      'supplier':UNKNOWN,'modelNumber':UNKNOWN,'tolerances':UNKNOWN,
      'assemblyNotes':assembly_notes.get(p['group'],UNKNOWN),'removalNotes':UNKNOWN,
      'cleaningNotes':UNKNOWN,'maintenanceNotes':UNKNOWN,
      'revision':'Rev-B concept / 2026-09-06','source':'../build.py; ../output/DESIGN.md',
      'motion':p['motion'],'downloads':downloads,'bounds':{'min':lo,'max':hi},
      'geometryStatus':'Existing concept CAD; includes unfinished procurement envelopes'
    }
    # Preserve documentary sentences rather than infer undocumented specifications.
    sentences=[s.strip() for s in p['info'].split('. ') if s.strip()]
    for key,words in [('manufacturing',['weld','fold']),('finish',['polish','Ra ']),('removalNotes',['remov','lift-off','lift-out','release']),('cleaningNotes',['wash','clean','allergen']),('maintenanceNotes',['replace','wear']),('fasteners',['M8','fastener']),('mates',['coupl','bearing','trunnion'])]:
        selected=[s for s in sentences if any(w.lower() in s.lower() for w in words)]
        if selected: record[key]='. '.join(selected)
    records.append(record)
catalog={'revision':'Rev-B concept / 2026-09-06','units':'mm','sceneUnitsPerMm':1,
 'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'parts':records,'instanceCount':len(records),'typeCount':len(set(p['typeId'] for p in records)),
 'missingInputs':['Selected supplier models and mounting drawings','Final bearing, shaft, seal and fastener interfaces','Per-part masses or validated mass calculation inputs','Toleranced manufacturing drawings','Complete guards, wiring and safety interfaces','Measured food trials and operating performance']}
(OUT/'catalog.json').write_text(json.dumps(catalog,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'catalog.js').write_text('window.CATALOG='+json.dumps(catalog,ensure_ascii=False)+';',encoding='utf-8')
with (OUT/'BOM.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f);writer.writerow(['Instance ID','Type ID','Name','Assembly','Instance quantity','Type quantity','Material','CAD bounds X mm','CAD bounds Y mm','CAD bounds Z mm','Revision','Evidence','Mass source'])
    for p in records: writer.writerow([p['id'],p['typeId'],p['name'],p['assembly'],1,p['typeQuantity'],p['material']['value'],*p['dimensions']['value'],p['revision'],p['geometryStatus'],'unknown'])
print(f"Prepared {len(records)} instances / {catalog['typeCount']} types; CAD untouched.")
