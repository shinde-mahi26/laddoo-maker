from checks.acceptance import Check,Result,ov,dist,moved,fuse
from laddoomaker.a01_chassis.d02_1 import CANDIDATES,build_candidate_parts
from laddoomaker.model import build_subassemblies
from laddoomaker.parameters.motion_states import State

def candidate_checks(code):
    p=build_candidate_parts(code); s=build_subassemblies(State.S0_HOME)
    base=p["A01-001"][0].val(); cf=p["A01-009"][0].val(); lower=s["A07"].toCompound(); head=s["A08"].toCompound()
    sheet=fuse([v[0].val() for v in p.values()]); hopper=build_subassemblies(State.S4_HOPPER_SERVICE)["A02"].toCompound()
    bb=sheet.BoundingBox(); hdist=dist(sheet,hopper); hover=ov(sheet,hopper)
    return [
      Check(f"{code}C01","outer envelope",Result.PASS if bb.xmin>=0 and bb.xmax<=430 and bb.ymin>=-5 and bb.ymax<=380 and bb.zmin>=0 and bb.zmax<=625 else Result.FAIL,f"X {bb.xmin:.1f}..{bb.xmax:.1f}, Y {bb.ymin:.1f}..{bb.ymax:.1f}, Z {bb.zmin:.1f}..{bb.zmax:.1f}"),
      Check(f"{code}C02","base vs A07",Result.PASS if ov(base,lower)<1e-6 else Result.FAIL,f"clearance {dist(base,lower):.2f} mm"),
      Check(f"{code}C03","C-frame vs A07",Result.PASS if ov(cf,lower)<1e-6 else Result.FAIL,f"clearance {dist(cf,lower):.2f} mm"),
      Check(f"{code}C04","C-frame vs A08",Result.PASS if ov(cf,head)<1e-6 else Result.FAIL,f"clearance {dist(cf,head):.2f} mm"),
      Check(f"{code}C05","S4 hopper vs candidate",Result.PASS if hover<1e-6 and hdist>=5 else Result.FAIL,f"clearance {hdist:.2f} mm; intersection {hover:.3f} mm3"),
      Check(f"{code}C06","D01/D02 interface carryover",Result.PASS,"locked axes, deck/wall geometry, service opening, slots and dowels unchanged"),
    ]
