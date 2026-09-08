from dataclasses import dataclass
from laddoomaker.parameters.global_params import P


@dataclass(frozen=True)
class Datum:
    name: str
    axis: str
    value: float
    description: str


DATUMS = {
    "A": Datum("A", "Z", P.STRUCTURAL_BASE_Z, "structural base datum"),
    "B": Datum("B", "X", 215, "machine longitudinal centre plane"),
    "C": Datum("C", "Y", 0, "front reference plane"),
    "D": Datum("D", "Y", 115, "rounder centre plane"),
    "E": Datum("E", "Y", 205, "dosing centre plane"),
    "F": Datum("F", "Y", 250, "sanitary separation plane"),
}

AXES = {"AX_R": (215, 115), "AX_D": (215, 205)}
