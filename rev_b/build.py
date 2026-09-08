"""Rev-B concept CAD and transparent engineering screens. Millimetres."""
from pathlib import Path
import math, json, csv, shutil
import cadquery as cq

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
parts=[]
def box(x,y,z,at): return cq.Workplane('XY').box(x,y,z).translate(at).val()
def cyl(r,h,at): return cq.Workplane('XY').circle(r).extrude(h).translate(at).val()
def add(id,name,shape,material,group,info,motion='fixed'):
    b=shape.BoundingBox()
    parts.append(dict(id=id,name=name,shape=shape,material=material,group=group,info=info,motion=motion,
        dimensions=[round(b.xlen,2),round(b.ylen,2),round(b.zlen,2)]))
def cup(d,upper=False):
    r=d/2
    # Equatorial faces separated by 0.6 mm. No overlapping orbital rims.
    z=.3 if upper else -r-5
    blank=cyl(r+5,r+4.7,(0,0,z))
    return blank.cut(cq.Workplane('XY').sphere(r).val())

add('01','Folded base pan',box(600,400,2,(300,200,31)), 'SS304, 2 mm','Frame','600 × 400 mm footprint. Folded edges and welded corners; four M8 levelling feet. Detail bends and drain slope before fabrication.')
for i,(x,y) in enumerate([(30,30),(570,30),(30,370),(570,370)]):
    add(f'02{i}','Levelling foot',cyl(19,25,(x,y,5)),'Silicone pad + SS304 M8 stud','Frame','Four individually adjustable feet; target bench rating ≥40 kg. Pad and stud shown as one envelope.')
for i,x in enumerate([40,560]):
    s=box(30,30,430,(x,330,247)).cut(box(26,26,432,(x,330,247)))
    add(f'03{i}','Rear structural upright',s,'SS304 tube 30 × 30 × 2','Frame','TIG welded dry-side support. Frame deflection and weld fatigue require physical verification.')
add('04','Rear cross member',box(550,30,30,(300,330,460)).cut(box(552,26,26,(300,330,460))),'SS304 tube 30 × 30 × 2','Frame','Continuous rear frame; weld fixture required.')
add('05','Dry service enclosure',box(550,100,190,(300,345,135)).cut(box(546,96,186,(300,345,135))),'SS304, 2 mm','Electrical','Rear compartment: 24 VDC 240 W PSU, motor drivers, controller, safety relay and terminals. Envelopes, not selected supplier mounting patterns.')
add('06','Food / drive partition',box(560,2,240,(300,290,270)),'SS304, 2 mm','Frame','Sealed rear partition. Moving penetrations require removable boots and catch drains; no bearing exposed over food.')
# Hollow open hopper above belt. Entire cassette removes for washing.
outer=cq.Workplane('XY').rect(95,110).workplane(offset=145).rect(210,190).loft().val()
inner=cq.Workplane('XY').workplane(offset=-2).rect(92.6,107.6).workplane(offset=149).rect(207.6,187.6).loft().val()
add('10','Open hopper cassette',outer.cut(inner).translate((135,170,415)),'SS304, 1.2 mm','Dosing','Approximately 3.4 L geometric volume; 2 L working fill. Open throat 95 × 110 mm. Polished food side Ra target ≤0.8 µm. Removable radiused seams.')
add('11','Hopper lid',box(216,196,3,(135,170,562)),'Clear food-contact polycarbonate','Dosing','Lift-off lid with coded interlock. No reach into belt throat while enabled; supplier food-contact declaration required.')
add('12','Slow bridge-breaker shaft',cyl(6,105,(135,170,425)),'SS316L','Dosing','Quick-release shaft; external bearings and lip seals behind splash barrier. Intermittent 5–15 rpm; not a kneader.')
for i,z in enumerate([444,486]):
    add(f'13{i}','Flexible sweep paddle',box(80,8,15,(135,170,z)),'Platinum-cured food-contact silicone','Dosing','Soft replaceable blade. Clearance must be tuned to avoid crushing motichoor and trapping peanuts.')
