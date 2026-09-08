"""Reproducible feasibility audit and dimensioned, separated CAD review package."""
from pathlib import Path
import sys, os, math, json, csv, html
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT)]
import cadquery as cq
from laddoomaker.model import build_subassemblies
from laddoomaker.a07_orbital_rounder.cartridges import CARTRIDGES, installed_cartridge
from laddoomaker.a01_chassis.d02_1 import candidate_masses
from checks.acceptance import obj, ov

OUT=ROOT/'exports'/'engineering_review'
for d in ('parts','drawings','assemblies'): (OUT/d).mkdir(parents=True,exist_ok=True)

SPEC={
'A02':('SS304 proposed','Hopper 280 x 240 top; 110 x 80 throat; height 205; intended wall 1.2 mm. Existing solid is an envelope, not a hollow hopper. Lid/clamps provisional.'),
'A03':('SS304 shaft; motor unselected','Shaft diameter 12, active length 120, axis Z455 along Y. Arms, bearings, seals and complete torque transmission missing; torque/speed require mixture tests.'),
'A04':('SS304 food components proposed','Shaft diameter 12; rotor sweep diameter 68; housing ID80/OD84; nominal radial gap 6. Gate 50 x 45 x 1.5, travel 65. Paddles, inlet/outlet and drive interfaces unresolved.'),
'A05':('SS304 cup proposed; purchased load cell unselected','Cup OD70/ID60, height45; current geometry has no conical discharge. 1 kg load-cell class provisional. G2 70 x 50 x 1.5, travel60. Force path, mounting, overload stops, actuator and cable isolation unresolved.'),
'A06':('SS304 proposed','Width70; inlet Y205/Z278; lip Y155/Z208; slope54.46deg. Existing profile is 10 mm vertical depth, not the specified 1 mm sheet chute; supports and sidewalls missing.'),
'A07':('Food-contact polymer unselected / dry hardware unselected','Orbit radius3; trial speed100-320rpm; C52 insert nominal cavity diameter52, height25. Boss diameter38; deck aperture52; HTD3M 20T/24T provisional. Bearings, eccentric, guide interfaces, retention and bellows remain development items.'),
'A08':('Food-contact polymer unselected / drive unselected','Travel55; upper cartridge bottom Z225 home, Z170 forming. Intended spring1N/mm, trial force2-10N; spring, drive, guides and stops absent. C52 cup collision confirmed.'),
'A09':('Food-contact pusher material unselected; SS304 tray proposed','Pusher8 x 22 x 16; commanded sweep105 in +X; tray260 x 180 x 5. Actuator, linkage and receiving chute missing.'),
'A10':('Purchased components unselected','Electronics, HMI and emergency stop are envelopes only. 24V/~350W architecture provisional; final protection, interlocks, thermal design and wiring not designed.')}

LW2_MASSES=candidate_masses('LW2')
def detail(group,name):
    if group!='A01': return SPEC[group]
    pid=name.split('_')[0]
    mat=LW2_MASSES.get(pid,{}).get('material','SS304')
    thickness={'A01-001':1.5,'A01-002':1.2,'A01-003':1.2,'A01-004':1.5,'A01-005':0.8,'A01-006':0.8,'A01-007':0.8,'A01-009':3,'A01-014':1.0}
    return mat,f"Approved LW2 nominal section {thickness.get(pid,'see solid')} mm; envelope dimensions below are measured CAD extents. Bend development, joints, fits and isolation remain unresolved."

