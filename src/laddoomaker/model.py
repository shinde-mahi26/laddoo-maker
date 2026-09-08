"""D01 machine skeleton and simplified A01-A10 architecture."""
import cadquery as cq
from laddoomaker.common.geometry import color
from laddoomaker.parameters.global_params import P
from laddoomaker.parameters.motion_states import State, MOTIONS, orbit_xy
from laddoomaker.a07_orbital_rounder.cartridges import installed_cartridge
from laddoomaker.a01_chassis.d02_1 import build_approved_a01 as build_a01


def _box(x,y,z,dx,dy,dz):
    return cq.Workplane("XY").box(dx,dy,dz,centered=(False,False,False)).translate((x,y,z))


def _cylinder(x,y,z,r,h):
    return cq.Workplane("XY").circle(r).extrude(h).translate((x,y,z))


def build_subassemblies(state: State = State.S0_HOME, orbit_angle: float | None = None) -> dict[str,cq.Assembly]:
    m = MOTIONS[state]
    angle = m.orbit_angle if orbit_angle is None else orbit_angle
    ox, oy = orbit_xy(angle)
    groups: dict[str,cq.Assembly] = {}

    a = build_a01()
    groups["A01"] = a

    a = cq.Assembly(name="A02")
    hopper = cq.Workplane("XY").rect(110,80).workplane(offset=205).center(0,-20).rect(280,240).loft(combine=True).translate((215,205,395))
    hmove=(0,m.hopper_forward,m.hopper_lift)
    a.add(hopper.translate(hmove), name="A02-001_hopper_envelope", color=color("food"))
    a.add(_box(75,65,600,280,240,8).translate(hmove), name="A02-002_lid", color=color("steel"))
    for x in (120,310): a.add(_box(x,245,390,20,12,25).translate(hmove),name=f"A02-clamp-{x}",color=color("steel"))
    groups["A02"] = a

    a = cq.Assembly(name="A03")
    # XZ normal points toward -Y; negative extrusion implements Y125 -> Y245.
    shaft = cq.Workplane("XZ").circle(6).extrude(-120).translate((215,125,455)).translate(hmove)
    a.add(shaft, name="A03-001_hopper_shaft", color=color("food"))
    # Dry-side retractable axial dog; 20 mm +Y retraction in S4.
    coupling_y=245+m.coupling_retract
    coupling=cq.Workplane("XZ").circle(10).extrude(-20).translate((215,coupling_y,455))
    a.add(coupling,name="A03-004_retractable_dog_coupling",color=color("dry"))
    a.add(_box(175,315,420,80,40,70), name="A03-900_gearmotor_envelope", color=color("dry"))
    groups["A03"] = a

    a = cq.Assembly(name="A04")
    shaft = cq.Workplane("XZ").circle(6).extrude(-70).translate((215,170,375))
    a.add(shaft, name="A04-001_rotor_shaft", color=color("food")); a.add(_box(160,315,335,110,50,80), name="A04-900_motor_envelope", color=color("dry"))
    hub=cq.Workplane("XZ").circle(15).extrude(-70).translate((215,170,375))
    rotor=hub
    paddle=cq.Workplane("XZ").box(8,34,70,centered=(True,True,False)).translate((215,375,0)).rotate((0,0,0),(1,0,0),90).translate((0,170,0))
    # Simpler conservative 68 mm OD rotor envelope plus four visible paddles.
    rotor_env=cq.Workplane("XZ").circle(34).extrude(-70).translate((215,170,375))
    housing_outer=cq.Workplane("XZ").circle(42).extrude(-74).translate((215,168,375))
    housing_inner=cq.Workplane("XZ").circle(40).extrude(-74).translate((215,168,375))
    a.add(hub,name="A04-002_rotor_hub",color=color("food")); a.add(rotor_env,name="A04-004_paddle_sweep",color=color("polymer")); a.add(housing_outer.cut(housing_inner),name="A04-005_food_housing",color=color("steel"))
    g1_y = 180 + (-65 if m.g1_open else 0)
    a.add(_box(190,g1_y,340,50,45,1.5), name="A04-006_G1", color=color("steel"))
    groups["A04"] = a

    a = cq.Assembly(name="A05")
    cup = cq.Workplane("XY").circle(35).circle(30).extrude(45).translate((215,205,290))
    a.add(cup, name="A05-001_weigh_cup", color=color("food")); a.add(_box(175,205,275,80,25,12), name="A05-900_load_cell", color=color("dry"))
    gate_y = 205 + (-60 if m.g2_open else 0)
    a.add(_box(180,gate_y-25,285,70,50,1.5), name="A05-006_G2", color=color("steel")); groups["A05"] = a

    a = cq.Assembly(name="A06")
    # YZ side profile extruded across X: locked inlet Y205/Z278, outlet Y155/Z208.
    chute = cq.Workplane("YZ").moveTo(205,278).lineTo(155,208).lineTo(155,198).lineTo(205,268).close().extrude(70).translate((180,0,0))
    a.add(chute, name="A06-001_transfer_chute", color=color("food")); groups["A06"] = a

    a = cq.Assembly(name="A07")
    a.add(installed_cartridge("C52",False,ox,oy,150), name="A07-C52_lower_cartridge", color=color("polymer"))
    a.add(_cylinder(ox,oy,115,19,35), name="A07-001_moving_boss", color=color("steel"))
    a.add(_cylinder(ox,oy,95,34,20), name="A07-002_orbit_carriage", color=color("dry")); groups["A07"] = a
    a.add(_box(155,108,105,120,14,8), name="A07-003_x_guide", color=color("dry"))
    a.add(_box(208,55,112,14,120,8), name="A07-004_y_guide", color=color("dry"))
    outer_seat=_cylinder(215,115,120,36,4).cut(_cylinder(215,115,119,27,6))
    inner_seat=_cylinder(ox,oy,121,23,4).cut(_cylinder(ox,oy,120,21,6))
    bellows=_cylinder(215,115,124,36,23).cut(_cylinder(215,115,123,21,25))
    a.add(outer_seat,name="A07-005_bellows_outer_seat",color=color("steel")); a.add(inner_seat,name="A07-006_bellows_inner_seat",color=color("steel")); a.add(bellows,name="A07-007_bellows_envelope",color=color("polymer"))
    # Provisional HTD-3M belt drive below the deck.
    motor_axis=(260,115); driven_axis=(215,115)
    a.add(_cylinder(*motor_axis,65,9.55,9),name="A07-010_motor_pulley_20T",color=color("dry")); a.add(_cylinder(*driven_axis,65,11.46,9),name="A07-011_driven_pulley_24T",color=color("dry"))
    a.add(_box(215,105,65,45,20,9),name="A07-012_HTD3M_belt_envelope",color=color("dry")); a.add(_box(245,90,45,30,50,45),name="A07-013_rounder_motor",color=color("dry")); a.add(_box(240,88,43,40,54,5),name="A07-014_tension_slots",color=color("steel"))

    a = cq.Assembly(name="A08")
    upper_z = 225 - m.upper_drop
    a.add(installed_cartridge("C52",True,215,115,upper_z), name="A08-C52_upper_cartridge", color=color("polymer"))
    a.add(_box(155,55,260-m.upper_drop,120,100,30), name="A08-002_carriage", color=color("steel")); groups["A08"] = a

    a = cq.Assembly(name="A09")
    pusher_x = 145 + m.ejector_sweep
    a.add(_box(pusher_x,104,178,8,22,16), name="A09-002_pusher", color=color("polymer"))
    a.add(_box(85,-90,75,260,180,5), name="A09-006_output_tray", color=color("steel")); groups["A09"] = a

    a = cq.Assembly(name="A10")
    a.add(_box(285,260,160,105,110,150), name="A10-900_electronics_envelope", color=color("dry"))
    a.add(_box(40,5,470,130,10,90), name="A10-010_HMI", color=color("dry")); a.add(_cylinder(350,10,500,20,35), name="A10-011_estop", color=color("dry")); groups["A10"] = a
    # D01 wiring keep-outs: rear vertical trunks and explicit sealed crossings.
    routes={"A03":(300,285,430,12,70,70),"A04":(315,285,335,12,70,80),"gates":(280,245,270,12,115,90),"loadcell":(268,225,270,8,90,55),"A07":(300,245,45,12,100,90),"A08":(285,245,205,12,100,150),"A09":(320,245,145,12,100,70),"HMI":(25,15,465,12,245,105),"estop":(365,15,480,12,245,80)}
    for name,(x,y,z,dx,dy,dz) in routes.items(): a.add(_box(x,y,z,dx,dy,dz),name=f"A10-KO-{name}",color=color("keepout"))
    return groups


def build_machine(state: State = State.S0_HOME, orbit_angle: float | None = None) -> cq.Assembly:
    machine = cq.Assembly(name=f"LADDOOMAKER_REV_A1_{state.value}")
    for number, assembly in build_subassemblies(state, orbit_angle).items():
        machine.add(assembly, name=number)
    return machine
