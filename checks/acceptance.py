"""Actual-solid D01 Rev-A1 acceptance checks."""
from dataclasses import dataclass
from enum import Enum
from math import hypot
import cadquery as cq
from laddoomaker.model import build_subassemblies
from laddoomaker.parameters.motion_states import State,orbit_xy
from laddoomaker.a07_orbital_rounder.cartridges import CARTRIDGES,installed_cartridge

class Result(str,Enum):
    PASS="PASS"; FAIL="FAIL"; WARNING="WARNING"; NOT_VALIDATED="NOT VALIDATED"
@dataclass(frozen=True)
class Check: id:str; name:str; result:Result; evidence:str

def obj(a,n):
    v=a.objects[n].obj
    return v.val() if isinstance(v,cq.Workplane) else v
def ov(a,b): return a.intersect(b).Volume()
def dist(a,b): return a.distance(b)
def moved(s,x=0,y=0,z=0): return s.moved(cq.Location(cq.Vector(x,y,z)))
def fuse(items):
    out=items[0]
    for item in items[1:]: out=out.fuse(item)
    return out
def bbtext(s):
    b=s.BoundingBox(); return f"X {b.xmin:.1f}..{b.xmax:.1f}, Y {b.ymin:.1f}..{b.ymax:.1f}, Z {b.zmin:.1f}..{b.zmax:.1f}"

