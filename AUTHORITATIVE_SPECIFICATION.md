# CODEX MASTER CAD BUILD PROMPT

## LaddooMaker Mini — Rev-A Parametric Mechanical CAD

You are the lead mechanical CAD engineer implementing an already-defined machine architecture.

Your task is to create a complete, parametric, version-controlled CAD repository for:

**LaddooMaker Mini — Rev-A**

This is a compact countertop automatic machine that accepts prepared laddoo mixture, automatically portions 20–60 g, rounds each portion into a sphere, and ejects the finished laddoo.

The engineering architecture in this prompt is authoritative.

---

# 1. CRITICAL OPERATING RULE

Do **not independently redesign the machine**.

Your responsibility is to convert the supplied engineering specification into:

1. parametric CAD;
2. assemblies;
3. motion configurations;
4. keep-out geometry;
5. interface definitions;
6. interference checks;
7. validation reports;
8. neutral CAD exports.

If something appears mechanically questionable:

* do not silently change it;
* model the specified geometry if physically possible;
* create a documented issue;
* propose an alternative separately;
* keep the authoritative Rev-A geometry unchanged unless explicitly instructed.

Use:

`DESIGN_ISSUES.md`

for every discovered conflict.

---

# 2. DEVELOPMENT PHILOSOPHY

This first CAD iteration is a:

## Spatial / Interface / Mechanical Architecture Prototype

It is NOT yet a final manufacturing model.

Priorities:

1. overall packaging;
2. correct datums;
3. component interfaces;
4. motion;
5. service accessibility;
6. collision detection;
7. food-zone/dry-zone segregation;
8. replaceable components;
9. purchased-component envelopes;
10. future manufacturability.

Do not waste time adding cosmetic details.

---

# 3. CAD TECHNOLOGY

Use:

**Python 3.12**

Primary CAD:

**CadQuery 2.8.x**

Use `cq.Assembly` for the complete machine assembly.

Use millimetres everywhere.

Do not use inches internally.

Source-of-truth geometry must remain parametric Python.

Do NOT make:

* STL;
* DXF;
* STEP;
* Fusion files;
* FreeCAD files

the source of truth.

Those are generated artifacts.

---

# 4. REPOSITORY STRUCTURE

Create:

```text
laddoomaker-cad/
│
├── README.md
├── pyproject.toml
├── .gitignore
│
├── src/
│   └── laddoomaker/
│       │
│       ├── __init__.py
│       │
│       ├── parameters/
│       │   ├── global_params.py
│       │   ├── d01_geometry.py
│       │   ├── tolerances.py
│       │   ├── materials.py
│       │   └── motion_states.py
│       │
│       ├── common/
│       │   ├── datums.py
│       │   ├── keepouts.py
│       │   ├── hardware.py
│       │   ├── metadata.py
│       │   └── utilities.py
│       │
│       ├── a01_chassis/
│       ├── a02_hopper/
│       ├── a03_agitator/
│       ├── a04_feeder_doser/
│       ├── a05_weigh_module/
│       ├── a06_transfer/
│       ├── a07_orbital_rounder/
│       ├── a08_upper_head/
│       ├── a09_ejector_output/
│       └── a10_electrical/
│
├── assemblies/
│   ├── food_path.py
│   ├── dosing_assembly.py
│   ├── rounding_assembly.py
│   ├── electrical_dry_zone.py
│   └── machine_rev_a.py
│
├── configs/
│   ├── state_s0_home.py
│   ├── state_s1_loading.py
│   ├── state_s2_forming.py
│   └── state_s3_ejection.py
│
├── checks/
│   ├── interference.py
│   ├── clearances.py
│   ├── service_access.py
│   ├── keepout_validation.py
│   ├── datum_validation.py
│   └── mass_properties.py
│
├── tests/
│   ├── test_global_envelope.py
│   ├── test_axes.py
│   ├── test_motion_states.py
│   ├── test_keepouts.py
│   └── test_exports.py
│
├── manifest/
│   ├── bom_rev_a.yaml
│   ├── purchased_components.yaml
│   └── fabricated_components.yaml
│
├── scripts/
│   ├── build_machine.py
│   ├── export_all.py
│   ├── validate_all.py
│   └── generate_report.py
│
├── exports/
│   ├── step/
│   ├── stl/
│   ├── gltf/
│   ├── svg/
│   └── preview/
│
└── docs/
    ├── D01_GENERAL_ARRANGEMENT.md
    ├── DESIGN_ISSUES.md
    ├── DESIGN_DECISIONS.md
    ├── INTERFACE_CONTROL.md
    ├── VALIDATION_REPORT.md
    ├── SERVICE_ACCESS.md
    └── REVISION_HISTORY.md
```

