"""D02 prototype-manufacturable A01 chassis geometry.

Geometry is a fabrication candidate for laser cut, press brake and TIG review.
Flat-pattern bend compensation remains preliminary until fabricator feedback.
"""
from dataclasses import dataclass
import cadquery as cq
from laddoomaker.common.geometry import color

DENSITY_KG_MM3=8.0e-6
BEND_RADIUS=2.0
K_FACTOR=0.42
STATUS="D02 DETAIL DESIGN - DFM REVIEW"

def box(x,y,z,dx,dy,dz): return cq.Workplane("XY").box(dx,dy,dz,centered=(False,False,False)).translate((x,y,z))
def cyl(x,y,z,r,h): return cq.Workplane("XY").circle(r).extrude(h).translate((x,y,z))
def ring(x,y,z,ro,ri,h): return cyl(x,y,z,ro,h).cut(cyl(x,y,z-1,ri,h+2))

@dataclass(frozen=True)
class PartRecord:
    part_id:str; description:str; quantity:int; material:str; thickness:float
    process:str; blank:str; make_or_buy:str="MAKE"; finish:str="SS304 2B, deburr/passivate as noted"; classification:str="PROTOTYPE_RELEASE_CANDIDATE"

PART_RECORDS=(
 PartRecord("A01-001","Folded base pan",1,"SS304",2.0,"laser cut + press brake + TIG corner closeout","486 x 436"),
 PartRecord("A01-002","Folded rear structural spine",1,"SS304",1.5,"laser cut + press brake","430 x 650"),
 PartRecord("A01-003","Sanitary partition with dry-side returns",1,"SS304",1.2,"laser cut + press brake + continuous wet TIG","400 x 440"),
 PartRecord("A01-004","Rounder sanitary deck",1,"SS304",1.5,"laser cut + press brake + continuous wet TIG","400 x 290"),
 PartRecord("A01-005","Left removable panel",1,"SS304",1.0,"laser cut + press brake","420 x 625"),
 PartRecord("A01-006","Right removable panel",1,"SS304",1.0,"laser cut + press brake","420 x 625"),
 PartRecord("A01-007","Rear service cover",1,"SS304",1.0,"laser cut + press brake","410 x 580"),
 PartRecord("A01-008","Front service door/frame",1,"SS304+PC",1.0,"laser cut + press brake + hinge assembly","390 x 380"),
 PartRecord("A01-009","Rounder C-frame weldment plates/crossmembers",1,"SS304",4.0,"laser cut + fixture TIG + finish machine","2x 160 x 350 + crossmembers"),
 PartRecord("A01-010","Reinforcement pad set",1,"SS304",2.0,"laser cut + TIG","mixed"),
 PartRecord("A01-011","M8 feet/captive nut set",1,"SS304",3.0,"buy feet + laser pads + TIG nuts","4x 55 x 55"),
 PartRecord("A01-012","Captive panel hardware set",1,"SS",0,"BUY","n/a","BUY"),
 PartRecord("A01-013","Structural fastener/dowel set",1,"SS",0,"BUY","n/a","BUY"),
 PartRecord("A01-014","Removable control fascia carrier",1,"SS304",1.5,"laser cut + press brake","360 x 150"),
 PartRecord("A01-015","A03 removable drive adapter carrier",1,"SS304",3.0,"laser cut + slots","110 x 100"),
 PartRecord("A01-016","A04 removable drive adapter carrier",1,"SS304",3.0,"laser cut + slots","130 x 110"),
 PartRecord("A01-017","Removable cable gland interface plate",1,"SS304",2.0,"laser cut + provisional pilot holes","120 x 80"),
)

