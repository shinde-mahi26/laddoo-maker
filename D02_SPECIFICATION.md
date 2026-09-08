# LADDOOMAKER MINI

# D02 — CHASSIS / BASE / STRUCTURAL MANUFACTURING DESIGN

## Rev-A1 → D02 Detail Development

Continue the EXISTING LaddooMaker CadQuery repository.

Do not rebuild the project.

D01 Rev-A1 is ACCEPTED and is now the authoritative spatial interface specification.

Your task is to convert **A01 Chassis/Base** from provisional spatial envelopes into a realistic prototype-manufacturable structural assembly.

Do NOT begin D03–D12.

Do NOT change locked D01 process geometry.

---

# 1. D02 objective

Create a fabrication-ready candidate design for:

**A01 — Chassis / Base / Structural Assembly**

including:

* structural base pan;
* rear structural spine;
* sanitary partition;
* rounder sanitary deck;
* rounder structural C-frame;
* C-frame alignment/mounting system;
* left/right exterior panels;
* rear service cover;
* front service-door frame;
* removable control-fascia carrier;
* feet and foot reinforcement;
* local reinforcement brackets;
* dry-zone motor-adapter interfaces;
* cable/gland mounting provisions;
* panel sealing interfaces;
* assembly and welding sequence.

Generate:

* parametric CadQuery geometry;
* STEP files;
* sheet profiles;
* preliminary flat patterns;
* DXFs where valid;
* dimensioned drawing data;
* material/weight report;
* structural-interface validation;
* prototype manufacturing BOM;
* fabrication notes;
* DFM report.

---

# 2. Authoritative D01 locked geometry

DO NOT CHANGE:

```text
Machine:
430 W × 380 D × 625 H mm

Global:
X left→right
Y front→rear
Z bottom→top

Centre plane:
X = 215

Rounder axis:
X215 / Y115

Dosing axis:
X215 / Y205

Sanitary wall:
Y250

Ball centre:
Z178

Lower cartridge datum:
Z150

Rounder sanitary deck:
Z120

Orbit:
3.00 mm radius

A08 travel:
55 mm

Feeder axis:
Z375

Agitator axis:
Z455

G1:
Z340

G2:
Z285

Transfer outlet:
X215/Y155/Z208
```

Existing D01 Rev-A1 motion/service states must continue to pass.

---

# 3. D02 design philosophy

The machine is intended to be fabricated using ordinary capable Indian prototype manufacturing processes:

* fibre/laser cutting;
* press-brake bending;
* TIG welding;
* manual finishing;
* conventional CNC milling/turning where genuinely required;
* standard fasteners;
* standard purchased components.

Avoid unnecessarily exotic manufacturing.

Prefer:

**laser-cut + bend + TIG + simple finish machining**

over:

**large billet CNC machining**.

Do not sacrifice alignment, hygiene or serviceability merely to minimize part count.

---

# 4. Primary material

Default structural material:

## SS304

Use nominal sheet/plate thicknesses:

| Component                    |  Thickness |
| ---------------------------- | ---------: |
| Base pan                     | **2.0 mm** |
| Rear structural spine        | **1.5 mm** |
| Sanitary partition           | **1.2 mm** |
| Rounder sanitary deck        | **1.5 mm** |
| External side panels         | **1.0 mm** |
| Rear service cover           | **1.0 mm** |
| Front outer skins            | **1.0 mm** |
| Control fascia carrier       | **1.5 mm** |
| Local reinforcement brackets | **2.0 mm** |
| Rounder C-frame plates       | **4.0 mm** |

Do not reduce these thicknesses automatically for mass/cost savings.

If FEA or fabrication review suggests a change, document it rather than silently applying it.

---

# 5. Surface/material assumptions

Use SS304 density for mass calculations.

Prototype finish assumptions:

* general external stainless: 2B or equivalent fabrication finish;
* food/wet-zone structural surfaces: smooth and cleanable;
* remove burrs;
* no sharp exposed sheet edges;
* no carbon-steel contamination of food-zone stainless;
* remove significant weld heat tint;
* pickle/passivate wet-zone stainless after fabrication where appropriate.