---

# 5. GLOBAL COORDINATE SYSTEM

Use:

```text
X = left → right
Y = front → rear
Z = bottom → top
```

Global origin:

```text
G0 = (0, 0, 0)
```

at the:

**front-left point of the machine countertop plane.**

---

# 6. MASTER MACHINE ENVELOPE — LOCKED

Body:

```text
WIDTH  X = 430 mm
DEPTH  Y = 380 mm
HEIGHT Z = 625 mm
```

Body space:

```text
X = 0 → 430
Y = 0 → 380
Z = 0 → 625
```

Output tray may extend forward into:

```text
Y = -90 mm
```

Maximum operational envelope approximately:

```text
430 × 470 × 625 mm
```

Do not change these dimensions.

---

# 7. MASTER DATUMS — LOCKED

Create datum objects/reference planes for:

```text
DATUM_A = structural base plane
DATUM_B = X = 215
DATUM_C = Y = 0
DATUM_D = Y = 115
DATUM_E = Y = 205
DATUM_F = Y = 250
```

Descriptions:

```text
A = structural base datum
B = machine longitudinal centre plane
C = front reference plane
D = rounder centre plane
E = dosing centre plane
F = sanitary separation plane
```

---

# 8. CRITICAL PRODUCT AXES — LOCKED

Rounder axis:

```text
AX_R:
X = 215
Y = 115
vertical in Z
```

Dosing axis:

```text
AX_D:
X = 215
Y = 205
vertical in Z
```

Offset:

```text
90 mm
```

Do not alter this offset.

---

# 9. MASTER VERTICAL REFERENCES — LOCKED

Use:

```text
Z625 = maximum machine height

Z600 = hopper upper rim

Z455 = hopper agitator shaft axis

Z395 = hopper throat plane

Z375 = feeder rotor shaft axis

Z340 = primary dosing gate G1

Z285 = weigh discharge gate G2

Z208 = transfer chute outlet lip

Z178 = nominal finished-ball centre

Z150 = lower rounder cartridge mounting datum

Z120 = sanitary rounder deck

Z35 = principal structural base level

Z0 = countertop
```

These supersede all earlier exploratory dimensions.

---

# 10. FUNCTIONAL ZONES

Create explicit translucent keep-out solids for all zones.

## FOOD / WET ZONE

Approximate:

```text
X = 35 → 395
Y = 0 → 250
Z = 120 → 600
```

## REAR DRY SPINE

```text
Y = 250 → 380
```

Nominal depth:

```text
130 mm
```

## LOWER DRY CHAMBER

Approximate:

```text
X = 35 → 395
Y = 35 → 220
Z = 35 → 120
```

Food-zone components must not expose:

* bearings requiring lubrication;
* belts;
* electrical hardware;
* ordinary wiring;
* unsealed motors.

---

# 11. SANITARY WALL — LOCKED

Primary sanitary wall:

```text
Y = 250
```

Material:

```text
SS304
1.2 mm nominal
```

Approximate extent:

```text
X = 35 → 395
Z = 120 → 520
```

Only explicitly defined penetrations may cross it.

Allowed penetration categories:

1. A03 agitator shaft;
2. A04 feeder shaft;
3. G1 gate drive;
4. G2 gate drive;
5. sensor harness;
6. load-cell harness;
7. intentionally modelled sealed service connections.

Do not introduce arbitrary openings.

---

# 12. A01 — CHASSIS / STRUCTURE

Create separate parametric parts for:

```text
A01-001 base pan
A01-002 rear structural spine
A01-003 sanitary partition
A01-004 front food deck
A01-005 left enclosure
A01-006 right enclosure
A01-007 rear electrical cover
A01-008 front service door
A01-009 rounder C-frame
A01-010 reinforcement brackets
```

Nominal materials:

```text
Base pan:
SS304 2.0 mm

Rear spine:
SS304 1.5 mm

Sanitary partition:
SS304 1.2 mm

Food deck:
SS304 1.5 mm

External panels:
SS304 1.0 mm

Rounder C-frame:
SS304 4.0 mm
```

At this stage use simplified folded-shell geometry where exact bend allowances have not yet been defined.

Do NOT generate production flat patterns yet.

---

# 13. ROUNDING C-FRAME

The rounder mechanism must be structurally referenced to one rigid internal frame.

