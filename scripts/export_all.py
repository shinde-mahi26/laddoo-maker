from pathlib import Path
import sys
import os,subprocess
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
import cadquery as cq
from laddoomaker.model import build_machine, build_subassemblies
from laddoomaker.parameters.motion_states import State

(ROOT/"exports"/"step").mkdir(parents=True,exist_ok=True)
cq.exporters.export(build_machine(State.S0_HOME).toCompound(), str(ROOT/"exports"/"step"/"LADDOOMAKER_REV_A1.step"))
for name, asm in build_subassemblies().items(): cq.exporters.export(asm.toCompound(), str(ROOT/"exports"/"step"/f"{name}.step"))
for state in State: cq.exporters.export(build_machine(state).toCompound(), str(ROOT/"exports"/"step"/f"{state.value}.step"))
for angle in (0,90,180,270): cq.exporters.export(build_machine(State.S2_FORMING,angle).toCompound(),str(ROOT/"exports"/"step"/f"S2_FORMING_{angle:03}.step"))
subprocess.run([sys.executable,str(ROOT/"scripts"/"export_prototypes.py")],check=True)
subprocess.run([sys.executable,str(ROOT/"scripts"/"generate_visual_review.py")],check=True)
print("Exported Rev-A1 assembly, A01-A10, S0-S4/S2 quadrants, prototype STL, and CAD-derived review files")
sys.stdout.flush()
# OCP 7.9 can fault during Windows interpreter teardown after successful writes.
# A direct clean process exit avoids destructing already-exported native objects.
os._exit(0)