Direct food-contact surface specifications will be refined in D03–D09.

A01 is primarily structural and sanitary-support geometry.

---

# 6. A01 assembly hierarchy

Create/update:

```text
A01_CHASSIS
│
├── A01-001_BASE_PAN
├── A01-002_REAR_SPINE
├── A01-003_SANITARY_PARTITION
├── A01-004_ROUNDER_DECK
├── A01-005_LEFT_PANEL
├── A01-006_RIGHT_PANEL
├── A01-007_REAR_SERVICE_COVER
├── A01-008_FRONT_SERVICE_DOOR
├── A01-009_ROUNDER_C_FRAME
├── A01-010_REINFORCEMENT_SET
├── A01-011_FEET_SET
├── A01-012_PANEL_HARDWARE_SET
├── A01-013_STRUCTURAL_FASTENER_SET
├── A01-014_CONTROL_FASCIA_CARRIER
├── A01-015_A03_DRIVE_ADAPTER_INTERFACE
├── A01-016_A04_DRIVE_ADAPTER_INTERFACE
└── A01-017_CABLE_GLAND_INTERFACE_PLATE
```

Individual hardware may be nested below these assemblies.

---

# 7. A01-001 — base pan

Design a realistic folded SS304 base pan.

External footprint must remain:

```text
430 × 380 mm maximum
```

Principal structural base level:

```text
Z = 35 mm
```

The pan should provide:

* structural floor;
* foot mount reinforcement;
* C-frame mounting region;
* lower-drive chamber support;
* side-panel attachment;
* rear-spine attachment.

Prefer a one-piece laser-cut/folded pan where practical.

Starting configuration:

* 2.0 mm SS304;
* nominal 25–30 mm upturned peripheral flanges;
* corner reliefs designed for press brake manufacture;
* no unnecessary welded corner boxes.

Do not let flange geometry intrude into existing A07/A09 keep-outs.

---

# 8. feet

Retain D01 nominal foot centres:

```text
F1 X35  Y35
F2 X395 Y35
F3 X35  Y345
F4 X395 Y345
```

Feet:

```text
M8
maximum pad OD ≈40 mm
```

Design reinforced captive mounting points.

Preferred:

* welded SS nut plate;
* captive stainless nut;
* or equivalent serviceable arrangement.

Do NOT rely on a simple M8 thread tapped directly into 2 mm sheet.

Provide approximately:

```text
±10 mm levelling capability
```

where commercially realistic.

---

# 9. base reinforcement

Add local reinforcement only where mechanically justified:

* C-frame mounts;
* feet;
* heavy motor mounts;
* rear spine;
* door hinge loads.

Avoid turning the entire base into double-thickness sheet.

Prefer laser-cut 2 mm reinforcement pads.

---

# 10. lower dry chamber

Maintain usable lower mechanical region associated with D01:

```text
approximately
Z35 → Z120
```

and existing A07 lower-drive keep-out.

Do not obstruct:

* rounder BLDC;
* HTD belt;
* eccentric shaft;
* X/Y carriage;
* counterweight;
* ejector mechanism;
* wiring keep-outs.

Re-run IC06 and relevant D01 checks after chassis detailing.

---

# 11. A01-003 sanitary partition

Authoritative location:

# Y = 250 mm

Nominal material:

```text
SS304
1.2 mm
```

Approximate active extent inherited from D01:

```text
X35 → X395
Z120 → approximately Z520
```

Design the wall with formed returns on the **dry side**, not food-facing crevice-producing flanges.

Objectives:

* stiff enough to support seals/interfaces;
* separates wet and dry regions;
* supports shaft-seal interface plates where required;
* allows removable dry-side motor adapter plates.

Food-facing side should be as uninterrupted as practical.

---

# 12. sanitary-wall flanges

Use approximately:

```text
15–20 mm formed return flanges
```

where useful for stiffness.

Returns should point into the dry zone where possible.