groups=build_subassemblies(); rows=[]; cards=[]; exploded=[]; actual=[]; errors=[]
colors=['#778899','#d2b26b','#6899a9','#92a976','#b79ac8','#bf917f','#69a4b5','#a78bb2','#a4ad83','#899cae']
for gi,(group,assembly) in enumerate(groups.items()):
    sub=[]; index=0
    for name,node in assembly.objects.items():
        if node.obj is None or '-KO-' in name or 'paddle_sweep' in name: continue
        shape=node.obj.val() if isinstance(node.obj,cq.Workplane) else node.obj
        for si,solid in enumerate(shape.Solids(),1):
            index+=1; ident=f'{name}__{si:02}'
            b=solid.BoundingBox(); dims=[b.xlen,b.ylen,b.zlen]
            local=solid.translate((-b.xmin,-b.ymin,-b.zmin))
            cq.exporters.export(local,str(OUT/'parts'/f'{ident}.step'))
            cq.exporters.export(local,str(OUT/'drawings'/f'{ident}.svg'),opt={'projectionDir':(1,-1,1),'width':440,'height':300,'showAxes':False,'marginLeft':25,'marginTop':25})
            material,note=detail(group,name)
            row={'part':ident,'parent':group,'material_status':material,'x_mm':round(dims[0],3),'y_mm':round(dims[1],3),'z_mm':round(dims[2],3),'installed_x_min':round(b.xmin,3),'installed_y_min':round(b.ymin,3),'installed_z_min':round(b.zmin,3),'volume_mm3':round(solid.Volume(),3),'valid':solid.isValid(),'specification':note,'status':'REVIEW ONLY - NOT FABRICATION RELEASE'}
            rows.append(row)
            if not solid.isValid(): errors.append(ident)
            # Deliberately generous part-grid separation; does not represent a removal trajectory.
            separated=local.translate((gi*2500+(index-1)%4*600,(index-1)//4*700,0))
            exploded.append(separated); actual.append(solid); sub.append(separated.translate((-gi*2500,0,0)))
            cards.append(f'<article id="{ident}"><h2>{html.escape(ident)}</h2><img src="drawings/{ident}.svg" alt="CAD isometric"><p><b>X {dims[0]:.2f} × Y {dims[1]:.2f} × Z {dims[2]:.2f} mm</b></p><p>{html.escape(material)}</p><p>{html.escape(note)}</p><a href="parts/{ident}.step">Individual 3D STEP</a></article>')
    cq.exporters.export(cq.Compound.makeCompound(sub),str(OUT/'assemblies'/f'{group}_PARTS_SEPARATED.step'))
    print(group,index,'solids exported',flush=True)
cq.exporters.export(cq.Compound.makeCompound(exploded),str(OUT/'assemblies'/'ALL_PARTS_SEPARATED.step'))
cq.exporters.export(cq.Compound.makeCompound(actual),str(OUT/'assemblies'/'ASSEMBLED_REVIEW.step'))
with (OUT/'PART_DIMENSIONS.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
(OUT/'PART_DIMENSIONS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')

measurements=[]
for code in CARTRIDGES:
    for angle in (0,90,180,270):
        from laddoomaker.parameters.motion_states import orbit_xy
        x,y=orbit_xy(angle)
        lower=installed_cartridge(code,False,x,y,150).val()
        upper=installed_cartridge(code,True,215,115,170).val()
        measurements.append({'cartridge':code,'angle_deg':angle,'overlap_mm3':round(ov(lower,upper),3)})
# Test food sphere at nominal finished centre against the forming cups.
food=[]
for code,spec in CARTRIDGES.items():
    ball=cq.Workplane('XY').sphere(spec.nominal_diameter/2).translate((215,115,178)).val()
    food.append({'cartridge':code,'nominal_ball_mm':spec.nominal_diameter,'upper_food_overlap_mm3':round(ov(ball,installed_cartridge(code,True,215,115,170).val()),3),'lower_food_overlap_mm3':round(ov(ball,installed_cartridge(code,False,218,115,150).val()),3)})
speed=[]
for rpm in (100,200,320):
    w=rpm*2*math.pi/60
    speed.append({'rpm':rpm,'frequency_hz':rpm/60,'speed_m_s':.003*w,'acceleration_m_s2':.003*w*w,'force_per_kg_N':.003*w*w})
trajectory=[{'horizontal_speed_m_s':u,'time_s':.04/u,'drop_mm':1000*(.04*1.4+.5*9.81*(.04/u)**2)} for u in (.2,.5,1.0)]
evidence={'solid_count':len(rows),'invalid_solids':errors,'cup_interference':measurements,'nominal_ball_interference':food,'orbit':speed,'point_particle_chute_tangent_transfer':trajectory,'minimum_tangent_drop_mm':56,'chute_lip_to_nominal_ball_centre_drop_mm':30}
(OUT/'FEASIBILITY_EVIDENCE.json').write_text(json.dumps(evidence,indent=2),encoding='utf-8')
summary=''.join(f"<tr><td>{r['cartridge']}</td><td>{r['angle_deg']}</td><td>{r['overlap_mm3']}</td></tr>" for r in measurements)
page='''<!doctype html><html><head><meta charset="utf-8"><title>LaddooMaker engineering review</title><style>body{font:16px system-ui;margin:36px;background:#f3f4f5;color:#243342}header{max-width:1100px}a{color:#145da0}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(390px,1fr));gap:20px}article{background:white;padding:20px;border:1px solid #ccd4da;break-inside:avoid}h2{font-size:16px;overflow-wrap:anywhere}img{width:100%;height:300px;object-fit:contain}td,th{padding:6px 15px;border:1px solid #c5ccd2}table{border-collapse:collapse} @media print{main{display:block}article{page-break-after:always}header{page-break-after:always}}</style></head><body><header><h1>LaddooMaker — feasibility and separated CAD</h1><p><b>Current design cannot be built as a working machine without further engineering.</b> The concept warrants a prototype, but cup collisions, incomplete food passage and missing mechanisms prevent functional approval.</p><p>Each sheet shows one connected CAD solid and its measured X/Y/Z envelope. These are not machining dimensions or production drawings. Fused bodies can represent several manufactured pieces; missing components have no invented dimensions. All dimensions are mm.</p><p><a href="assemblies/ASSEMBLED_REVIEW.step">Assembled 3D</a> · <a href="assemblies/ALL_PARTS_SEPARATED.step">All parts separated in 3D</a> · <a href="PART_DIMENSIONS.csv">Dimension register</a> · <a href="FEASIBILITY_REPORT.md">Full feasibility report</a></p><h2>Forming cup collisions — actual CAD intersection</h2><table><tr><th>Cartridge</th><th>Orbit degrees</th><th>Overlap mm³</th></tr>'''+summary+'''</table><p>Separated positions use a spaced review grid, not a disassembly path. Part STEP files have their minimum corner at local zero; original locations are retained in the dimension register. Review geometry excludes wire keep-outs and rotor sweep.</p></header><main>'''+''.join(cards)+'</main></body></html>'
(OUT/'PART_CATALOG.html').write_text(page,encoding='utf-8')
(OUT/'FEASIBILITY_REPORT.md').write_text((ROOT/'docs'/'FEASIBILITY_REVIEW_2026_09_06.md').read_text(encoding='utf-8'),encoding='utf-8')
print(json.dumps(evidence,indent=2),flush=True)
os._exit(1 if errors else 0)