Allowed C-frame envelope:

```text
X = 135 → 295
Y = 50 → 185
Z = 35 → 365
```

Preliminary four-point mounting interface:

```text
P1 = X155 Y70
P2 = X275 Y70
P3 = X155 Y170
P4 = X275 Y170
```

Fastener class:

```text
M6
```

Pattern:

```text
120 × 100 mm
```

Upper and lower rounding systems must mount to this same structural frame.

Do not reference their alignment to cosmetic outer panels.

---

# 14. A02 — HOPPER

Upper opening:

```text
X = 75 → 355
Y = 65 → 305
Z = 600

size:
280 × 240 mm
```

Lower throat:

```text
X = 160 → 270
Y = 165 → 245
Z = 395

size:
110 X × 80 Y mm
```

Hopper therefore transitions rearward:

```text
upper Y centre = 185
lower Y centre = 205
```

Rearward offset:

```text
20 mm
```

Use:

```text
SS304
1.2 mm
```

Create:

* hopper shell;
* top rolled-edge approximation;
* removable lid;
* bottom mounting flange;
* gasket representation;
* two locating pins;
* two over-centre clamp envelopes.

Do not optimize funnel geometry without approval.

---

# 15. HOPPER SERVICE MOVEMENT

Model hopper as removable.

Required removal sequence:

```text
Stage 1:
+30 mm Z

Stage 2:
approximately -100 mm Y
```

Create a hopper service keep-out.

Required overhead service clearance:

```text
180 mm above machine
```

Run an interference check of the removal trajectory.

---

# 16. A03 — ANTI-BRIDGE AGITATOR

Axis:

```text
X = 215
Z = 455
parallel to Y
```

Food-side active shaft:

approximately:

```text
Y = 125 → 245
```

Main shaft:

```text
Ø12 mm
SS304
```

Create:

* shaft;
* central hub;
* four simplified rounded agitator arms;
* sanitary penetration;
* bearing envelopes;
* removable coupling;
* generic purchased gearmotor envelope.

Motor keep-out:

```text
X = 175 → 255
Y = 265 → 355
Z = 420 → 490
```

Purchased gearmotor shall initially be a generic envelope.

Do not design gearbox internals.

---

# 17. A04 — LOW-SHEAR FEEDER

Feeder rotor axis:

```text
X = 215
Z = 375
parallel to Y
```

Active rotor envelope approximately:

```text
X = 175 → 255
Y = 170 → 240
Z = 340 → 410
```

Main rotor shaft:

```text
Ø12 mm SS304
```

Model:

* rotor shaft;
* rotor hub;
* four rounded paddles;
* removable food housing;
* removable housing liner;
* shaft coupling;
* bearing envelopes;
* rear gearbox;
* generic 24 V 100 W-class BLDC envelope.

IMPORTANT:

Feeder paddle geometry is a:

`DEVELOPMENT_COMPONENT`

It must be parameterized.

Do not treat paddle shape as production-frozen.

---

# 18. FEEDER MOTOR KEEP-OUT

Reserve:

```text
X = 160 → 270
Y = 255 → 365
Z = 335 → 415
```

No electrical board or unrelated structure may occupy this space.

---

# 19. PRIMARY DOSING GATE — G1

Gate reference:

```text
Z = 340
```

Nominal opening:

```text
~50 mm X
~45 mm Y
```

Gate translation direction:

```text
Y
```

Reserve total actuator/blade motion:

```text
65 mm
```

Model both:

```text
G1_CLOSED
G1_OPEN
```

Gate blade nominal thickness:

```text
1.5 mm SS304
```

Exact gate edge remains development geometry.

---

# 20. A05 — GRAVIMETRIC WEIGH MODULE

Axis:

```text
X = 215
Y = 205
```

Nominal removable cup:

```text
Ø70 mm
```

Maximum envelope:

```text
Ø80 mm
```

Approximate vertical envelope:

```text
Z = 285 → 338
```

Complete A05 keep-out:

```text
X = 165 → 265
Y = 155 → 250
Z = 270 → 350
```

Model:

* removable weigh cup;
* conical lower portion;
* three-point locating interface;
* load platform;
* generic 1 kg single-point load-cell envelope;
* load-cell shield;
* mechanical overload stops;
* lower discharge gate;
* actuator envelope.

Load cell must remain installed when cup is removed.

---

# 21. WEIGH-CUP SERVICE ACCESS

Cup removal direction:

```text
-Y
```

Required unobstructed extraction:

```text
≥100 mm
```

Validate that:

* C-frame;
* service-door frame;
* transfer chute;
* gate hardware

do not prevent removal.

---

# 22. LOWER WEIGH GATE — G2

Reference:

```text
Z = 285
```

Translation:

```text
parallel Y
```

Reserve:

```text
60 mm motion envelope
```

Create:

```text
G2_OPEN
G2_CLOSED
```

---

# 23. A06 — TRANSFER CHUTE

Inlet reference approximately:

```text
X = 215
Y = 205
Z = 278
```

Outlet lip:

```text
X = 215
Y = 155
Z = 208
```

Approximate displacement:

```text
Y travel = 50 mm
Z drop = 70 mm
```

Resulting slope:

approximately 54–55 degrees.

Nominal material:

```text
SS304 1.0 mm
```

Create removable chute.

---

# 24. TRANSFER CHUTE CRITICAL RULE

Chute terminates at:

```text
Y = 155
```

It must NOT extend all the way to:

```text
Y = 115
```

The final approximately 40 mm horizontal transfer to the rounder is intentionally a free-flight region.

Reserve chute keep-out:

```text
X = 180 → 250
Y = 150 → 215
Z = 195 → 285
```

---

# 25. A07 — ORBITAL ROUNDER

Rounder axis:

```text
X = 215
Y = 115
```

Nominal ball centre:

```text
Z = 178
```

Allow ball-centre operating range:

```text
Z = 174 → 183
```

Lower cartridge mounting datum:

```text
Z = 150
```

Rounder deck:

```text
Z = 120
```

---

# 26. ORBITAL MOTION

Lower cup centre nominal:

```text
X = 215
Y = 115
```

Orbit:

```text
radius = 3.00 mm
```

Thus centre movement:

```text
X = 212 → 218
Y = 112 → 118
```

Lower cup must translate in circular motion WITHOUT rotating around its own axis.

Implement this conceptually with:

* X carriage;
* Y carriage;
* eccentric follower.

Detailed rail selection remains provisional.

---

# 27. LOWER ROUNDER DRY KEEP-OUT

Reserve:

```text
X = 135 → 295
Y = 45 → 190
Z = 35 → 150
```

Contains:

* X/Y carriage;
* linear-guide envelopes;
* eccentric shaft;
* bearings;
* pulley;
* belt;
* rounder motor;
* counterweight.

---

# 28. ECCENTRIC SHAFT

Main shaft:

```text
Ø12 mm
```

Use two 12 mm-bore bearing envelopes.

Nominal bearing-class envelope may represent:

```text
12 × 28 × 8 mm
```

Eccentric:

```text
3.00 mm offset
```

Create eccentric as a replaceable cap/module rather than permanently incorporating offset into the entire main shaft.

Parameter:

```text
ORBIT_RADIUS = 3.00
```

Future development range may include:

```text
2.0
2.5
3.0
3.5
```

but Rev-A configuration remains 3.00.

---

# 29. LOWER SANITARY BELLOWS

Model a simplified compliant cover between:

* moving lower-cartridge boss;
* stationary rounder deck.

It must permit:

```text
±3 mm X
±3 mm Y
```

Do not attempt detailed elastomer FEA.

Represent its geometric envelope.

---

# 30. ROUNDING CARTRIDGES

Create parametric upper and lower cartridges:

```text
C34
C40
C46
C52
```

Finished-ball working ranges:

```text
C34 = 31–36 mm
C40 = 36–42 mm
C46 = 42–48 mm
C52 = 48–54 mm
```

Model cartridge mounts using a conceptual three-lug bayonet interface.

Upper and lower cartridge keying must be different.

Do not allow them to be accidentally interchangeable.

Cartridge curvature remains:

`DEVELOPMENT_COMPONENT`

Keep parameters exposed.

---

# 31. A08 — UPPER Z HEAD

Axis:

```text
X = 215
Y = 115
```

Usable mechanical Z travel:

# 55 mm

This value is LOCKED for Rev-A0.

Model:

* upper structural support;
* NEMA17-class motor envelope;
* T8 × 2 conceptual leadscrew;
* two linear guides;
* carriage;
* spring plunger;
* approximate 1 N/mm spring;
* bellows;
* cartridge holder;
* upper cartridge.

---

# 32. A08 ENVELOPE

Reserve:

```text
X = 155 → 275
Y = 55 → 155
Z = 205 → 390
```

Required separation to feeder fixed housing:

```text
≥10 mm
```

---

# 33. UPPER-CUP RETRACTION REQUIREMENT