Avoid horizontal ledges on the food-facing side that collect product/wash residue.

---

# 13. wet-zone seam philosophy

Where A01-003 interfaces with A01-004 and surrounding wet-zone structural surfaces:

prefer:

## continuous TIG seam

where a permanent joint is required.

Food/wet-facing seam should be:

* continuous;
* no intermittent cavities;
* dressed sufficiently smooth;
* visually inspectable.

Dry-side non-sanitary structural seams may use intermittent/stitch welding if distortion analysis permits.

Document every weld category.

---

# 14. A01-004 rounder sanitary deck

Authoritative plane:

# Z = 120 mm

Primary food-zone deck around rounder.

Material:

```text
SS304
1.5 mm
```

Maintain rounder axis:

```text
X215/Y115
```

Maintain Rev-A1 moving-boss interface:

```text
moving boss OD = 38 mm
deck aperture = Ø52 mm
```

The deck aperture centre shall be:

```text
X215/Y115
```

Do not reposition.

---

# 15. deck construction

The deck should be sufficiently stiff that normal cleaning/manual loads do not substantially change the rounder boss/deck clearance.

Use:

* folded downward edge returns;
* local dry-side reinforcement ring if required;
* attachment to C-frame/base structure.

Do NOT simply increase the entire deck thickness unless necessary.

If reinforcement ring is required:

place it completely on the dry side.

---

# 16. deck aperture tolerance

For prototype drawing candidate:

```text
Ø52.0 mm
```

Target positional tolerance relative to AX_R:

```text
±0.20 mm
```

Detailed production GD&T may be refined during D07.

Ensure final geometry preserves D01's:

```text
4.00 mm minimum boss/deck radial metal clearance
```

at full 3 mm orbit.

---

# 17. rounder C-frame — key D02 structural component

A01-009 is no longer just a bounding box.

Create a manufacturable internal C-frame within the existing envelope:

```text
X135 → 295
Y50 → 185
Z35 → 365
```

It must structurally support:

* A07 lower orbital mechanism;
* A08 upper Z head.

Upper and lower rounder mechanisms must reference this SAME frame.

Outer cosmetic panels must NOT establish their alignment.

---

# 18. C-frame manufacturing approach

Preferred construction:

* two primary 4 mm SS304 laser-cut side plates;
* 4 mm SS cross-members;
* folded brackets where appropriate;
* TIG welded in fixture;
* critical mounting interfaces finish-drilled/reamed or machined AFTER welding.

Do not depend on as-welded ±0.1 mm precision.

---

# 19. C-frame base interface

Retain nominal D01 mounting centres:

```text
P1 X155 Y70
P2 X275 Y70
P3 X155 Y170
P4 X275 Y170
```

Nominal pattern:

```text
120 × 100 mm
```

Originally M6-class.

For D02 prototype design, use:

## four M6 adjustment slots

centred on P1–P4.

Starting slot size:

```text
7 × 14 mm
```

Orient slot directions intelligently to allow approximately:

```text
±3 to ±4 mm
```

assembly alignment.

Do not allow adjustment range to create collision with existing keep-outs.

---

# 20. precision locating strategy

After the C-frame is aligned to:

```text
AX_R = X215/Y115
```

provide two dedicated alignment dowel positions.

Prototype approach:

* clamp and align C-frame;
* verify rounder axis;
* drill/ream dowel holes in assembled condition;
* install stainless dowels;
* subsequent removal/reinstallation returns the frame to alignment.

Starting dowel:

```text
Ø6 mm
```

Final dowel fit to be defined once actual machining process is selected.

Do not place dowel holes collinear.

---

# 21. C-frame precision target

After alignment and dowelling:

target AX_R structural reference:

```text
X215/Y115 ±0.15 mm
```

relative to defined chassis datums.

This is an assembly/alignment target.

Do not expect the raw welded frame itself to achieve this without finish operations.

---

# 22. C-frame critical interface surfaces

Define machined/finished datum interfaces for:

* A07 lower mechanism;
* A08 upper head.

Create:

```text
CF_DATUM_1
CF_DATUM_2
CF_DATUM_3
```

or equivalent 3-2-1 locating philosophy.

Document how upper/lower assemblies inherit rounder alignment.

---

# 23. C-frame weld distortion

Codex must include manufacturing notes requiring:

* fixture before welding;
* balanced weld sequence;
* tack → verify → weld;
* critical holes/features finish-machined after weldment completion.

Generate a recommended welding sequence.

---

# 24. rear structural spine

Design A01-002 as a folded SS304 structural assembly occupying the existing rear region without changing:

```text
sanitary plane Y250
rear body limit Y380
```

Material:

```text
1.5 mm SS304
```

The rear spine shall support:

* A03 drive adapter;
* A04 drive adapter;
* A10 electrical hardware later;
* rear cover;
* cable management;
* upper chassis stiffness.

Prefer one main folded U/hat-channel structure plus local brackets.

---

# 25. purchase-dependent drive interfaces

A03 and A04 motors/gearboxes remain PURCHASE-DEPENDENT.

Therefore:

DO NOT laser permanent motor-specific mounting patterns directly into major structural panels.

Instead create removable adapter interfaces:

```text
A01-015 A03 adapter carrier
A01-016 A04 adapter carrier
```

Carrier plates mount to standard structural hole/slot patterns.

Later D03/D04 may replace only adapter plates when actual motors are selected.

---

# 26. adapter carrier approach

Suggested:

* 2.0 or 3.0 mm SS adapter plate;
* bolted to rear spine;
* generic adjustment slots;
* enough envelope for D01-approved motors;
* no exposed fastener thread into wet zone.

Do not finalize actual motor-shaft coupling dimensions in D02.

---

# 27. shaft penetration interfaces

A03/A04 shaft penetrations through sanitary boundary must remain compatible with:

* A03 retractable dog coupling;
* A04 feeder drive;
* future sanitary seal housings.

In D02:

create replaceable **seal-interface plates** rather than making highly specific seal geometry permanent in the sanitary wall.

This allows D03/D04 to select final seals.

---

# 28. A01-005 / A01-006 side panels

Left and right outer panels:

```text
SS304
1.0 mm
```

They are:

* cosmetic;
* protective;
* removable for servicing.

They are NOT structural references for A07/A08.

Use formed returns for stiffness.

Avoid excessive fastener count.

---

# 29. panel attachment

Preferred:

* M4/M5 captive threads;
* rivet nuts only in dry zones;
* quarter-turn fasteners where genuinely useful;
* captive screws for service covers.

Do not use loose nuts that can fall into the machine during service.

---

# 30. rear service cover

A01-007:

```text
SS304
1.0 mm
```

Must permit access to:

* A03/A04 drives;
* A10 hardware;
* wiring;
* terminal region.

Use a removable or hinged panel.

D02 should preserve at least the previously required rear service access concept.

---

# 31. ventilation provisions

Do not finalize fan model.

Preserve D01 ventilation zones.

Create guarded/louvered structural openings only as provisional interface geometry.

No cooling path may communicate directly with the food zone.

---

# 32. front service door

A01-008 shall preserve the validated clear opening:

# 320 W × 330 H mm

Approximate D01 region:

```text
X55 → X375
Z115 → Z445
```

Do not reduce this validated clear opening.

Cartridge and weigh-cup service paths must continue to pass.

---

# 33. front door construction

Preferred prototype:

* formed SS304 frame;
* 1.0 mm sheet skin/frame;
* clear non-food-contact inspection panel;
* stainless hinge;
* positive latch;
* interlock mounting provision.

Inspection panel may be represented using:

```text
3–4 mm polycarbonate placeholder
```

Exact grade remains purchase-dependent.

---

# 34. door hinge

Design hinge geometry so that open door does not obstruct:

* tray removal;
* cartridge extraction;
* weigh-cup extraction;
* normal cleaning sequence.

Re-run service checks.

Provide at least:

```text
~110° opening
```

if packaging permits.

---

# 35. dry-zone splash protection

