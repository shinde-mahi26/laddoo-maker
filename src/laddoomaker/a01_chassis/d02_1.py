"""D02.1 lightweighting study and the approved LW2 production candidate."""
from dataclasses import dataclass
import cadquery as cq
from laddoomaker.a01_chassis.d02 import build_parts as baseline_parts,box,cyl,ring
from laddoomaker.common.geometry import color

DENSITY={"SS304":8.0e-6,"AL5052":2.68e-6,"AL6061":2.70e-6,"PC":1.20e-6}

@dataclass(frozen=True)
class Candidate:
    code:str; base_t:float; spine_t:float; panel_t:float; rear_t:float; fascia_t:float; cframe_t:float
    dry_material:str; cframe_material:str; strategy:str

CANDIDATES={
 "LW1":Candidate("LW1",1.5,1.2,0.8,0.8,1.0,3.0,"SS304","SS304","all-SS folded sections, dry cut-outs and local 4 mm interface pads"),
 "LW2":Candidate("LW2",1.5,1.2,0.8,0.8,1.0,3.0,"AL5052","SS304","SS wet barrier/C-frame plus isolated aluminium dry skins and spine"),
 "LW3":Candidate("LW3",1.2,1.0,0.8,0.8,0.8,2.0,"AL5052","SS304","minimum-mass folded SS channels with local 4 mm datum pads"),
}

def _base(t):
    floor=box(0,0,35,430,380,t)
    fl=box(0,0,35+t,t,380,28).union(box(430-t,0,35+t,t,380,28)).union(box(t,0,35+t,430-2*t,t,28)).union(box(t,380-t,35+t,430-2*t,t,28))
    # Three shallow dry-side ribs plus local accepted pads resist oil-canning.
    ribs=box(70,80,35+t,290,t,12).union(box(70,190,35+t,290,t,12)).union(box(70,300,35+t,290,t,12))
    return floor.union(fl).union(ribs)
def _spine(t): return box(35,365,37,360,t,588).union(box(35,345,37,t,20,588)).union(box(395-t,345,37,t,20,588))
def _panel(left,t):
    x=0 if left else 430-t; retx=t if left else 415
    return box(x,0,35,t,380,590).union(box(retx,0,35,15-t,t,590)).union(box(retx,380-t,35,15-t,t,590))
def _rear(t): return box(15,380-t,50,400,t,560).union(box(15,365,50,t,15,560)).union(box(415-t,365,50,t,15,560))
def _fascia(t): return box(30,15,455,370,t,120).cut(box(40,14,470,130,t+2,90)).cut(cyl(350,14,500,22,t+3))
def _cframe_parts(t,aggressive=False):
    # Windowed side plates; LW3 gains folded 15 mm edge flanges.
    left=box(135,50,35,t,135,330).cut(box(134,70,70,t+2,95,245)); right=box(295-t,50,35,t,135,330).cut(box(294-t,70,70,t+2,95,245))
    cross=box(135+t,50,35,160-2*t,135,t).union(box(135+t,50,349-t,160-2*t,135,t))
    if aggressive:
        left=left.union(box(135+t,50,35,15,t,330)); right=right.union(box(280-t,50,35,15,t,330))
    pads=box(135,85,140,4,60,70).union(box(291,85,140,4,60,70))
    return left,right,cross,pads

def _cframe(t,aggressive=False):
    left,right,cross,pads=_cframe_parts(t,aggressive)
    return left.union(right).union(cross).union(pads)