At full retract, the lowest surface of every installed upper cartridge shall satisfy:

```text
Z ≥ 225
```

This is critical.

The loading corridor must remain clear between:

```text
transfer chute outlet ~ Z208
```

and:

```text
upper cup lowest surface ≥ Z225
```

Validate for C34, C40, C46 and C52.

---

# 34. FORMING FORCE REPRESENTATION

Prototype forming force is created through spring compression.

Starting spring rate:

```text
~1 N/mm
```

Working conceptual force:

```text
2–10 N
```

No active force sensor is required in Rev-A CAD.

The spring-compliant plunger must be geometrically represented.

---

# 35. ROUNDING PROCESS KEEP-OUT

Create a cylindrical processing keep-out:

```text
centre:
X = 215
Y = 115

diameter:
80 mm

Z:
145 → 230
```

No permanent component may occupy this space.

A09 ejector may enter only during the S3 EJECTION state.

---

# 36. A09 — EJECTOR

Rev-A ejection direction:

# +X

Use side-sweep architecture.

Model:

* actuator envelope;
* shaft;
* removable food pusher;
* coupling;
* home sensor envelope;
* output chute.

Ejector transient envelope:

```text
X = 145 → 300
Y = 75 → 155
Z = 155 → 205
```

When parked, the pusher must remain entirely outside the Ø80 processing keep-out.

---

# 37. OUTPUT CHUTE

Initial finished-ball reception region approximately:

```text
X = 280
Y = 110
Z = 165
```

Output transitions toward front.

Nominal front exit approximately:

```text
X = 250
Y = 15
Z = 105
```

Exact curved chute geometry remains adjustable within its envelope.

---

# 38. OUTPUT TRAY

Nominal:

```text
260 mm W
180 mm D
```

Approximate plan:

```text
X = 85 → 345
Y = -90 → +90
```

Nominal tray floor:

```text
Z ≈ 80
```

Tray removal direction:

```text
-Y
```

Tray shall be removable without opening the main service door.

---

# 39. MACHINE FEET

Nominal centres:

```text
F1 = X35  Y35
F2 = X395 Y35
F3 = X35  Y345
F4 = X395 Y345
```

Nominal:

```text
M8
Ø40 mm maximum foot diameter
```

---

# 40. FRONT SERVICE DOOR

Nominal clear opening:

```text
320 mm W
330 mm H
```

Approximate:

```text
X = 55 → 375
Z = 115 → 445
Y ≈ 0
```

Include:

* conceptual hinge;
* latch;
* interlock target;
* transparent inspection-window placeholder.

Opening geometry must permit removal of food-contact parts.

---

# 41. SERVICE CLEARANCES

Create KEEP_OUT solids for:

## Hopper removal

```text
180 mm above machine
```

## Front servicing

```text
450 mm in front
```

## Rear maintenance

```text
250 mm behind
```

## Tray extraction

```text
≥100 mm forward
```

These may exist outside the machine assembly but must be visible in a service-layout configuration.

---

# 42. A10 — ELECTRICAL / CONTROLS

Do not model PCB internals.

Create purchased-component envelopes.

Main electronics region approximately:

```text
X = 285 → 390
Y = 260 → 370
Z = 160 → 550
```

This region must subtract:

* feeder motor keep-out;
* agitator motor keep-out;
* wiring routing;
* cooling clearance.

Model generic envelopes for:

* 24 V / ~350 W PSU;
* controller;
* BLDC drivers;
* stepper driver;
* contactor;
* terminal blocks;
* EMI filter;
* DC/DC converter.

---

# 43. HMI

Nominal centre:

```text
X = 105
Y ≈ 15
Z = 515
```

Maximum envelope:

```text
130 × 90 mm
```

Represent a:

```text
4.3-inch-class HMI
```

Do not model electronics internally.

---

# 44. EMERGENCY STOP

Nominal centre:

```text
X = 350
Y ≈ 10
Z = 515
```

Create purchased-component envelope.

Ensure it remains externally accessible.

---

# 45. VENTILATION

Rear intake approximate zone:

```text
X = 280 → 370
Y ≈ 378
Z = 80 → 180
```

Rear exhaust approximate zone:

```text
X = 280 → 370
Y ≈ 378
Z = 430 → 520
```

No air path may communicate directly with the food zone.

---

# 46. MOTION STATES

Implement four complete assembly configurations.

## S0 — HOME / SERVICE

```text
Upper cup fully retracted
G1 closed
G2 closed
Ejector parked
Orbital mechanism at home
```

## S1 — LOADING