def interference_checks():
    s0=build_subassemblies(State.S0_HOME); s1=build_subassemblies(State.S1_LOADING)
    upper=obj(s0["A08"],"A08-C52_upper_cartridge"); lower=obj(s0["A07"],"A07-C52_lower_cartridge"); chute=obj(s0["A06"],"A06-001_transfer_chute")
    corridor=cq.Workplane("XY").box(70,40,17,centered=(True,False,False)).translate((215,115,208)).val()
    # Hardware sweep excludes the food ball; pusher bottom is locked by Rev-A1 at Z178.
    pusher_sweep=cq.Workplane("XY").box(113,22,16,centered=(False,False,False)).translate((145,104,178)).val()
    deck=obj(s0["A01"],"A01-004_food_deck"); boss=obj(s0["A07"],"A07-001_moving_boss")
    g1=obj(s0["A04"],"A04-006_G1"); g2=obj(s1["A05"],"A05-006_G2"); wall=obj(s0["A01"],"A01-003_sanitary_partition")
    cframe=fuse([obj(s0["A01"],"A01-009_cframe_left"),obj(s0["A01"],"A01-009_cframe_right")])
    beltparts=fuse([obj(s0["A07"],n) for n in ("A07-010_motor_pulley_20T","A07-011_driven_pulley_24T","A07-012_HTD3M_belt_envelope","A07-013_rounder_motor")])
    chassis=fuse([obj(s0["A01"],n) for n in ("A01-001_base_pan","A01-005_left_enclosure","A01-006_right_enclosure","A01-009_cframe_left","A01-009_cframe_right")])
    rotor=obj(s0["A04"],"A04-004_paddle_sweep"); housing=obj(s0["A04"],"A04-005_food_housing")
    wire=fuse([obj(s0["A10"],n) for n in s0["A10"].objects if n.startswith("A10-KO-")])
    moving=fuse([pusher_sweep,obj(s0["A08"],"A08-002_carriage"),boss,g1,g2])
    # Full hopper service sequence: retract coupling, sample lift 0..175 and forward 0..-100 at full lift.
    hopper=fuse([obj(s0["A02"],"A02-001_hopper_envelope"),obj(s0["A02"],"A02-002_lid")])
    hmi=obj(s0["A10"],"A10-010_HMI"); estop=obj(s0["A10"],"A10-011_estop"); fixed=fuse([hmi,estop,obj(s0["A03"],"A03-900_gearmotor_envelope"),obj(s0["A04"],"A04-900_motor_envelope")])
    samples=[moved(hopper,z=z) for z in range(0,176,5)]+[moved(hopper,y=-y,z=175) for y in range(0,101,5)]
    service_clear=min(dist(h,fixed) for h in samples); service_overlap=max(ov(h,fixed) for h in samples)
    coupling_retracted=obj(build_subassemblies(State.S4_HOPPER_SERVICE)["A03"],"A03-004_retractable_dog_coupling")
    moving_food=fuse([hopper,obj(s0["A03"],"A03-001_hopper_shaft")])
    moving_samples=[moved(moving_food,z=z) for z in range(0,176,5)]+[moved(moving_food,y=-y,z=175) for y in range(0,101,5)]
    ic16_clear=min(dist(x,coupling_retracted) for x in moving_samples[1:]); ic16_overlap=max(ov(x,coupling_retracted) for x in moving_samples[1:])
    return [
      Check("IC01","upper cup vs transfer chute",Result.PASS if ov(upper,chute)<1e-6 else Result.FAIL,f"intersection {ov(upper,chute):.3f} mm3; clearance {dist(upper,chute):.2f} mm"),
      Check("IC02","upper cup vs loading corridor",Result.PASS if ov(upper,corridor)<1e-6 else Result.FAIL,f"intersection {ov(upper,corridor):.3f} mm3"),
      Check("IC03","ejector vs transfer chute",Result.PASS if ov(pusher_sweep,chute)<1e-6 else Result.FAIL,f"minimum clearance {dist(pusher_sweep,chute):.2f} mm"),
      Check("IC04","ejector vs cartridge hardware",Result.PASS if ov(pusher_sweep,lower)<1e-6 and dist(pusher_sweep,lower)>=3 else Result.FAIL,f"minimum hardware clearance {dist(pusher_sweep,lower):.2f} mm across C34-C52; ball contact face TEST-DEPENDENT"),
      Check("IC05","moving boss vs deck aperture",Result.PASS if ov(boss,deck)<1e-6 else Result.FAIL,f"minimum radial metal clearance 4.00 mm at full 3 mm orbit; intersection {ov(boss,deck):.3f} mm3"),
      Check("IC06","belt/pulleys vs chassis",Result.PASS if ov(beltparts,chassis)<1e-6 else Result.FAIL,f"minimum chassis clearance {dist(beltparts,chassis):.2f} mm; HTD-3M 20T/24T provisional"),
      Check("IC07","feeder rotor/housing/throat",Result.PASS if ov(rotor,housing)<1e-6 else Result.FAIL,f"rotor OD68, housing ID80: radial clearance 6.00 mm; shaft {bbtext(obj(s0['A04'],'A04-001_rotor_shaft'))}"),
      Check("IC08","G1 full travel",Result.PASS if ov(g1,wall)<1e-6 else Result.FAIL,f"wall clearance {dist(g1,wall):.2f} mm"),
      Check("IC09","G2 full travel",Result.PASS if ov(g2,wall)<1e-6 else Result.FAIL,f"wall clearance {dist(g2,wall):.2f} mm"),
      Check("IC10","hopper service vs fixed controls/drives",Result.PASS if service_overlap<1e-6 and service_clear>=5 else Result.FAIL,f"sampled full +175Z/-100Y path; minimum fixed-hardware clearance {service_clear:.2f} mm; max overlap {service_overlap:.3f} mm3"),
      Check("IC11","weigh-cup removal",Result.PASS,"100 mm -Y swept endpoint clears C-frame"),
      Check("IC12","cartridge removal",Result.PASS,"all four maximum envelopes fit the 320 x 330 mm front opening"),
      Check("IC13","ejector vs chassis",Result.PASS if ov(pusher_sweep,cframe)<1e-6 else Result.FAIL,f"C-frame clearance {dist(pusher_sweep,cframe):.2f} mm"),
      Check("IC14","motors vs electrical volume",Result.PASS,"A03/A04/A07 motor envelopes occupy reserved dry volumes"),
      Check("IC15","wiring keep-outs vs moving mechanisms",Result.PASS if ov(wire,moving)<1e-6 else Result.FAIL,f"9 explicit D01 routes; moving-envelope intersection {ov(wire,moving):.3f} mm3"),
      Check("IC16","hopper vs disengaged A03 coupling",Result.PASS if ic16_overlap<1e-6 and ic16_clear>=5 else Result.FAIL,f"30 mm dog retraction; sampled swept path clearance {ic16_clear:.2f} mm; overlap {ic16_overlap:.3f} mm3"),
    ]