def build_candidate_parts(code):
    c=CANDIDATES[code]; b=baseline_parts(); p={}
    p["A01-001"]=(_base(c.base_t),"SS304","STRUCTURAL")
    p["A01-002"]=(_spine(c.spine_t),c.dry_material,"STRUCTURAL")
    for key in ("A01-003_sanitary_partition","A01-004_food_deck","A01-004R_deck_ring"):
        p[key.split("_")[0]]=(b[key],"SS304","FOOD/WET BARRIER")
    p["A01-005"]=(_panel(True,c.panel_t),c.dry_material,"COSMETIC PANEL"); p["A01-006"]=(_panel(False,c.panel_t),c.dry_material,"COSMETIC PANEL")
    p["A01-007"]=(_rear(c.rear_t),c.dry_material,"SERVICE PANEL")
    p["A01-008"]=(b["A01-008_front_door_frame"],c.dry_material,"SERVICE PANEL"); p["A01-008P"]=(b["A01-008P_inspection_panel"],"PC","SERVICE PANEL")
    p["A01-009"]=(_cframe(c.cframe_t,code=="LW3"),c.cframe_material,"STRUCTURAL")
    for key in ("A01-010_reinforcement_set","A01-011_feet_set","A01-012_panel_hardware","A01-013_structural_fasteners"):
        p[key.split("_")[0]]=(b[key],"SS304","HARDWARE" if "011" in key or "012" in key or "013" in key else "REINFORCEMENT")
    p["A01-014"]=(_fascia(c.fascia_t),c.dry_material,"SERVICE PANEL")
    for key in ("A01-015_A03_adapter","A01-016_A04_adapter","A01-017_gland_plate"):
        p[key.split("_")[0]]=(b[key],c.dry_material,"REINFORCEMENT")
    return p

def build_candidate(code):
    a=cq.Assembly(name=f"A01-{code}_D02_1_STUDY")
    for pid,(shape,material,_) in build_candidate_parts(code).items(): a.add(shape,name=f"{code}-{pid}",color=color("steel" if material=="SS304" else "dry"))
    return a

ACTIVE_CANDIDATE="LW2"

def build_approved_a01():
    """Build approved LW2 with the canonical A01 names used by D01/D02 checks."""
    c=CANDIDATES[ACTIVE_CANDIDATE]; p=build_candidate_parts(ACTIVE_CANDIDATE)
    names={
      "A01-001":"A01-001_base_pan","A01-002":"A01-002_rear_spine",
      "A01-003":"A01-003_sanitary_partition","A01-004":"A01-004_food_deck",
      "A01-004R":"A01-004R_deck_ring","A01-005":"A01-005_left_enclosure",
      "A01-006":"A01-006_right_enclosure","A01-007":"A01-007_rear_cover",
      "A01-008":"A01-008_front_door_frame","A01-008P":"A01-008P_inspection_panel",
      "A01-010":"A01-010_reinforcement_set","A01-011":"A01-011_feet_set",
      "A01-012":"A01-012_panel_hardware","A01-013":"A01-013_structural_fasteners",
      "A01-014":"A01-014_fascia_carrier","A01-015":"A01-015_A03_adapter",
      "A01-016":"A01-016_A04_adapter","A01-017":"A01-017_gland_plate",
    }
    a=cq.Assembly(name="A01_CHASSIS_D02_1_LW2_APPROVED")
    for pid,(shape,material,_) in p.items():
        if pid=="A01-009": continue
        shade="steel" if material=="SS304" else ("polymer" if material=="PC" else "dry")
        a.add(shape,name=names[pid],color=color(shade))
    left,right,cross,pads=_cframe_parts(c.cframe_t)
    a.add(left,name="A01-009_cframe_left",color=color("steel"))
    a.add(right,name="A01-009_cframe_right",color=color("steel"))
    a.add(cross.union(pads),name="A01-009_cframe_crossmembers",color=color("steel"))
    return a

def candidate_masses(code):
    out={}
    for pid,(shape,material,category) in build_candidate_parts(code).items(): out[pid]={"mass_kg":shape.val().Volume()*DENSITY[material],"material":material,"category":category,"volume_mm3":shape.val().Volume()}
    # Purchased hardware masses are better represented by accepted BOM estimates.
    out["A01-011"]["mass_kg"]=0.80; out["A01-012"]["mass_kg"]=0.25; out["A01-013"]["mass_kg"]=0.18
    return out
