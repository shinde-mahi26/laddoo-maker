import cadquery as cq
from laddoomaker.common.geometry import box_from_bounds, color
from laddoomaker.parameters import d01_geometry as g


def build_keepouts() -> cq.Assembly:
    a = cq.Assembly(name="keepouts")
    for name, bounds in {
        "food_zone": g.FOOD_ZONE, "rear_dry_spine": g.REAR_DRY_SPINE,
        "lower_dry_chamber": g.LOWER_DRY_CHAMBER, "feeder_motor": g.FEEDER_MOTOR,
        "agitator_motor": g.AGITATOR_MOTOR, "weigh_module": g.WEIGH_MODULE,
        "transfer_chute": g.TRANSFER_CHUTE, "lower_rounder_dry": g.LOWER_ROUNDER_DRY,
        "upper_head": g.UPPER_HEAD, "ejector_transient": g.EJECTOR_TRANSIENT,
    }.items():
        a.add(box_from_bounds(bounds), name=name, color=color("keepout"))
    process = cq.Workplane("XY").circle(40).extrude(85).translate((215,115,145))
    a.add(process, name="rounding_process", color=color("keepout"))
    return a
