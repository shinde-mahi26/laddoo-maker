"""Small reusable CadQuery geometry helpers."""
import cadquery as cq
from laddoomaker.parameters.d01_geometry import Bounds


def box_from_bounds(b: Bounds) -> cq.Workplane:
    return cq.Workplane("XY").box(b.x1-b.x0, b.y1-b.y0, b.z1-b.z0, centered=(False, False, False)).translate((b.x0,b.y0,b.z0))


def color(name: str) -> cq.Color:
    palette = {
        "steel": cq.Color(0.72, 0.75, 0.78, 1),
        "food": cq.Color(0.15, 0.65, 0.85, 1),
        "dry": cq.Color(0.95, 0.55, 0.12, 1),
        "keepout": cq.Color(0.85, 0.15, 0.15, 0.18),
        "polymer": cq.Color(0.25, 0.75, 0.35, 1),
    }
    return palette[name]