add('14','Agitator gearmotor',cyl(28,65,(135,170,570)),'Aluminium motor shell, isolated dry','Drives','24 V BLDC, 20 W, output 5–15 rpm, ≥3 N·m continuous; torque-limited. Coupler and sanitary shaft seal procurement required.')
# Belt represented as actual continuous hollow loop, rollers axis Y.
belt=box(210,100,24,(160,170,397)).cut(box(210,102,20,(160,170,397)))
add('15','Metering belt cassette',belt,'Food-contact PU endless belt, 2 mm','Dosing','210 × 100 mm cassette. 0–35 mm/s coarse/fine feed. Belt may smear besan or bridge sticky jaggery; bench trial is required. Detachable scraper and catch tray.')
for i,x in enumerate([67,253]):
    s=cyl(10,106,(0,0,0)).rotate((0,0,0),(1,0,0),90).translate((x,223,397))
    add(f'16{i}','Belt roller',s,'SS304 tube / shaft','Dosing','Ø20 × 106 mm roller. External sealed bearings and tool-free tension release. Two rollers; return side contained.')
add('17','Belt gearmotor',box(55,55,55,(253,258,397)),'Aluminium motor shell','Drives','24 V BLDC 25 W; output 0–35 rpm, ≥1 N·m continuous. 10 mm roller radius. Encoder, current limit, stopped belt while weighing.')
add('18','Removable belt scraper',box(3,96,22,(265,170,386)),'Food-contact PEEK','Dosing','Replaceable thin edge; removes trailing smear into weigh cup. Maximum particle size initially ≤4 mm.')
# Weigh cup open top, rotating on load-cell supported cradle.
weigh=cyl(48,60,(270,170,308)).cut(cyl(46.5,62,(270,170,310)))
add('20','Tipping weigh cup',weigh,'SS304, 1.5 mm wall / 2 mm floor','Weighing','Ø96 × 60 mm, 0.40 L. Tares empty before every portion; complete tip cradle and motor sit on cell. 2 g / 3 g provisional accuracy targets, not validated.', 'weigh')
add('21','Single point load cell',box(80,20,15,(270,250,300)),'Anodized aluminium, dry cover','Weighing','2 kg capacity; 24-bit ADC. Fixed end rear, live end cup cradle. Flexible slack wires, no hoses or stiff parallel force path. Overload stops set to cell datasheet.')
add('22','Weighed cradle arm',box(14,78,8,(270,216,308)),'SS304','Weighing','Tip motor and cup supported at live cell end. Bearings, fasteners, motor torque reaction all on weighed structure. Shown as concept bracket.')
add('23','Weigh tip actuator',box(40,40,48,(270,238,340)),'Geared servo, aluminium dry shell','Drives','24 V geared position servo 15 W; ≥1.5 N·m continuous. Tip 150°, return home, then tare. No weighing during tip motion.')
# Linear shuttle at constant height; cup directly below dose, then travels 160 mm.
for i,y in enumerate([125,215]):
    add(f'30{i}','Shuttle guide rail',box(270,12,12,(350,y,155)),'Hardened steel, sealed dry shroud','Transfer','MGN12-class rail envelope; stainless bellows/cover needed. Two blocks per rail. Travel 160 mm. Lubricant isolated from food.')
