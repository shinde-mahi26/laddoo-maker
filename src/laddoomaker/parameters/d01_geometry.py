from dataclasses import dataclass


@dataclass(frozen=True)
class Bounds:
    x0: float; x1: float; y0: float; y1: float; z0: float; z1: float


FOOD_ZONE = Bounds(35, 395, 0, 250, 120, 600)
REAR_DRY_SPINE = Bounds(0, 430, 250, 380, 0, 625)
LOWER_DRY_CHAMBER = Bounds(35, 395, 35, 220, 35, 120)
C_FRAME = Bounds(135, 295, 50, 185, 35, 365)
FEEDER_MOTOR = Bounds(160, 270, 255, 365, 335, 415)
AGITATOR_MOTOR = Bounds(175, 255, 265, 355, 420, 490)
WEIGH_MODULE = Bounds(165, 265, 155, 250, 270, 350)
TRANSFER_CHUTE = Bounds(180, 250, 150, 215, 195, 285)
LOWER_ROUNDER_DRY = Bounds(135, 295, 45, 190, 35, 150)
UPPER_HEAD = Bounds(155, 275, 55, 155, 205, 390)
EJECTOR_TRANSIENT = Bounds(145, 300, 75, 155, 155, 205)
