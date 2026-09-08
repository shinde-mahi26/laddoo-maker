"""Authoritative Rev-A0 parameters, all dimensions in millimetres."""
from dataclasses import dataclass


@dataclass(frozen=True)
class GlobalParams:
    WIDTH: float = 430
    DEPTH: float = 380
    HEIGHT: float = 625
    OUTPUT_Y_MIN: float = -90
    CENTER_X: float = 215
    ROUNDER_Y: float = 115
    DOSER_Y: float = 205
    SANITARY_Y: float = 250
    BALL_CENTER_Z: float = 178
    BALL_CENTER_Z_MIN: float = 174
    BALL_CENTER_Z_MAX: float = 183
    ROUNDER_DECK_Z: float = 120
    LOWER_CARTRIDGE_DATUM_Z: float = 150
    ORBIT_RADIUS: float = 3.0
    UPPER_HEAD_TRAVEL: float = 55
    UPPER_RETRACT_MIN_Z: float = 225
    CHUTE_OUTLET_Y: float = 155
    CHUTE_OUTLET_Z: float = 208
    HOPPER_RIM_Z: float = 600
    HOPPER_THROAT_Z: float = 395
    AGITATOR_AXIS_Z: float = 455
    FEEDER_AXIS_Z: float = 375
    G1_Z: float = 340
    G2_Z: float = 285
    STRUCTURAL_BASE_Z: float = 35


P = GlobalParams()

LOCKED_PARAMETER_NAMES = tuple(GlobalParams.__dataclass_fields__)