add('31','Shuttle carriage',box(100,116,8,(270,170,168)),'SS304','Transfer','Timing-belt drive under catch deck; belt clamp and limit flags require supplier detail.', 'shuttle')
add('32','Shuttle timing belt',box(260,8,3,(350,260,160)),'Steel-cord polyurethane, dry','Transfer','HTD 3M, 9 mm width procurement target; diagram represents belt run. 20-tooth pulley radius 9.55 mm. Tensioner and return run detailed at procurement.')
add('33','Shuttle motor',box(42,48,42,(480,260,160)),'Closed-loop stepper / aluminium','Drives','24 V NEMA17 closed-loop stepper; ≥0.3 N·m at 200 rpm, 30 W budget. 160 mm stroke in 1.2 s; accel 0.5 m/s². Home + end limit sensors.')
add('34','Lower tilt bearing support',box(16,16,54,(270,239,195)),'SS304','Transfer','Rear support clear of every food cavity. Trunnion axis Z225; rear yoke and shaft must connect to cup exterior. CAD support envelope; final bearing and shaft fits need mechanical detail.', 'shuttle')
add('35','Lower forming insert Ø46',cup(46).translate((270,170,225)),'Food-contact POM-C','Forming','Split spherical cavity. Exchange matched pairs Ø36–64 in 2 mm steps. 0.6 mm equator relief avoids hard rim collision; flash/seam and sticking require food trials.', 'lower')
add('36','Lower tip servo',box(50,48,50,(270,257,225)),'Geared servo, aluminium dry shell','Drives','24 V 20 W, ≥2 N·m continuous; 120° outward tilt to eject. Home sensor; upper head must be raised before tip. Flexible cable carrier.', 'shuttle')
add('40','Press support arm',box(32,180,30,(430,240,450)),'SS304 rectangular section','Forming','Rear support to press. 150 N design force. Deflection and resonances unverified; hard stop prevents insert contact.')
add('41','Head linear actuator',box(58,64,145,(430,170,446)),'24 V screw actuator / steel and aluminium','Drives','50 W budget; 150 N continuous at ≥40 mm/s; 95 mm stroke. 4 mm lead, efficiency assumption 0.35. Encoder + two limits + load feedback; self-locking not assumed.')
add('42','Head push rod',cyl(8,40,(430,170,376)),'SS316L with sanitary bellows','Forming','Rod retracts 95 mm. Bellows not represented. Anti-rotation guides, brake or positive retention required; do not rely on software to hold head.', 'head')
add('43','Compliant head load module',cyl(20,16,(430,170,360)),'SS304 + spring steel in sealed boot','Forming','0–200 N compression sensor; 5 N/mm spring, 2–16 mm usable deflection. Adjustable 10–80 N trial force, hard cutoff 120 N. Spring and sensor shown as envelope.', 'head')
add('44','Upper forming insert Ø46',cup(46,True).translate((430,170,320)),'Food-contact POM-C','Forming','Matched upper cavity, lifted 95 mm in home pose. Static split-mould compression; no claim of hand-rolled texture. No orbital cup interference.', 'head')
add('45','Matched upper tool spacer',cyl(12,12,(430,170,348)),'SS304','Forming','Recipe-tool-specific spacer connects solid outside of upper cup to head module. Length 35 minus cavity radius, mm. Provided for every tool size; retained/keyed connection still requires detailing.', 'head')
# Downward sloping open discharge channel.
tray=box(120,105,2,(0,0,0)).fuse(box(120,2,22,(0,-51.5,10))).fuse(box(120,2,22,(0,51.5,10)))
add('50','Output chute',tray.rotate((0,0,0),(0,1,0),25).translate((532,170,174)),'SS304, 1.2–2 mm','Output','Open chute with sidewalls. Removable silicone liner softens drop. Ball exit/release needs sticky-mixture testing; no simulated adhesion model.')
add('51','Collection tray',box(110,150,2,(540,170,74)).fuse(box(110,2,15,(540,96,82))).fuse(box(110,2,15,(540,244,82))),'SS304','Output','Lift-out tray. Stop on tray-full sensor. No collection reach into moving cup; front interlocked cover.')
add('60','Front lift-off guard',box(584,3,430,(300,65,280)),'Clear polycarbonate, 3 mm','Guarding','Interlocked clear guard; concept panel, not a validated reach barrier. Hinges/latches and complete side guards required before powered operation.')
add('61','User interface enclosure',box(130,36,65,(115,62,107)),'ABS PC dry enclosure','Electrical','30 / 50 / 100 g presets; recipe, density, tare, jog, cleaning lockout. Splash-resistant membrane controls.')
add('62','Emergency stop',cyl(17,18,(0,0,0)).rotate((0,0,0),(1,0,0),90).translate((213,47,110)),'Red polymer + electrical switch','Electrical','Latching E-stop through safety relay cuts drive enable/power. Independent manual reset; no automatic restart. Exact safety circuit requires electrical engineering review.')
add('63','24 V power supply',box(180,55,42,(170,344,122)),'Enclosed AC/DC supply','Electrical','230 VAC 50 Hz input, 24 V 10 A / 240 W output. Target ≥20% electrical reserve. Earthed metal chassis, fused inlet, segregated mains. No heater or compressor.')
add('64','Control and safety module',box(150,60,45,(390,345,120)),'FR4 PCB + DIN rail modules','Electrical','Controller, ADC, servo drivers and monitored safety relay. Shown as procurement envelope; schematic and cable schedule in design document.')

assembly=cq.Assembly(name='LaddooMaker_Rev_B_concept')
data=[]
for p in parts:
    shape=p['shape']; assembly.add(shape,name=p['id']+'_'+p['name'].replace(' ','_').replace('Ø','D'))
    cq.exporters.export(shape,str(OUT/(p['id']+'.step')))
    v,t=shape.tessellate(.7)
    data.append({k:val for k,val in p.items() if k!='shape'} | {'vertices':[round(c,3) for q in v for c in (q.x,q.y,q.z)],'triangles':[i for tr in t for i in tr]})
