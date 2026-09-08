from checks.acceptance import interference_checks,kinematic_checks,coordinate_audit,Result

def test_rev_a1_mandatory_interferences_pass():
    required={"IC04","IC05","IC06","IC07","IC10","IC15","IC16"}
    checks={c.id:c for c in interference_checks()}
    assert all(checks[i].result==Result.PASS for i in required)
def test_a03_a04_coordinates():
    checks={c.name:c for c in coordinate_audit()}
    assert "Y 125.0..245.0" in checks["A03 shaft"].evidence
    assert "Y 170.0..240.0" in checks["A04 shaft"].evidence
def test_service_kinematics_pass(): assert all(c.result==Result.PASS for c in kinematic_checks())