Create overlapping panel returns/drip lips around:

* front service-door perimeter;
* side covers;
* rear cover.

The machine is not being designed for pressure washing.

But ordinary wiping, splash and food-handling contamination should not have a direct gravity path into electronics/belts.

---

# 36. control fascia carrier

HMI and E-stop remain PURCHASE-DEPENDENT.

Do not commit the main chassis to one display model.

Create:

## A01-014 removable control fascia carrier

located around the D01 front-control region.

It should accept a replaceable inner cutout plate later.

This allows HMI replacement without remanufacturing major chassis parts.

---

# 37. HMI/E-stop D01 envelopes

Maintain existing accepted positions/envelopes.

Do not change the hopper service clearance.

Rev-A1 service trajectory currently passes with approximately:

```text
40.50 mm minimum fixed-hardware clearance
```

and A03 disengaged coupling with:

```text
10.53 mm clearance
```

D02 panels must not reduce these below:

```text
10 mm preferred
5 mm absolute service minimum
```

unless explicitly documented.

---

# 38. cable gland interface

Create A01-017 removable cable/gland interface plate.

Reason:

D12 will determine actual cable sizes and gland counts.

Do not drill irreversible arbitrary gland patterns in the main sanitary wall or rear spine.

---

# 39. external corners and edges

Avoid exposed sharp corners.

For folded external sheet:

prefer:

```text
edge radius / hem / closed return
```

as practical.

Minimum exposed edge treatment:

```text
deburr + break sharp edge
```

Use hems where they improve handling safety without trapping food.

---

# 40. bend design

For D02 design geometry:

use an initial SS304 inside bend radius approximately:

```text
R_i ≈ 1.0–1.5 × sheet thickness
```

unless geometric constraints require otherwise.

However:

## DO NOT treat generic K-factor flat patterns as final shop-release flat patterns.

Create a central parameter for:

```text
BEND_RADIUS
K_FACTOR
```

and document that actual bend compensation must be replaced by the selected fabricator's press-brake/tooling data before final cutting.

---

# 41. preliminary flat patterns

You MAY generate preliminary DXF flat patterns for DFM and quotation.

Mark them:

# PRELIMINARY — VERIFY BEND ALLOWANCE WITH FABRICATOR

Do not label them RELEASED FOR CUTTING until bend data is confirmed.

---

# 42. recommended bend simplification

Prefer:

* common bend radii;
* common V-die-compatible bends;
* 90° bends;
* minimal special tooling.

Avoid:

* tiny return flanges impossible to press;
* bends too close to cutouts;
* unnecessary compound bends.

Flag every questionable bend in:

```text
docs/D02_DFM_REPORT.md
```

---

# 43. welding design

Create explicit joint types.

Use:

## W1 — Wet-zone continuous TIG

for permanent sanitary seams.

## W2 — Structural continuous/controlled TIG

where load path requires.

## W3 — Dry-zone stitch weld

where adequate and distortion reduction is beneficial.

## W4 — Tack only / later finish weld

for assembly-fixture sequence.

Create weld map.

---

# 44. weld finishing

Wet-zone seams:

* continuous;
* no obvious pinholes;
* remove sharp undercut/projections;
* grind/blend where necessary for cleaning.

Do not aggressively thin structural sheet solely to make cosmetic welds invisible.

Dry structural welds do not require cosmetic polishing unless exposed.

---

# 45. passivation

D02 manufacturing notes should specify:

* remove fabrication contamination;
* remove significant weld discoloration in wet-zone stainless;
* passivate affected SS304 surfaces after fabrication/finishing according to the fabricator's qualified process.

Do not prescribe an unsafe chemical recipe.

---

# 46. fastener philosophy

Structural dry side:

```text
M4
M5
M6
M8 feet
```

Preferred stainless fasteners.

No exposed loose hardware in food path.

Where daily cleaning occurs:

avoid threaded fasteners.

Those interfaces belong primarily to A02–A09 but D02 must not obstruct them.

---

# 47. general prototype tolerances

