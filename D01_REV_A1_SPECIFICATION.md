# LADDOOMAKER MINI — D01 REV-A1

Continue the EXISTING Rev-A CadQuery repository.

Do not rebuild the project.

Do not start D02–D12.

Do not change locked product axes, machine envelope or process geometry unless explicitly authorized below.

The objective is to resolve the D01 acceptance blockers and return either:

**D01 REV-A1 ACCEPTED FOR DETAIL DEVELOPMENT**

or a documented reason why Rev-A2 is necessary.

---

# 1. Preserve all locked geometry

The following remain locked:

* body: 430 × 380 × 625 mm
* centre plane: X215
* rounder axis: X215/Y115
* dosing axis: X215/Y205
* sanitary wall: Y250
* nominal ball centre: Z178
* lower cartridge datum: Z150
* sanitary rounder deck: Z120
* orbit radius: 3.00 mm
* upper-head total usable travel: 55 mm
* feeder axis: Z375
* agitator axis: Z455
* G1: Z340
* G2: Z285
* transfer chute outlet: X215/Y155/Z208
* chute terminates at Y155
* hopper top and throat geometry

Do not alter these merely to obtain PASS results.

---

# 2. Fix A03 coordinate implementation first

Audit the existing STEP/source geometry for A03.

The authoritative A03 agitator axis is:

X = 215
Z = 455
shaft parallel to Y

Its intended food-side active region is approximately:

Y = 125 → 245

The current exported STEP appears to contain an agitator-shaft-like solid at approximately:

X = 209 → 221
Y = 5 → 125
Z = 449 → 461

This appears inconsistent with D01.

Determine whether this solid is A03.

If yes:

correct the CAD implementation to the authoritative coordinates.

Do NOT change D01 to match the incorrect model.

Also audit A04 feeder shaft/rotor placement against:

feeder axis Z375
active rotor approximately Y170 → 240
dosing centre Y205.

Create:

DI-005 — A03/A04 shaft coordinate audit

and resolve it before continuing.

---

# 3. Redesign A03 drive interface for hopper removal

The hopper must not require removal of a long horizontal agitator shaft through an inaccessible front opening.

Use this Rev-A1 architecture:

* agitator shaft remains captured in/removable with the hopper-side food assembly;
* dry-side agitator motor remains behind the sanitary wall;
* provide a retractable axial dog coupling between hopper agitator and dry-side drive;
* coupling retracts sufficiently into the dry side before hopper lifting;
* hopper-side shaft must be clear of the sanitary wall after coupling release.

Model a conceptual retractable coupling with:

minimum axial disengagement target:
15–20 mm

The exact production coupling remains PROVISIONAL.

The service sequence becomes:

1. machine isolated;
2. hopper emptied;
3. lid released/removed as necessary;
4. agitator drive dog disengaged/retracted;
5. hopper clamps released;
6. hopper lifted;
7. hopper translated forward.

Validate this actual sequence.

---

# 4. Resolve DI-003 — hopper/HMI collision

Do NOT move the locked process axes.

Do NOT immediately relocate the HMI.

The existing +30 mm Z then -100 mm Y removal trajectory is no longer mandatory.

Use a higher vertical lift before forward translation.

Start with:

**+175 mm Z**

followed by:

**-100 mm Y**

This is permitted as a Rev-A1 SERVICE-TRAJECTORY change.

Check the complete swept volume, not merely the endpoint.

Validate against:

* HMI
* emergency stop
* chassis
* feeder
* A03 coupling
* sanitary wall
* other fixed hardware

Required minimum clearance after disengagement:

≥5 mm

Prefer:

≥10 mm where reasonably achievable.

Also verify the entire lifted hopper remains inside the previously reserved approximately 180 mm overhead service envelope.

If +175 mm does not provide sufficient robust clearance, determine the minimum vertical lift required up to the available service envelope and report it.

Do not move HMI unless vertical-lift solution cannot work.

Update:

DI-003

with actual minimum clearance.

---

# 5. Add missing hopper-removal collision test

Create:

IC16 — hopper vs A03 agitator/coupling during service removal

This test must include the full swept trajectory.

PASS is only allowed after A03 drive disengagement is represented.

---

# 6. Detail lower moving boss / sanitary deck interface

Resolve the geometry ambiguity responsible for IC05.

Use the following PROVISIONAL Rev-A1 starting geometry:

Rounder axis:
X215/Y115

Deck:
Z120

Moving boss nominal OD:
**Ø38 mm**

Deck aperture nominal:
**Ø52 mm**

Orbit:
±3 mm X/Y

This produces:

* 7 mm radial static clearance at nominal centre;
* approximately 4 mm minimum boss-to-aperture clearance at full 3 mm orbital displacement.

Model:

* moving boss;
* deck aperture;
* boss upper cartridge interface;
* bellows inner seat;
* bellows outer/deck seat.

Starting bellows interface:

inner sealing land around:
Ø42 mm

outer/deck seat around:
Ø72 mm

effective flexible height:
approximately 20–25 mm

The detailed elastomer convolution remains PROVISIONAL / SUPPLIER-DEPENDENT.

Geometrically prove:

* no metal-to-metal boss/deck collision through full orbit;
* bellows envelope has room for ±3 mm;
* food zone remains isolated from lower mechanism.

Update IC05 accordingly.

Do not claim elastomer fatigue or sanitary certification has been validated.

---

# 7. Detail ejector / cartridge interaction

Resolve IC04.

Preserve:

ejection direction = +X.

The pusher must contact the ball while clearing the lower cartridge rim.

Use a first Rev-A1 development geometry approximately:

pusher thickness:
8 mm

pusher Y width:
20–25 mm

contact height:
approximately 16 mm

pusher lowest working surface:
**Z ≥178 mm**

lower cartridge maximum fixed rim top target:
**Z ≤175 mm**

Therefore maintain at least:

**3 mm nominal vertical hardware clearance**

between cartridge rim and pusher.

Use a broad curved/concave ball-contact face rather than a point contact.

The exact contact curvature remains TEST-DEPENDENT.

Run ejector sweep for:

C34
C40
C46
C52

and verify at:

S3 ejection.

Report minimum hardware clearance.

If the above simple pusher cannot clear all four cartridges, do not move the rounder axis.

Instead propose a relieved/crescent pusher geometry and document it.

---

# 8. Detail A07 belt/pulley drive

IC06 must no longer remain NOT VALIDATED.

Model a provisional real belt drive.

Starting specification:

belt type:
HTD 3M-class

belt width:
9 mm

motor pulley:
20T

eccentric-shaft pulley:
24T

target ratio:
1.20:1 reduction

Use a generic 40–60 W / 24 V BLDC envelope.

Find a motor-axis location inside the existing lower dry chamber that:

* clears the C-frame;
* clears the XY carriage;
* clears the eccentric counterweight;
* clears the enclosure;
* allows belt installation/tensioning.

Do not alter AX_R.

The exact motor manufacturer remains PURCHASE-DEPENDENT.

Model:

* both pulleys;
* belt solid/envelope;
* tensioning allowance;
* motor mounting slots/adjustment envelope.

Run IC06 as a real intersection test.

---

# 9. Detail feeder rotor enough for IC07

The feeder remains DEVELOPMENT_COMPONENT but it must have enough actual geometry for collision checking.

Starting Rev-A1 values:

shaft:
Ø12 mm SS304

shaft direction:
parallel Y

active width:
approximately 70 mm

rotor outside diameter:
**68 mm**

hub OD:
approximately 30 mm

paddles:
4

paddle edges:
rounded

housing radial clearance:
approximately 5 mm

housing internal diameter/envelope:
approximately **78–80 mm**

Maintain large non-grinding clearances.

The hopper throat remains:

110 mm X × 80 mm Y.

Verify:

* rotor/housing fits under throat;
* rotor does not collide with hopper;
* paddles complete 360° rotation;
* shaft/coupling stays correctly positioned relative to Y250 sanitary plane.

IC07 may PASS geometrically while paddle geometry remains TEST-DEPENDENT.

---

# 10. Model wiring keep-outs

Resolve IC15 to at least geometric D01 level.

Do not design complete electrical harnesses yet.

Create explicit KEEP_OUT conduits/cable routes for:

* A03 agitator motor
* A04 feeder motor
* gate actuators
* load cell
* A07 rounder motor
* A08 Z motor/home sensor
* A09 ejector
* HMI
* emergency stop/interlocks

Requirements:

* keep wiring outside exposed food-contact space;
* use sanitary-wall cable glands at defined crossings;
* maintain bend-radius/service-loop volumes;
* no cable keep-out may intersect moving mechanisms in S0–S3;
* keep power wiring separate from the load-cell signal route where practical.

Update IC15 based on actual keep-out solids.

Exact connectors/cable gauges remain D12 work.

---

# 11. Complete normal-cleaning release model

Resolve SV05.

At D01 level, model enough release geometry and extraction paths to prove independent removal of normal food-contact parts.

Include:

* hopper
* hopper-side agitator
* feeder food housing/liner
* feeder rotor where intended
* G1 removable food blade
* weigh cup
* G2 removable food blade
* transfer chute
* C34/C40/C46/C52 upper/lower cartridges
* ejector food pad
* output chute/tray

Use simplified but explicit:

* bayonet
* locating pins
* over-centre clamps
* quick-release couplings

where already specified.

Do not invent screws for daily-clean components.

Generate an updated service sequence in:

docs/SERVICE_ACCESS.md

---

# 12. Treat DI-002 correctly

DI-002 is still open in DESIGN_ISSUES.md and must not disappear from the validation report.

However, it is primarily TEST-DEPENDENT rather than necessarily a D01 spatial blocker.

