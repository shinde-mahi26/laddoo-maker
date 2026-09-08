"""Development rounding cartridges; curvature is intentionally not production-frozen."""
from dataclasses import dataclass
import cadquery as cq


@dataclass(frozen=True)
class CartridgeSpec:
    code: str
    diameter_range: tuple[float, float]
    nominal_diameter: float


CARTRIDGES = {
    "C34": CartridgeSpec("C34", (31, 36), 34),
    "C40": CartridgeSpec("C40", (36, 42), 40),
    "C46": CartridgeSpec("C46", (42, 48), 46),
    "C52": CartridgeSpec("C52", (48, 54), 52),
}


def build_cartridge(code: str, upper: bool) -> cq.Workplane:
    """Return a conceptual cup with different upper/lower bayonet keying."""
    spec = CARTRIDGES[code]
    outer_r = spec.nominal_diameter / 2 + 5
    height = 25
    body = cq.Workplane("XY").circle(outer_r).extrude(height)
    cavity_r = spec.nominal_diameter / 2
    cavity = cq.Workplane("XY").sphere(cavity_r).translate((0, 0, 5 if upper else height - 5))
    body = body.cut(cavity)
    # Three conceptual key lugs; upper keying is rotated 30 degrees.
    lug = cq.Workplane("XY").box(7, 5, 5, centered=(True, True, False)).translate((outer_r + 2.5, 0, 5))
    keyed = body
    phase = 30 if upper else 0
    for angle in (phase, phase + 120, phase + 240):
        keyed = keyed.union(lug.rotate((0, 0, 0), (0, 0, 1), angle))
    return keyed


def installed_cartridge(code: str, upper: bool, x: float = 215, y: float = 115, z: float | None = None) -> cq.Workplane:
    if z is None: z = 225 if upper else 150
    return build_cartridge(code, upper).translate((x, y, z))