assembly.save(str(OUT/'MACHINE_REV_B.step'))
(OUT/'parts.js').write_text('window.PARTS='+json.dumps(data,separators=(',',':'))+';',encoding='utf-8')
with (OUT/'BOM.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f);w.writerow(['ID','Part','Material','Group','Envelope mm','Specification'])
    for p in parts:w.writerow([p['id'],p['name'],p['material'],p['group'],' x '.join(map(str,p['dimensions'])),p['info']])
shutil.copyfile(ROOT.parent/'exports/assembly_film/three.min.js',OUT/'three.min.js')
shutil.copyfile(ROOT.parent/'exports/assembly_film/THREE_LICENSE.txt',OUT/'THREE_LICENSE.txt')
cup_meshes={}
for d in range(36,65,2):
    pair=[]
    for upper,at in [(False,(270,170,225)),(True,(430,170,320))]:
        shape=cup(d,upper).translate(at)
        cq.exporters.export(shape,str(OUT/f'C{d}_{"upper" if upper else "lower"}.step'))
        v,t=shape.tessellate(.4)
        pair.append({'vertices':[round(c,3) for q in v for c in (q.x,q.y,q.z)],'triangles':[i for tr in t for i in tr]})
    spacer=cyl(12,35-d/2,(430,170,325+d/2))
    cq.exporters.export(spacer,str(OUT/f'C{d}_spacer.step'))
    v,t=spacer.tessellate(.4)
    pair.append({'vertices':[round(c,3) for q in v for c in (q.x,q.y,q.z)],'triangles':[i for tr in t for i in tr]})
    cup_meshes[d]=pair
(OUT/'cups.js').write_text('window.CUPS='+json.dumps(cup_meshes,separators=(',',':'))+';',encoding='utf-8')

# Real CAD intersections of all mould pairs over head travel, not a food model.
checks=[]
for d in range(36,65,2):
    lo=cup(d)
    maximum=0
    for dz in [0,.5,1,5,20,50,95]: maximum=max(maximum,lo.intersect(cup(d,True).translate((0,0,dz))).Volume())
    sphere=cq.Workplane('XY').sphere(d/2).val()
    support=box(16,16,54,(0,69,-30))
    spacer=cyl(12,35-d/2,(0,0,5+d/2))
    intrusion=sphere.intersect(support).Volume()+sphere.intersect(spacer).Volume()
    checks.append({'diameter_mm':d,'max_rigid_insert_overlap_mm3':maximum,'support_food_intrusion_mm3':intrusion,'pass':maximum<1e-6 and intrusion<1e-6})
diameters=[{'mass_g':m,'density_g_cm3':rho,'diameter_mm':round(10*(6*m/(math.pi*rho))**(1/3),2)} for m in [30,50,100] for rho in [.8,1,1.2]]
# Coarse feed finishes 5g short, then 2 g/s fine feed, assumed 4 s form.
timing=[]
for m in [30,50,100]:
    seconds=(m-5)/20+5/2+.8+1.2+1.2+2.375+4+2.375+1.2+1.2
    timing.append({'mass_g':m,'seconds':round(seconds,3),'pieces_min':round(60/seconds,3),'assumed_not_measured':True})
report={'status':'Concept engineering screens only; no physical validation or food rheology simulation',
 'cad_parts':len(parts),'cup_clearance':checks,'diameters':diameters,'timing':timing,
 'press':{'force_N':150,'lead_mm':4,'efficiency_assumed':.35,'required_screw_torque_Nm':150*.004/(2*math.pi*.35),'speed_mm_s':40,'mechanical_input_W':150*.04/.35,'motor_budget_W':50},
 'feed':{'assumed_belt_force_N':20,'roller_radius_m':.01,'service_factor':2,'required_output_torque_Nm':.4,'specified_continuous_Nm':1},
 'shuttle':{'assumed_moving_mass_kg':1.5,'acceleration_m_s2':.5,'friction_N':8,'pulley_radius_m':.00955,'service_factor':2,'required_torque_Nm':2*(1.5*.5+8)*.00955,'specified_at_speed_Nm':.3},
 'electrical':{'actuators_plus_controls_W':195,'supply_W':240,'reserve_fraction':45/240},
 'not_tested':['Food cohesion, adhesion, density or peanut crushing','Dose accuracy and hopper bridging','Full machine collision sweep, supports and cable clearances','FEA, fatigue, thermal and electrical compliance','Physical output, cleaning, reliability']}
(OUT/'SIMULATION.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='cup_clearance'},indent=2),flush=True)
print('Cup pairs:',sum(p['pass'] for p in checks),'/',len(checks),flush=True)
assert all(p['pass'] for p in checks)
# Avoid Windows OCCT finalizer crash after successful export; files are closed above.
import os
os._exit(0)