Perform this envelope validation:

working finished-ball centre range:
Z174–183

ball diameter range:
31–54 mm

Therefore approximate ball top range is:

Z189.5 → 210 mm

Verify that the A08 mechanism can position the upper forming surface throughout the required spatial envelope while retaining:

retracted lowest surface:
Z ≥225

total usable travel:
55 mm

If geometrically sufficient:

change DI-002 status to:

**CONTROLLED — TEST-DEPENDENT / NON-BLOCKING FOR D01**

Do NOT claim cartridge curvature, spring compression or texture performance is validated.

Those remain physical-prototype tasks.

---

# 13. Audit all STEP coordinates after changes

After Rev-A1 build, independently measure bounding boxes/locations from generated geometry.

At minimum verify:

* machine body
* hopper
* A03 shaft
* A04 rotor/shaft
* HMI
* E-stop
* A06 chute
* A07 rounder
* A08 upper head
* output tray

The generated STEP must agree with source parameters.

No "correct parameters but wrong transformed solid" is acceptable.

---

# 14. Repeat all motion states

Regenerate and validate:

S0
S1
S2 0°
S2 90°
S2 180°
S2 270°
S3

Also add:

S4_HOPPER_SERVICE

representing:

* agitator drive disengaged;
* hopper raised to approved Rev-A1 service Z;
* hopper translated forward.

---

# 15. Update validation categories

Re-run:

LP
AB
MV
IC
SV
CT
EX
MC

Add:

IC16 hopper vs A03 coupling/shaft

Add a new category:

## KI — KINEMATIC / SERVICE SEQUENCE

At minimum:

KI01 agitator coupling disengagement
KI02 hopper vertical lift
KI03 hopper forward extraction
KI04 weigh-cup extraction
KI05 cartridge removal
KI06 ejector parking
KI07 G1/G2 removal/service state

---

# 16. Mass/CG

Do not fabricate a mass result.

If current parts remain solid envelope representations rather than realistic sheet-metal shells, MC01/MC02 may remain NOT VALIDATED.

That is acceptable for D01.

Mass/CG is NOT a reason by itself to reject D01 if the model is still explicitly spatial/provisional.

Record this limitation.

---

# 17. D01 Rev-A1 acceptance criteria

D01 Rev-A1 may be ACCEPTED even with TEST-DEPENDENT cartridge/food-performance items open.

But it must have:

PASS:

* hopper service trajectory
* A03 coupling/hopper disengagement
* lower boss/deck hardware clearance
* ejector/cartridge hardware clearance
* belt/pulley/chassis clearance
* feeder rotor/throat hardware clearance
* wiring keep-out/motion clearance
* weigh cup removal
* cartridge removal
* A01-A10 actual build
* required STEP exports

Allowed WARNING:

* elastomer bellows fatigue not tested
* cartridge curvature not food-tested
* spring force not experimentally validated
* feeder paddle effectiveness not food-tested
* ejector surface effectiveness not food-tested

Those belong to physical prototype validation.

---

# 18. Required documents

Update:

docs/DESIGN_ISSUES.md
docs/DESIGN_DECISIONS.md
docs/VALIDATION_REPORT.md
docs/SERVICE_ACCESS.md
docs/INTERFACE_CONTROL.md
docs/REVISION_HISTORY.md

Revision history must add:

## D01 Rev-A1

and list every changed provisional/service geometry.

Do not overwrite the historical Rev-A0 audit record.

---

# 19. Required exports

Generate:

LADDOOMAKER_REV_A1.step

plus A01–A10 STEP files.

Generate updated review views for:

* complete isometric
* transparent enclosure
* X215 section
* Y115 section
* Y205 section
* S0
* S1
* all four S2 quadrant positions where useful
* S3
* S4 hopper service
* lower boss/bellows detail
* belt/pulley detail
* ejector/cartridge detail
* feeder/hopper interface

---

# 20. Final acceptance response

Return:

D01 REV-A1 CAD BUILD STATUS

REV-A0 → REV-A1 CHANGES

PASS / FAIL / WARNING / NOT VALIDATED COUNTS

DI-002 STATUS

DI-003 STATUS

DI-004 STATUS

DI-005 STATUS

HOPPER SERVICE CLEARANCE

LOWER BOSS/DECK MINIMUM CLEARANCE

EJECTOR/CARTRIDGE MINIMUM CLEARANCE

BELT/CHASSIS MINIMUM CLEARANCE

FEEDER/HOUSING MINIMUM CLEARANCE

WIRING KEEP-OUT STATUS

GENERATED STEP PATH

UPDATED VISUAL REVIEW PATHS

Then choose exactly:

**D01 REV-A1 ACCEPTED FOR DETAIL DEVELOPMENT**

or

**D01 REV-A1 REQUIRES REV-A2**

Do not begin D02 automatically.

Perform the work now.