```text
Upper cup fully retracted
G2 open as required
Transfer path clear
Ejector parked
Lower rounder at home
```

## S2 — FORMING

```text
G1 closed
G2 closed
Upper cup lowered
Ejector parked
Lower rounder in orbital operating configuration
```

For static geometry, provide at least:

```text
0°
90°
180°
270°
```

eccentric positions.

## S3 — EJECTION

```text
Rounder returned home
Upper cup retracted
Ejector swept through discharge position
```

---

# 47. INTERFERENCE CHECKS

Implement automated or programmatic geometric checks for:

```text
IC01 upper cup vs transfer chute
IC02 upper cup vs loading corridor
IC03 ejector vs transfer chute
IC04 ejector vs cartridges
IC05 orbital carrier vs sanitary deck
IC06 timing belt/pulleys vs chassis
IC07 feeder rotor vs hopper throat
IC08 G1 gate travel vs sanitary wall
IC09 G2 gate travel vs sanitary wall
IC10 hopper removal vs enclosure/HMI
IC11 weigh cup removal vs front frame
IC12 cartridge removal vs service door
IC13 ejector vs service door
IC14 motor envelopes vs electrical volume
IC15 moving cables vs mechanisms
```

Generate:

```text
docs/VALIDATION_REPORT.md
```

with PASS/FAIL for each.

---

# 48. MINIMUM CLEARANCES

Unless an explicit later detail overrides:

```text
stationary non-contact parts:
≥2 mm

moving mechanism to fixed structure:
≥3 mm

motors/gearboxes to enclosure:
≥5 mm

upper head to feeder fixed housing:
≥10 mm

removable food parts:
≥5 mm extraction clearance

moving wiring:
≥10 mm plus strain-relief envelope
```

---

# 49. COMPONENT METADATA

Every generated component must include metadata in the manifest:

```text
part_id
name
subassembly
revision
geometry_type
material
food_contact
make_or_buy
development_status
quantity
mass_if_known
notes
```

Allowed geometry types:

```text
FABRICATED
MACHINED
PURCHASED
FOOD_CONTACT
KEEP_OUT
```

Multiple flags may apply.

---

# 50. DEVELOPMENT COMPONENTS

The following are intentionally NOT production-frozen:

```text
feeder paddle geometry
feeder internal clearance
G1 cutting edge
G2 gate detail
rounding cup curvature
rounding insert material
transfer trajectory
ejector face geometry
exact motor/gearbox models
exact linear guides
exact belt/pulley selection
```

Mark them clearly.

Do not convert an assumption into a locked dimension.

---

# 51. LOCKED PARAMETERS

Codex may not alter:

```text
machine width = 430
machine depth = 380
machine height = 625

machine centre plane = X215

rounder Y = 115
dosing Y = 205
sanitary wall Y = 250

ball centre nominal Z = 178
lower cartridge datum Z = 150
rounder deck Z = 120

feeder axis Z = 375
agitator axis Z = 455

G1 Z = 340
G2 Z = 285

transfer outlet =
X215 Y155 Z208

orbit radius = 3.00

upper Z travel = 55

hopper upper opening =
280 × 240

hopper throat =
110 X × 80 Y
```

---

# 52. PARAMETER FILE

All major values must live centrally.

Example structure:

```python
MACHINE_WIDTH = 430.0
MACHINE_DEPTH = 380.0
MACHINE_HEIGHT = 625.0

CENTER_X = 215.0

ROUNDER_Y = 115.0
DOSER_Y = 205.0
SANITARY_WALL_Y = 250.0

BALL_CENTER_Z = 178.0
LOWER_CARTRIDGE_DATUM_Z = 150.0
ROUNDER_DECK_Z = 120.0

FEEDER_AXIS_Z = 375.0
AGITATOR_AXIS_Z = 455.0

G1_Z = 340.0
G2_Z = 285.0

CHUTE_OUTLET_Y = 155.0
CHUTE_OUTLET_Z = 208.0

ORBIT_RADIUS = 3.00
UPPER_Z_TRAVEL = 55.0
```

Do not scatter locked values through individual files.

---

# 53. MATERIAL LIBRARY

At minimum define:

```text
SS304
Aluminium
Food-contact polymer placeholder
Food-grade silicone placeholder
Generic steel
Purchased component
Keep-out
```

Assign approximate density so mass properties can later be calculated.

---

# 54. PURCHASED COMPONENT MODELLING RULE

Do NOT create fake engineering detail inside motors, bearings, electronics, switches or load cells.

