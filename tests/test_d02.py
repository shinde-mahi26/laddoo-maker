from checks.d02 import d02_checks
from checks.acceptance import Result
from laddoomaker.a01_chassis.d02 import build_a01,mass_properties,flat_patterns

def test_d02_a01_hierarchy(): assert len(build_a01().objects)>=18
def test_d02_checks(): assert all(c.result==Result.PASS for c in d02_checks())
def test_d02_mass_and_flats(): assert sum(mass_properties().values())>5; assert len(flat_patterns())>=14
