from pathlib import Path
from laddoomaker.common.datums import DATUMS, AXES
from laddoomaker.model import build_subassemblies
from laddoomaker.parameters.global_params import P
from laddoomaker.parameters.motion_states import State, orbit_xy


def run_checks() -> list[tuple[str,bool,str]]:
    checks = []
    def add(name, ok, detail): checks.append((name, bool(ok), detail))
    add("overall locked envelope", (P.WIDTH,P.DEPTH,P.HEIGHT)==(430,380,625), f"{P.WIDTH}x{P.DEPTH}x{P.HEIGHT}")
    add("rounder axis", AXES["AX_R"]==(215,115), str(AXES["AX_R"]))
    add("doser axis", AXES["AX_D"]==(215,205), str(AXES["AX_D"]))
    add("sanitary plane", DATUMS["F"].value==250, str(DATUMS["F"].value))
    add("ball centre", P.BALL_CENTER_Z==178, str(P.BALL_CENTER_Z))
    add("orbit radius", orbit_xy(0)==(218,115) and orbit_xy(180)==(212,115), str(P.ORBIT_RADIUS))
    add("upper travel", P.UPPER_HEAD_TRAVEL==55, str(P.UPPER_HEAD_TRAVEL))
    add("retracted cartridge", P.UPPER_RETRACT_MIN_Z>=225, str(P.UPPER_RETRACT_MIN_Z))
    add("chute termination", P.CHUTE_OUTLET_Y==155, str(P.CHUTE_OUTLET_Y))
    subs = build_subassemblies(State.S0_HOME)
    add("A01-A10 hierarchy", set(subs)=={f"A{i:02}" for i in range(1,11)}, ", ".join(subs))
    machine_shape = __import__("laddoomaker.model", fromlist=["build_machine"]).build_machine(State.S0_HOME).toCompound()
    bb = machine_shape.BoundingBox()
    add("actual operational X envelope", bb.xmin >= 0 and bb.xmax <= 430, f"{bb.xmin:.2f}..{bb.xmax:.2f}")
    add("actual operational Y envelope", bb.ymin >= -90 and bb.ymax <= 380, f"{bb.ymin:.2f}..{bb.ymax:.2f}")
    add("actual operational Z envelope", bb.zmin >= 0 and bb.zmax <= 625, f"{bb.zmin:.2f}..{bb.zmax:.2f}")
    return checks


def write_report(path: Path) -> bool:
    results = run_checks(); path.parent.mkdir(parents=True,exist_ok=True)
    lines=["# VALIDATION REPORT", "", "Generated from executable Rev-A parameters.", ""]
    for name, ok, detail in results: lines.append(f"- {'PASS' if ok else 'FAIL'} — {name}: {detail}")
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")
    return all(ok for _,ok,_ in results)