Purchased components should initially be:

```text
accurate interface
+
conservative external envelope
```

Example motor:

model:

* body envelope;
* shaft;
* mounting face;
* mounting holes;
* connector keep-out if needed.

Do not model windings or internal gears.

---

# 55. BEARINGS

Where currently specified as generic 12 mm shaft bearings, create nominal envelopes representing:

```text
12 mm ID
28 mm OD
8 mm width
```

Do not lock manufacturer or exact bearing specification until purchasing stage.

---

# 56. MASS PROPERTIES

After initial geometry is complete, calculate approximate:

```text
dry machine mass
CG X
CG Y
CG Z
```

Also create a simplified 4 kg hopper-mixture mass.

Loaded CG target:

```text
X = 215 ±25
Y = 185 ±30
Z ≤ 320
```

If outside this envelope:

do NOT redesign automatically.

Report it as an issue.

---

# 57. D01 DRAWING VIEWS

Generate geometry suitable for later drawing creation.

Required views:

## D01-01

* isometric;
* front elevation;
* right elevation;
* top view;
* overall machine envelope;
* A01–A10 labels;
* service envelopes.

## D01-02

Prepare section definitions:

### A-A

```text
X = 215
```

Longitudinal vertical section.

### B-B

```text
Y = 115
```

Rounder section.

### C-C

```text
Y = 205
```

Doser section.

### D-D

```text
Z ≈ 180
```

Horizontal process-layout section.

Do not attempt full production dimensioning yet.

---

# 58. EXPORT REQUIREMENTS

Generate:

## Complete assembly

```text
exports/step/LADDOOMAKER_REV_A.step
```

## Subassemblies

Separate STEP for:

```text
A01
A02
A03
A04
A05
A06
A07
A08
A09
A10
```

## Individual machined/fabricated components

STEP export where meaningful.

## Prototype polymer components

STL exports for:

```text
C34
C40
C46
C52
feeder development paddles
development ejector pad
```

## Visual review

Export:

```text
GLTF/GLB where practical
SVG orthographic previews
```

Do NOT produce production sheet-metal DXFs at this stage unless the profile is truly planar and does not require an unresolved bend/unfold operation.

---

# 59. BOM MANIFEST

Create:

```text
manifest/bom_rev_a.yaml
```

containing A01–A10.

At minimum include major parts already defined in this prompt.

Part-number format:

```text
A07-006
```

Never assign random generated part IDs.

---

# 60. BUILD SCRIPT

Provide one command that builds the complete CAD.

Example desired developer experience:

```bash
python scripts/build_machine.py
```

and:

```bash
python scripts/validate_all.py
```

and:

```bash
python scripts/export_all.py
```

Commands should create missing export directories automatically.

---

# 61. TESTS

Implement automated tests for at least:

```text
machine overall envelope
datum coordinates
rounder axis
doser axis
sanitary plane
ball-centre location
hopper dimensions
orbit radius
upper-head travel
service keep-outs
major subassembly existence
export success
```

Where reliable geometric intersection testing is available, test collision states.

---

# 62. BUILD ORDER

Do NOT attempt the entire detailed machine in one monolithic file.

Proceed in phases.

## PHASE 0 — Repository

Create:

* package structure;
* parameters;
* datums;
* metadata;
* build infrastructure;
* tests.

Commit/checkpoint.

---

## PHASE 1 — D01 Skeleton

Model only:

* overall envelope;
* datums;
* structural base;
* sanitary wall;
* rounder axis;
* doser axis;
* hopper envelope;
* all keep-outs.

Validate D01 coordinates before proceeding.

---

## PHASE 2 — Purchased Component Envelopes

Create generic:

* motors;
* gearboxes;
* load cell;
* bearings;
* HMI;
* PSU;
* stepper;
* electrical modules.

Do not over-detail.

---

## PHASE 3 — Food Path

Build:

```text
A02
A03
A04
A05
A06
A07 cartridges
A08 upper cartridge
A09 output path
```

Verify continuity.

---

## PHASE 4 — Mechanical Motion

Implement:

* G1 motion;
* G2 motion;
* upper Z;
* lower 3 mm orbital movement;
* ejector sweep.

Generate S0–S3 states.

---

## PHASE 5 — Structural Integration

Add:

* rounder C-frame;
* motor mounts;
* bearing supports;
* enclosure shells;
* service door;
* lower dry compartment.

---

## PHASE 6 — Validation

Run all:

* interference;
* keep-out;
* clearance;
* service-access;
* envelope;
* motion-state checks.