Use project-level candidate tolerances unless a feature explicitly overrides:

## Laser-cut profile

```text
±0.20 mm
```

## Bend-to-bend / formed sheet features

```text
±0.50 mm
```

## Bend angle

```text
±0.5°
```

## Welded chassis overall

```text
±1.0 mm
```

## Interface mounting holes

```text
±0.20 mm
```

## Finish-machined C-frame locating features

```text
±0.10 mm
```

## AX_R aligned condition

```text
±0.15 mm
```

Do not apply ±0.1 mm to ordinary sheet-metal dimensions.

---

# 48. datums

Create a practical D02 manufacturing datum scheme.

Suggested:

## Datum A

principal structural base reference.

## Datum B

machine centre plane X215.

## Datum C

front structural reference Y0 or a physically measurable derived front datum.

For C-frame alignment establish dedicated secondary datums tied to AX_R.

Drawings must make datum transfer physically achievable in a normal workshop.

---

# 49. structural load philosophy

Primary rounder load path:

```text
A08 upper head
↓
A01-009 C-frame
↑
A07 lower rounder
↓
A01 base reinforcement
↓
feet
↓
countertop
```

Do NOT route rounder reaction forces through:

* cosmetic side panels;
* front door;
* HMI fascia;
* thin sanitary wall alone.

---

# 50. structural analysis

Perform a first-pass static structural analysis using conservative simplified loads.

This need not be formal certification FEA.

At minimum evaluate:

* approximately 10 N upper forming force;
* rounder dynamic excitation;
* motor/belt reaction;
* hopper static load approximately 4 kg mixture;
* reasonable manual service loads.

Because real loads are still development-dependent, use a conservative factor.

Report:

* maximum displacement;
* likely weak regions;
* whether local reinforcement is advisable.

Do not fabricate precision claims from crude simulation.

---

# 51. deck stiffness check

Apply a representative manual/service vertical load around the rounder deck and demonstrate that local deflection is unlikely to consume the existing:

```text
4 mm minimum boss/deck clearance
```

If a simple simulation shows excessive deck flex:

add dry-side reinforcement.

Do not move the rounder axis.

---

# 52. door/load check

Check that:

* door does not sag unreasonably;
* hinge attachment does not distort 1 mm skin;
* latch area is locally reinforced if needed.

---

# 53. A01 mass properties

Because D02 now uses actual sheet/plate thicknesses, calculate a realistic A01 mass.

Report separately:

```text
base pan mass
rear spine mass
sanitary wall/deck mass
C-frame mass
outer panels mass
door mass
reinforcements mass
total A01 mass
```

Do not extrapolate this into complete machine mass yet because other subassemblies remain provisional.

---

# 54. fabrication BOM

Generate:

```text
manifest/D02_A01_BOM.csv
manifest/D02_A01_BOM.yaml
```

Fields:

```text
part_id
description
quantity
material
thickness
manufacturing_process
raw_blank_size
finished_mass
make_or_buy
finish
drawing_number
revision
notes
```

---

# 55. sheet nesting data

Calculate approximate required SS304 sheet area by thickness:

```text
1.0 mm
1.2 mm
1.5 mm
2.0 mm
4.0 mm plate
```

Do not optimize commercial sheet nesting unless a nesting library is available.

Provide total area + 15% prototype scrap allowance separately.

---

# 56. drawing set

Generate a D02 drawing package with at least:

```text
D02-01 A01 General Chassis Assembly

D02-02 A01-001 Base Pan

D02-03 A01-002 Rear Structural Spine

D02-04 A01-003 Sanitary Partition

D02-05 A01-004 Rounder Sanitary Deck

D02-06 A01-009 C-frame Side Plates/Crossmembers

D02-07 A01-009 C-frame Weldment + Finish Operations

D02-08 Left/Right Panels

D02-09 Rear Service Cover

D02-10 Front Service Door

D02-11 Control Fascia Carrier

D02-12 Feet/Reinforcement Details

D02-13 Chassis Weld Map

D02-14 Chassis Assembly Sequence

D02-15 Interface Control Drawing
```

