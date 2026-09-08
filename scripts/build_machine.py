from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
from laddoomaker.model import build_machine
from laddoomaker.parameters.motion_states import State

for folder in ("step","stl","gltf","svg","preview"):
    (ROOT/"exports"/folder).mkdir(parents=True,exist_ok=True)
machine=build_machine(State.S0_HOME)
print(f"Built {machine.name} with A01-A10 hierarchy")
