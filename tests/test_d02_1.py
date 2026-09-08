from checks.d02_1 import candidate_checks
from checks.acceptance import Result
from laddoomaker.a01_chassis.d02 import build_a01 as build_baseline_a01
from laddoomaker.a01_chassis.d02_1 import CANDIDATES,ACTIVE_CANDIDATE,build_approved_a01,candidate_masses
from laddoomaker.model import build_subassemblies

def test_candidates_isolated_and_clear():
    for code in CANDIDATES: assert all(c.result==Result.PASS for c in candidate_checks(code))
def test_candidate_mass_order():
    masses={c:sum(v["mass_kg"] for v in candidate_masses(c).values()) for c in CANDIDATES}
    assert masses["LW2"]<15 and masses["LW3"]<15 and masses["LW1"]<20

def test_lw2_is_active_and_baseline_remains_available():
    assert ACTIVE_CANDIDATE=="LW2"
    active=build_subassemblies()["A01"]
    assert active.name=="A01_CHASSIS_D02_1_LW2_APPROVED"
    assert "A01-009_cframe_left" in active.objects
    assert build_approved_a01().toCompound().Volume()<build_baseline_a01().toCompound().Volume()
