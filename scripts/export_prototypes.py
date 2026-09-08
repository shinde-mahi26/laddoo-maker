from pathlib import Path
import os,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
import cadquery as cq
from laddoomaker.a07_orbital_rounder.cartridges import CARTRIDGES,build_cartridge

out=ROOT/"exports"/"stl"; out.mkdir(parents=True,exist_ok=True)
for code in CARTRIDGES:
    for upper in (False,True): cq.exporters.export(build_cartridge(code,upper),str(out/f"{code}_{'upper' if upper else 'lower'}.stl"))
for i,width in enumerate((8,10,12),start=1):
    paddle=cq.Workplane("XY").box(35,width,6).edges("|Z").fillet(2)
    cq.exporters.export(paddle,str(out/f"feeder_paddle_variant_{i}.stl"))
pad=cq.Workplane("XY").box(15,30,30).edges().fillet(2)
cq.exporters.export(pad,str(out/"ejector_pad.stl"))
print("Exported C34/C40/C46/C52 upper/lower and development polymer prototypes")
sys.stdout.flush(); os._exit(0)