---

# 57. each manufacturing drawing

Include as applicable:

* part number;
* revision;
* material;
* thickness;
* quantity;
* units;
* datums;
* critical dimensions;
* general tolerance;
* bend lines;
* bend direction;
* inside radius;
* weld note;
* surface/finish note;
* deburr instruction;
* mass;
* make/buy status.

---

# 58. sheet-metal DXFs

Generate one DXF per valid planar flat pattern.

Naming:

```text
A01-001_REV_A1_D02_FLAT.dxf
```

etc.

Again:

If bend allowance uses generic values, mark:

```text
PRELIMINARY_DFM
```

in filename or manifest status.

---

# 59. STEP exports

Generate:

```text
A01_D02_CHASSIS.step
```

and individual STEP files for each fabricated part/weldment.

Also regenerate:

```text
LADDOOMAKER_D02_REVIEW.step
```

with D02 A01 geometry inserted into the accepted D01 Rev-A1 assembly.

---

# 60. D01 regression

All relevant D01 acceptance checks must be rerun against the detailed D02 chassis.

At minimum:

* machine outer envelope;
* AX_R;
* AX_D;
* sanitary plane;
* A03/A04 locations;
* hopper S4 service trajectory;
* weigh-cup removal;
* cartridge removal;
* ejector clearance;
* belt/chassis clearance;
* wiring keep-outs;
* door opening;
* tray extraction.

D02 may not invalidate a D01 PASS without documenting a design issue.

---

# 61. additional D02 checks

Create:

```text
D02C01 base pan vs A07 lower mechanism
D02C02 C-frame vs A07 full orbit
D02C03 C-frame vs A08 full Z travel
D02C04 sanitary deck vs orbital boss
D02C05 rear spine vs A03 drive
D02C06 rear spine vs A04 drive
D02C07 panels vs wiring keep-outs
D02C08 service door vs cartridge removal
D02C09 service door vs weigh-cup removal
D02C10 hopper S4 vs detailed sheet edges
D02C11 foot hardware vs internal mechanisms
D02C12 C-frame alignment adjustment range
```

---

# 62. alignment procedure

Document a prototype alignment procedure.

Suggested workflow:

1. place chassis on level surface;
2. level base using feet;
3. install C-frame loosely using four M6 slots;
4. establish chassis datums;
5. position C-frame to AX_R X215/Y115;
6. tighten bolts lightly;
7. verify perpendicularity/upper-lower axis;
8. torque mounting bolts;
9. drill/ream two dowel locations in assembled condition;
10. install dowels;
11. re-check axis;
12. record actual measured values.

Generate:

```text
docs/D02_ALIGNMENT_PROCEDURE.md
```

---

# 63. welding/assembly procedure

Generate:

```text
docs/D02_CHASSIS_ASSEMBLY.md
```

Recommended sequence must minimize distortion.

At minimum consider:

1. laser cut;
2. deburr;
3. form panels;
4. inspect individual parts;
5. fixture base/rear spine;
6. tack;
7. measure diagonals/datums;
8. weld in balanced sequence;
9. install sanitary deck/wall;
10. weld wet-zone seams;
11. fabricate C-frame separately;
12. finish-machine C-frame critical interfaces;
13. install/align/dowel C-frame;
14. clean welds;
15. passivation;
16. install removable panels/hardware.

---

# 64. prototype vs production classification

Every D02 output must classify parts as:

```text
PROTOTYPE_RELEASE_CANDIDATE
```

or:

```text
PROVISIONAL
```

Do not call anything final production tooling.

---

# 65. items remaining provisional after D02

Do NOT falsely freeze:

* exact A03 motor mounting holes;
* exact A04 motor mounting holes;
* final shaft seals;
* exact HMI cutout;
* exact electrical glands;
* final fan openings;
* bellows supplier;
* production bend compensation before fabricator data.

Use replaceable adapter plates/interfaces.

---

# 66. fabricator RFQ package

Create:

```text
exports/D02_Rfq_Package/
```

