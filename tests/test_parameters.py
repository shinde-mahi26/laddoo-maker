from laddoomaker.common.datums import AXES, DATUMS
from laddoomaker.parameters.global_params import P
from laddoomaker.parameters.motion_states import orbit_xy

def test_locked_envelope(): assert (P.WIDTH,P.DEPTH,P.HEIGHT)==(430,380,625)
def test_axes(): assert AXES=={"AX_R":(215,115),"AX_D":(215,205)}
def test_datums(): assert {k:v.value for k,v in DATUMS.items()}=={"A":35,"B":215,"C":0,"D":115,"E":205,"F":250}
def test_orbit(): assert orbit_xy(0)==(218,115); assert orbit_xy(90)==(215,118)
def test_locked_verticals(): assert (P.BALL_CENTER_Z,P.ROUNDER_DECK_Z,P.UPPER_HEAD_TRAVEL)==(178,120,55)
