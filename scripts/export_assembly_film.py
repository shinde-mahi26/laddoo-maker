"""One animation record per connected CAD solid, with a complete ordered register."""
from pathlib import Path
import sys,json,csv,os
ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT/'src'),str(ROOT)]
import cadquery as cq
from laddoomaker.model import build_subassemblies
OUT=ROOT/'exports'/'assembly_film';OUT.mkdir(parents=True,exist_ok=True)
register={r['part']:r for r in json.loads((ROOT/'exports/engineering_review/PART_DIMENSIONS.json').read_text())}
# Spatial teaching order, not a collision-validated manufacturing route.
ORDER=['A01-011','A01-001','A01-010','A01-009_cframe_left','A01-009_cframe_right','A01-009_cframe_crossmembers','A01-013',
'A07-014','A07-013','A07-010','A07-011','A07-012','A07-003','A07-004','A07-002','A07-001',
'A01-004R','A01-004','A07-005','A07-006','A07-007','A07-C52',
'A01-002','A01-003','A01-015','A01-016','A01-017',
'A08-002','A08-C52','A05-900','A05-006','A05-001','A06-001',
'A04-005','A04-001','A04-002','A04-006','A04-900','A03-900','A03-004','A03-001',
'A02-001','A02-clamp','A02-002','A09-002','A09-006','A10-900','A01-014','A10-010','A10-011',
'A01-008P','A01-008_','A01-012','A01-005','A01-006','A01-007']
NAMES={'base_pan':'Base pan','rear_spine':'Rear structural spine','sanitary_partition':'Sanitary partition','food_deck':'Food deck','deck_ring':'Deck reinforcement ring',
'left_enclosure':'Left enclosure panel','right_enclosure':'Right enclosure panel','rear_cover':'Rear service cover','front_door_frame':'Front door / frame body',
'inspection_panel':'Inspection window','reinforcement_set':'Frame mounting pad','feet_set':'Foot / support pad','panel_hardware':'Panel fastener placeholder','structural_fasteners':'M6 fastener placeholder',
'fascia_carrier':'Control fascia','A03_adapter':'Agitator adapter plate','A04_adapter':'Feeder adapter plate','gland_plate':'Cable gland plate','cframe_left':'Left C-frame plate','cframe_right':'Right C-frame plate','cframe_crossmembers':'C-frame crossmember / pad',
'hopper_envelope':'Hopper envelope','lid':'Hopper lid','hopper_shaft':'Agitator shaft','retractable_dog_coupling':'Retractable dog coupling','gearmotor_envelope':'Agitator gearmotor envelope',
'rotor_shaft':'Feeder rotor shaft','motor_envelope':'Feeder motor envelope','rotor_hub':'Feeder hub','food_housing':'Feeder food housing','G1':'Primary gate G1','G2':'Weigh discharge gate G2',
'weigh_cup':'Weighing cup','load_cell':'Load-cell envelope','transfer_chute':'Transfer chute','lower_cartridge':'Lower C52 cartridge','upper_cartridge':'Upper C52 cartridge',
'moving_boss':'Orbital drive boss','orbit_carriage':'Orbital carriage','x_guide':'X guide envelope','y_guide':'Y guide envelope','bellows_outer_seat':'Bellows outer seat','bellows_inner_seat':'Bellows inner seat','bellows_envelope':'Bellows envelope',
'motor_pulley_20T':'20T motor pulley envelope','driven_pulley_24T':'24T driven pulley envelope','HTD3M_belt_envelope':'HTD3M belt envelope','rounder_motor':'Rounder motor envelope','tension_slots':'Motor tension plate','carriage':'Upper head carriage','pusher':'Ejector pusher','output_tray':'Output tray','electronics_envelope':'Electronics envelope','HMI':'HMI envelope','estop':'Emergency-stop envelope'}
records=[]
for group,asm in build_subassemblies().items():
 for name,node in asm.objects.items():
    if node.obj is None or '-KO-' in name or 'paddle_sweep' in name:continue
    shape=node.obj.val() if isinstance(node.obj,cq.Workplane) else node.obj
    for i,solid in enumerate(shape.Solids(),1):
        ident=f'{name}__{i:02}';r=register[ident];b=solid.BoundingBox();center=[(b.xmin+b.xmax)/2,(b.ymin+b.ymax)/2,(b.zmin+b.zmax)/2]
        vs,ts=solid.tessellate(.35)
        prefix=name.split('_',1)[-1];title=NAMES.get(prefix,'Hopper clamp envelope' if 'clamp' in name else prefix.replace('_',' '))
        rank=next((j for j,p in enumerate(ORDER) if name.startswith(p)),999)
        assert rank!=999,name
        direction=[0,0,180]
        if 'feet_set' in name:direction=[0,0,-110]
        elif 'left' in name:direction=[-240,0,0]
        elif 'right' in name:direction=[240,0,0]
        elif any(s in name for s in ['rear','motor_envelope','gearmotor','electronics','adapter']):direction=[0,240,0]
        elif any(s in name for s in ['door','panel','fascia','HMI','estop','tray','pusher','coupling']):direction=[0,-200,0]
        status='CAD solid / joint details unresolved'
        if 'envelope' in name or 'hardware' in name or 'fasteners' in name or 'guide' in name:status='Envelope / hardware selection unresolved'
        if 'cartridge' in name:status='Development part / forming collision unresolved'
        if 'crossmembers' in name or 'reinforcement' in name:status='Weldment piece / weld details unresolved'
        extra=''
        if 'structural_fasteners' in name:extra='CAD shank: Ø6 × 10 mm; head/thread absent'
        if 'feet_set' in name:extra='Foot designation M8; thread not modelled'
        if 'panel_hardware' in name:extra='CAD cylinder Ø8 × 8 mm; screw size unselected'
        records.append(dict(id=ident,name=title,group=group,rank=rank,center=center,dims=[r['x_mm'],r['y_mm'],r['z_mm']],material=r['material_status'],status=status,extra=extra,direction=direction,
          vertices=[round(c-center[k],4) for v in vs for k,c in enumerate((v.x,v.y,v.z))],triangles=[j for tri in ts for j in tri]))
records.sort(key=lambda r:(r['rank'],r['center'][2],r['center'][1],r['center'][0]))
for j,r in enumerate(records):r['step']=j+1;r['start_s']=12+j*4;r['end_s']=16+j*4
assert len(records)==70 and len({r['id'] for r in records})==70
(OUT/'assembly_data.js').write_text('window.ASSEMBLY_PARTS='+json.dumps(records,separators=(',',':'))+';',encoding='utf-8')
with (OUT/'ASSEMBLY_SEQUENCE.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=['step','id','name','group','dims','material','status','extra','start_s','end_s']);w.writeheader();w.writerows({k:r[k] for k in w.fieldnames} for r in records)
print('70 individually ordered and dimensioned CAD solids exported',flush=True);os._exit(0)