containing:

* chassis STEP;
* drawing PDFs if drawing exporter exists;
* DXFs;
* BOM;
* material summary;
* weld map;
* finish notes;
* DFM questions;
* preliminary flat-pattern disclaimer.

Also generate:

```text
docs/D02_FABRICATOR_RFQ_NOTES.md
```

---

# 67. DFM questions for fabricator

Include questions such as:

1. Are all bends possible on your tooling?
2. What inside radius will you use for each sheet thickness?
3. What bend allowance/K-factor does your shop use?
4. Can the C-frame weldment be fixture-welded and finish-machined?
5. Which weld seams are likely to distort?
6. Can wet-zone seams be continuously TIG welded and blended?
7. Are any cutouts too close to bend lines?
8. Can all specified materials be supplied with traceable SS304 grade?
9. Which design changes would significantly reduce fabrication cost?
10. What dimensional inspection can you provide?

---

# 68. do not release cutting files automatically

Even if DXF export succeeds:

Do NOT mark D02:

```text
RELEASED FOR FABRICATION
```

until:

* geometry passes validation;
* we review the drawings;
* fabricator provides bend/tooling feedback.

Use:

```text
D02 DETAIL DESIGN — DFM REVIEW
```

status first.

---

# 69. D02 acceptance conditions

D02 can be accepted for FABRICATOR DFM when:

* A01 contains realistic sheet/plate geometry;
* all sheet thicknesses assigned;
* C-frame is manufacturable;
* alignment/dowel strategy is present;
* all D01 regressions pass;
* S4 hopper removal still passes;
* cartridge/weigh-cup service still passes;
* A07/A08 interfaces remain aligned;
* preliminary DXFs generated;
* welding map generated;
* BOM generated;
* realistic A01 mass generated;
* no unresolved structural collision exists.

---

# 70. acceptance response

At completion return:

## D02 BUILD STATUS

## A01 PART COUNT

## A01 TOTAL MASS

## MATERIAL SUMMARY BY THICKNESS

## C-FRAME ALIGNMENT METHOD

## C-FRAME EXPECTED ADJUSTMENT RANGE

## D01 REGRESSION RESULTS

## D02 COLLISION RESULTS

## STRUCTURAL/DEFLECTION FINDINGS

## WELD/DFM WARNINGS

## PRELIMINARY DXF STATUS

## STEP EXPORT PATH

## RFQ PACKAGE PATH

## DESIGN ISSUES

Then choose exactly:

**D02 ACCEPTED FOR FABRICATOR DFM REVIEW**

or

**D02 REQUIRES REVISION**

Do NOT begin D03 automatically.

---

# 71. required document updates

Update:

```text
docs/DESIGN_DECISIONS.md
docs/DESIGN_ISSUES.md
docs/REVISION_HISTORY.md
docs/INTERFACE_CONTROL.md
```

Add:

```text
docs/D02_MANUFACTURING_SPEC.md
docs/D02_DFM_REPORT.md
docs/D02_ALIGNMENT_PROCEDURE.md
docs/D02_CHASSIS_ASSEMBLY.md
docs/D02_VALIDATION_REPORT.md
docs/D02_FABRICATOR_RFQ_NOTES.md
```

Do not overwrite D01 validation history.

---

# 72. important engineering rule

If manufacturability requires changing a LOCKED D01 feature:

STOP.

Create a design issue.

Do not modify D01 silently.

D02 is permitted to engineer provisional A01 geometry but not alter the accepted process architecture.

---

# 73. execution instruction

Do the work now.

Inspect the existing A01 implementation.

Refactor it into actual manufacturable sheet/plate parts.

Run CAD generation.

Run regression checks.

Generate drawings/data/STEP/DXF/BOM.

Fix CAD/programming errors.

Do not fix engineering conflicts by changing locked D01 dimensions.

Stop after the D02 acceptance gate.

The objective is:

# a real chassis/base manufacturing design that can be reviewed by a laser-cut/bend/TIG/CNC fabricator — not merely a more detailed rendering.
