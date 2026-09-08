from checks.acceptance import cartridge_checks,interference_checks,motion_checks,Result

def test_four_cartridge_sets_and_retraction():
    checks=cartridge_checks(); assert len(checks)==4; assert all(c.result==Result.PASS and "lowest Z=225.00" in c.evidence for c in checks)
def test_orbit_quadrants():
    check=next(c for c in motion_checks() if c.id=="MV03"); assert check.result==Result.PASS; assert "(218,115)" in check.evidence and "(215,112)" in check.evidence
def test_transfer_chute_clearance_is_geometric():
    check=next(c for c in interference_checks() if c.id=="IC01"); assert check.result==Result.PASS
