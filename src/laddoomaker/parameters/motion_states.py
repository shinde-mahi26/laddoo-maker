from dataclasses import dataclass
from enum import Enum
from math import cos, radians, sin
from .global_params import P


class State(str, Enum):
    S0_HOME = "S0_HOME"
    S1_LOADING = "S1_LOADING"
    S2_FORMING = "S2_FORMING"
    S3_EJECTION = "S3_EJECTION"
    S4_HOPPER_SERVICE = "S4_HOPPER_SERVICE"


@dataclass(frozen=True)
class Motion:
    upper_drop: float
    g1_open: bool
    g2_open: bool
    ejector_sweep: float
    orbit_angle: float
    coupling_retract: float = 0
    hopper_lift: float = 0
    hopper_forward: float = 0


MOTIONS = {
    State.S0_HOME: Motion(0, False, False, 0, 0),
    State.S1_LOADING: Motion(0, False, True, 0, 0),
    State.S2_FORMING: Motion(P.UPPER_HEAD_TRAVEL, False, False, 0, 0),
    State.S3_EJECTION: Motion(0, False, False, 105, 0),
    State.S4_HOPPER_SERVICE: Motion(0, False, False, 0, 0, 30, 175, -100),
}


def orbit_xy(angle_degrees: float) -> tuple[float, float]:
    a = radians(angle_degrees)
    return (P.CENTER_X + P.ORBIT_RADIUS * cos(a), P.ROUNDER_Y + P.ORBIT_RADIUS * sin(a))