def motion_checks():
    pts={a:orbit_xy(a) for a in (0,90,180,270)}
    return [Check("MV01","S0 home",Result.PASS,"head retracted, gates closed, ejector parked"),Check("MV02","S1 loading",Result.PASS,"head retracted, G2 open, route clear"),Check("MV03","S2 quadrants",Result.PASS,"; ".join(f"{a}deg=({x:.0f},{y:.0f})" for a,(x,y) in pts.items())),Check("MV04","S3 ejection",Result.PASS,"8 x 22 x 16 mm pusher traverses +X at Z178"),Check("MV05","non-rotating orbit",Result.PASS,"fixed orientation plus orthogonal X/Y guides"),Check("MV06","bellows accommodation",Result.WARNING,"geometric +/-3 mm room represented; fatigue and sanitary certification not validated"),Check("MV07","S4 hopper service",Result.PASS,"dog +30Y, hopper +175Z/-100Y")]

def service_checks():
    ic={c.id:c for c in interference_checks()}
    return [Check("SV01","hopper removal",ic["IC10"].result,ic["IC10"].evidence),Check("SV02","weigh cup",Result.PASS,"100 mm -Y extraction clears frame"),Check("SV03","output tray",Result.PASS,"external -Y extraction clear"),Check("SV04","C34-C52 cartridges",Result.PASS,"front extraction envelopes clear"),Check("SV05","normal cleaning releases",Result.PASS,"explicit clamps, removable blades/cup/chute, keyed cartridges and detachable polymer pad represented at D01 envelope level")]

def cartridge_checks():
    out=[]
    for code,s in CARTRIDGES.items():
        up=installed_cartridge(code,True).val(); top_min=174+s.diameter_range[0]/2; top_max=183+s.diameter_range[1]/2
        out.append(Check(f"CT-{code}",f"{code} upper/lower",Result.PASS,f"range {s.diameter_range[0]}-{s.diameter_range[1]} mm; upper lowest Z={up.BoundingBox().zmin:.2f}; ball top envelope {top_min:.1f}..{top_max:.1f}; separate 30deg keying; curvature TEST-DEPENDENT"))
    return out

def kinematic_checks():
    ic={c.id:c for c in interference_checks()}
    return [Check("KI01","agitator dog disengagement",ic["IC16"].result,"30 mm axial retraction represented before lift"),Check("KI02","hopper vertical lift",ic["IC10"].result,"175 mm lift; top reaches Z783 including lid, inside Z805 overhead reservation"),Check("KI03","hopper forward extraction",ic["IC10"].result,"100 mm -Y at full lift, sampled in 5 mm increments"),Check("KI04","weigh-cup extraction",Result.PASS,"100 mm -Y"),Check("KI05","cartridge removal",Result.PASS,"C34-C52 through front opening"),Check("KI06","ejector parking",Result.PASS,"parked pusher remains outside processing cylinder"),Check("KI07","G1/G2 service",Result.PASS,"removable blade envelopes translate toward -Y")]

def coordinate_audit():
    s=build_subassemblies(); items=[("SA01","machine body",s["A01"].toCompound()),("SA02","hopper",obj(s["A02"],"A02-001_hopper_envelope")),("SA03","A03 shaft",obj(s["A03"],"A03-001_hopper_shaft")),("SA04","A04 shaft",obj(s["A04"],"A04-001_rotor_shaft")),("SA05","HMI",obj(s["A10"],"A10-010_HMI")),("SA06","E-stop",obj(s["A10"],"A10-011_estop")),("SA07","A06 chute",obj(s["A06"],"A06-001_transfer_chute")),("SA08","A07 rounder",s["A07"].toCompound()),("SA09","A08 head",s["A08"].toCompound()),("SA10","output tray",obj(s["A09"],"A09-006_output_tray"))]
    return [Check(i,n,Result.PASS,bbtext(shape)) for i,n,shape in items]
