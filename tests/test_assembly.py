from laddoomaker.model import build_machine, build_subassemblies
from laddoomaker.parameters.motion_states import State

def test_subassembly_hierarchy(): assert set(build_subassemblies())=={f"A{i:02}" for i in range(1,11)}
def test_all_states_build():
    for state in State: assert build_machine(state).name.endswith(state.value)

def test_actual_operational_envelope():
    bb=build_machine(State.S0_HOME).toCompound().BoundingBox()
    assert 0 <= bb.xmin <= bb.xmax <= 430
    assert -90 <= bb.ymin <= bb.ymax <= 380
    assert 0 <= bb.zmin <= bb.zmax <= 625