Do not conceal failures.

---

## PHASE 7 — Exports

Export:

* STEP;
* STL;
* GLTF;
* SVG/previews;
* manifests;
* reports.

---

# 63. DO NOT START D02–D12 YET

At completion of this task, STOP before detailed fabrication drawings.

Do not generate:

* final bend deductions;
* welding symbols;
* production GD&T;
* production DXFs;
* bearing fits;
* machining tolerances;
* final surface-finish callouts;
* final electrical drawings.

Those come after D01 spatial review.

---

# 64. DESIGN-ISSUE FORMAT

If you find a problem, write:

```text
ISSUE ID:
DI-001

LOCATION:
A08 vs A06

STATE:
S1 Loading

DESCRIPTION:
...

LOCKED PARAMETERS INVOLVED:
...

OBSERVED CONFLICT:
...

PROPOSED OPTION A:
...

PROPOSED OPTION B:
...

RECOMMENDED:
...

CAD STATUS:
Original Rev-A geometry preserved.
```

Never silently resolve it.

---

# 65. DESIGN DECISION LOG

Create:

```text
docs/DESIGN_DECISIONS.md
```

Separate:

```text
LOCKED
PROVISIONAL
ASSUMED
PURCHASE-DEPENDENT
TEST-DEPENDENT
```

This distinction must be preserved throughout the repository.

---

# 66. VISUAL REVIEW

Generate useful review outputs for a human engineer.

At minimum:

1. complete isometric assembly;
2. transparent outer-shell view;
3. food-path-only view;
4. dry-zone-only view;
5. longitudinal X215 section;
6. rounder section Y115;
7. dosing section Y205;
8. top process view;
9. S0 state;
10. S1 state;
11. S2 state;
12. S3 state;
13. hopper-removal state;
14. front-service state.

Use visually distinct component colors only for CAD review.

Manufacturing material/color is independent.

---

# 67. FINAL VALIDATION CHECKLIST

The CAD build must explicitly report whether all are true:

* overall machine ≤430×380×625;
* rounder axis X215/Y115;
* dosing axis X215/Y205;
* sanitary wall Y250;
* hopper fits;
* hopper removes;
* weigh cup removes;
* all cartridges install/remove;
* A08 has 55 mm usable travel;
* retracted upper cup clears loading corridor;
* A06 chute ends Y155;
* chute does not collide with A08;
* ejector does not collide with chute;
* ejector clears processing zone when parked;
* lower cup completes 3 mm orbit;
* orbital system clears sanitary deck;
* feeder motor remains dry;
* agitator motor remains dry;
* rounder drive remains below deck;
* electronics remain outside food zone;
* tray removes;
* front service door permits required access;
* STEP assembly export succeeds;
* A01–A10 exist as separate subassemblies;
* no undocumented dimensional changes exist.

---

# 68. DEFINITION OF DONE

The first CAD task is complete when the repository contains:

```text
working parametric Python CAD
+
A01–A10 assembly hierarchy
+
D01 Rev-A geometry
+
four machine states
+
service keep-outs
+
interference validation
+
STEP assembly
+
visual review exports
+
BOM manifest
+
design issue report
+
design decision log
```

and:

```text
python scripts/validate_all.py
```

runs successfully, except for explicitly documented unresolved engineering issues.

---

# 69. FINAL RESPONSE TO USER

At completion, report:

## CAD BUILD STATUS

```text
Repository:
...

CadQuery version:
...

Subassemblies completed:
A01...
```

## VALIDATION

```text
PASS:
...

FAIL:
...
```

## ENGINEERING ISSUES

List every unresolved issue.

## GENERATED FILES

List important STEP/GLTF/STL/report locations.

## RECOMMENDED D01 CHANGES

Only propose changes.

Do not implement changes to locked geometry without approval.

## NEXT STEP

State whether the assembly is sufficiently validated to begin:

```text
D02 — Chassis / Sheet-Metal Manufacturing Specification
```

or whether D01 requires Rev-A1 first.

---

# 70. EXECUTION INSTRUCTION

Do not respond with only a plan.

Create the repository and implement the CAD.

Work iteratively.

Run the code.

Run tests.

Generate exports.

Inspect validation results.

Fix coding/model-generation defects.

Do not alter locked engineering geometry merely to make a test pass.

Where actual component dimensions are not yet available, use clearly labelled conservative purchased-component envelopes.

The objective is:

# a buildable, inspectable, parametric digital prototype of LaddooMaker Mini Rev-A — not an illustration.