def build_parts():
    p={}
    # One-piece base floor with 28 mm upturned flanges (simplified folded solids).
    floor=box(0,0,35,430,380,2)
    flanges=box(0,0,37,2,380,28).union(box(428,0,37,2,380,28)).union(box(2,0,37,426,2,28)).union(box(2,378,37,426,2,28))
    p["A01-001_base_pan"]=floor.union(flanges)
    # Rear hat/spine: rear web plus forward returns in dry zone.
    p["A01-002_rear_spine"]=box(35,365,37,360,1.5,588).union(box(35,345,37,1.5,20,588)).union(box(393.5,345,37,1.5,20,588))
    wall=box(35,250,120,360,1.2,400).union(box(35,251.2,120,1.2,18,400)).union(box(393.8,251.2,120,1.2,18,400))
    p["A01-003_sanitary_partition"]=wall
    deck=box(35,0,120,360,250,1.5).cut(cyl(215,115,115,26,15))
    deck=deck.union(box(35,0,105,1.5,250,15)).union(box(393.5,0,105,1.5,250,15)).union(box(35,0,105,360,1.5,15))
    p["A01-004_food_deck"]=deck
    p["A01-004R_deck_ring"]=ring(215,115,116,36,26,4)
    p["A01-005_left_enclosure"]=box(0,0,35,1,380,590).union(box(1,0,35,14,1,590)).union(box(1,379,35,14,1,590))
    p["A01-006_right_enclosure"]=box(429,0,35,1,380,590).union(box(415,0,35,14,1,590)).union(box(415,379,35,14,1,590))
    # Rear cover with dry-side returns and ventilation placeholders.
    p["A01-007_rear_cover"]=box(15,379,50,400,1,560).union(box(15,365,50,1,14,560)).union(box(414,365,50,1,14,560))
    # Front frame preserves exact X55..375 / Z115..445 clear opening.
    frame=box(35,0,95,20,1.5,370).union(box(375,0,95,20,1.5,370)).union(box(55,0,95,320,1.5,20)).union(box(55,0,445,320,1.5,20))
    door=box(40,-1,100,350,1,360).cut(box(65,-2,130,300,3,280))
    p["A01-008_front_door_frame"]=frame.union(door)
    p["A01-008P_inspection_panel"]=box(65,-4,130,300,3,280)
    # Two 4 mm windowed side plates and balanced crossmembers.
    left=box(135,50,35,4,135,330).cut(box(134,70,70,6,95,245)); right=box(291,50,35,4,135,330).cut(box(290,70,70,6,95,245))
    p["A01-009_cframe_left"]=left; p["A01-009_cframe_right"]=right
    p["A01-009_cframe_crossmembers"]=box(139,50,35,152,135,4).union(box(139,50,345,152,135,4))
    # Four base pads with 7x14 adjustment slots and two non-collinear dowel holes.
    pads=None
    for x,y in ((155,70),(275,70),(155,170),(275,170)):
        pad=box(x-18,y-18,37,36,36,2).cut(box(x-3.5,y-7,36,7,14,4))
        pads=pad if pads is None else pads.union(pad)
    pads=pads.cut(cyl(170,90,36,3,5)).cut(cyl(260,150,36,3,5))
    p["A01-010_reinforcement_set"]=pads
    feet=None
    for x,y in ((35,35),(395,35),(35,345),(395,345)):
        unit=cyl(x,y,0,20,35).union(box(x-27.5,y-27.5,33,55,55,2))
        feet=unit if feet is None else feet.union(unit)
    p["A01-011_feet_set"]=feet
    p["A01-012_panel_hardware"]=cyl(15,40,200,4,8).union(cyl(415,40,200,4,8))
    p["A01-013_structural_fasteners"]=cyl(155,70,35,3,10).union(cyl(275,70,35,3,10)).union(cyl(155,170,35,3,10)).union(cyl(275,170,35,3,10))
    # Replaceable front carrier; D01 HMI/E-stop positions remain unchanged.
    p["A01-014_fascia_carrier"]=box(30,15,455,370,1.5,120).cut(box(40,14,470,130,4,90)).cut(cyl(350,14,500,22,5))
    p["A01-015_A03_adapter"]=box(160,300,405,110,3,100).cut(cyl(215,299,455,12,5))
    p["A01-016_A04_adapter"]=box(150,300,325,130,3,110).cut(cyl(215,299,375,12,5))
    p["A01-017_gland_plate"]=box(285,251.2,200,120,3,80)
    return p

def build_a01():
    a=cq.Assembly(name="A01_CHASSIS_D02")
    for name,shape in build_parts().items():
        c="polymer" if name.endswith("inspection_panel") else "steel"
        a.add(shape,name=name,color=color(c))
    return a

def mass_properties():
    out={}
    for name,shape in build_parts().items():
        density=1.20e-6 if name=="A01-008P_inspection_panel" else DENSITY_KG_MM3
        out[name]=shape.val().Volume()*density
    out["A01-011_feet_set"]=0.80  # purchased M8 levelling feet + SS reinforcement pads
    out["A01-012_panel_hardware"]=0.25
    out["A01-013_structural_fasteners"]=0.18
    return out

def flat_patterns():
    """Preliminary planar blank candidates, not released cutting data."""
    specs={
      "A01-001":(486,436,2.0),"A01-002":(430,650,1.5),"A01-003":(400,440,1.2),"A01-004":(400,290,1.5),
      "A01-005":(420,625,1.0),"A01-006":(420,625,1.0),"A01-007":(410,580,1.0),"A01-008":(390,380,1.0),
      "A01-009L":(160,350,4.0),"A01-009R":(160,350,4.0),"A01-014":(360,150,1.5),"A01-015":(110,100,3.0),"A01-016":(130,110,3.0),"A01-017":(120,80,2.0)}
    return {k:{"shape":cq.Workplane("XY").rect(w,h).val(),"width":w,"height":h,"thickness":t} for k,(w,h,t) in specs.items()}
