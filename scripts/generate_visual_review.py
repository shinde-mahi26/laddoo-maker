from pathlib import Path
import os,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
import cadquery as cq
from laddoomaker.model import build_machine,build_subassemblies
from laddoomaker.parameters.motion_states import State
OUT=ROOT/"exports"/"svg"; OUT.mkdir(parents=True,exist_ok=True)
def comp(keys,state=State.S0_HOME,angle=None):
    s=build_subassemblies(state,angle); return cq.Compound.makeCompound([s[k].toCompound() for k in keys])
def ex(name,shape,d=(1,-1,1)):
    cq.exporters.export(shape,str(OUT/f"REV_A1_{name}.svg"),opt={"projectionDir":d,"showAxes":False,"width":1200,"height":900,"marginLeft":40,"marginTop":40})
keys=[f"A{i:02}" for i in range(1,11)]; whole=build_machine().toCompound()
ex("01_complete_isometric",whole); ex("02_enclosure_review",comp(["A01","A02","A09","A10"]),(1,-1,1))
ex("03_section_X215",whole.intersect(cq.Workplane("XY").box(2,600,850,centered=(True,True,False)).translate((215,145,0)).val()),(1,0,0))
ex("04_section_Y115",whole.intersect(cq.Workplane("XY").box(500,2,850,centered=(True,True,False)).translate((215,115,0)).val()),(0,1,0))
ex("05_section_Y205",whole.intersect(cq.Workplane("XY").box(500,2,850,centered=(True,True,False)).translate((215,205,0)).val()),(0,1,0))
ex("06_S0_HOME",build_machine(State.S0_HOME).toCompound()); ex("07_S1_LOADING",build_machine(State.S1_LOADING).toCompound())
for i,a in enumerate((0,90,180,270),8): ex(f"{i:02}_S2_FORMING_{a:03}",build_machine(State.S2_FORMING,a).toCompound())
ex("12_S3_EJECTION",build_machine(State.S3_EJECTION).toCompound()); ex("13_S4_HOPPER_SERVICE",build_machine(State.S4_HOPPER_SERVICE).toCompound())
ex("14_lower_boss_bellows",comp(["A01","A07"]),(1,-1,0.5)); ex("15_belt_pulley",build_subassemblies()["A07"].toCompound(),(0,0,1))
ex("16_ejector_cartridge",comp(["A07","A09"],State.S3_EJECTION),(1,-1,0.4)); ex("17_feeder_hopper",comp(["A02","A04"]),(1,-1,0.5))
print("Generated 17 Rev-A1 SVG views from actual CAD solids")
sys.stdout.flush(); os._exit(0)
