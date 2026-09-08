CONTINUE THE EXISTING LADDOOMAKER CAD REPOSITORY.

DO NOT START D03 YET.

D01 Rev-A1 remains frozen.

D02 has passed its DFM gate but A01 chassis calculated mass is
20.892 kg.

This is inconsistent with the product objective of a compact,
reasonably movable countertop appliance once the remaining
subassemblies are added.

Create:

D02.1 — A01 LIGHTWEIGHTING / MASS OPTIMIZATION STUDY

Do NOT modify the accepted D02 baseline until the study is reviewed.

==================================================
1. OBJECTIVE
==================================================

Reduce A01 chassis mass substantially while preserving:

- D01 geometry
- all process axes
- service access
- sanitation architecture
- stiffness
- manufacturability
- C-frame alignment
- boss/deck clearance
- hopper service trajectory
- A07/A08 mounting interfaces

Current A01 mass:

20.892 kg

Preferred target:

12–14 kg

Stretch target:

10–12 kg

Maximum preferred candidate:

15 kg

Do NOT achieve mass reduction by compromising food-zone hygiene
or reducing required clearances.

==================================================
2. FIRST PRODUCE MASS BREAKDOWN
==================================================

Before redesigning anything, calculate mass contribution for every
A01 part.

Provide table:

PART ID
DESCRIPTION
MATERIAL
THICKNESS
AREA/VOLUME
MASS
% OF A01 TOTAL

Sort descending by mass.

Identify the top 5 mass contributors.

Also categorize mass into:

STRUCTURAL
FOOD/WET BARRIER
COSMETIC PANEL
SERVICE PANEL
REINFORCEMENT
HARDWARE

==================================================
3. CREATE THREE CANDIDATES
==================================================

Do not replace D02.

Create three alternate branches/configurations:

A01-LW1
A01-LW2
A01-LW3

--------------------------------
LW1 — OPTIMIZED ALL-SS304
--------------------------------

Keep SS304 everywhere.

Study:

Base:
2.0 mm → candidate 1.5 mm
with local ribs/reinforcement.

Rear spine:
1.5 → candidate 1.2 mm
using folded hat/U-channel stiffness.

Exterior side panels:
1.0 → candidate 0.8 mm
with formed returns.

Rear service cover:
1.0 → candidate 0.8 mm.

Fascia carrier:
1.5 → candidate 1.0–1.2 mm.

C-frame:
study replacing broad 4 mm solid plates with:

3 mm plates
and/or
folded/flanged sections
and/or
local 4 mm interface pads only.

Do not reduce the sanitary deck or wall automatically.

Remove unnecessary solid reinforcement area.

Use lightening cut-outs ONLY in dry structural regions where they:

- do not weaken critical load paths;
- do not create cable hazards;
- do not create sanitation traps;
- remain manufacturable by laser cutting.

--------------------------------
LW2 — HYBRID SS + ALUMINIUM
--------------------------------

Keep SS304 for:

- wet-zone deck
- sanitary partition
- food-zone interfaces
- shafts/seal interfaces
- areas likely to receive cleaning chemicals/product

Allow dry/non-food parts to use appropriate aluminium,
preferably 5052 for folded sheet and 6061 where machined structural
parts genuinely require it.

Candidates:

dry exterior skins
rear service cover
control fascia
selected dry brackets
possibly selected C-frame structural members

Do NOT place aluminium where product or wash-down contamination is
reasonably expected.

Explicitly identify galvanic-isolation requirements at SS/Al joints.

Account for:

- isolation washers
- coatings where appropriate
- corrosion risk
- thermal expansion
- thread durability

Do not use aluminium merely because it is lighter if the resulting
construction is less robust or more expensive.

--------------------------------
LW3 — MINIMUM-MASS STRUCTURAL
--------------------------------

Create a more aggressive but still realistic prototype candidate.

Use:

- folded channels
- ribs
- beads/returns where CAD permits
- localized thick interfaces
- thin skins carrying no precision alignment load

instead of large constant-thickness plates.

Keep all precision A07/A08 interface surfaces sufficiently rigid.

This candidate is exploratory and may be rejected.

==================================================
4. C-FRAME OPTIMIZATION
==================================================

The C-frame is mechanically important.

Do not simply reduce its thickness.

Study alternatives:

A:
existing 4 mm plate

B:
3 mm SS304 flanged geometry

C:
3 mm side plates + localized 4 mm machined interface pads

D:
dry-side aluminium structural option if justified

For each calculate:

mass
estimated bending stiffness
fabrication complexity
weld distortion sensitivity
cost
alignment repeatability

The C-frame must still support the common A07/A08 datum structure.

AX_R aligned target remains:

X215/Y115 ±0.15 mm

The four M6 slots + two post-alignment Ø6 dowels remain unless a
better equivalent alignment strategy is explicitly proposed.

==================================================
5. BASE PAN OPTIMIZATION
==================================================

Study whether:

2.0 mm flat/folded base

can become:

1.5 mm formed base
+
localized 2.0–3.0 mm foot/C-frame pads.

Maintain:

foot locations
C-frame interface
lower dry chamber
A07 clearances

No oil-canning or unacceptable torsional flexibility.

==================================================
6. DO NOT WEAKEN THE SANITARY DECK BLINDLY
==================================================

Current deck:

1.5 mm SS304

Existing structural screening predicts about:

0.6 mm upper-bound local deflection under the conservative 300 N
screening condition.

The moving boss/deck system has:

4.00 mm minimum radial metal clearance.

Study deck lightweighting only if a reinforced geometry provides
equal or better stiffness.

Prefer:

formed returns
dry-side reinforcement ring
small stiffening features

rather than simply thick material.

==================================================
7. STRUCTURAL SCREENING
==================================================

Repeat conservative structural screening for every candidate.

At minimum:

10 N forming load

300 N conservative deck/service screening

4 kg hopper load

rounder excitation/belt reaction

door/hinge loading

reasonable manual handling load

Also add:

BASE TORSION SCREEN

Simulate or conservatively estimate the chassis response when one
foot is approximately 2 mm higher/lower than the others.

We do not want alignment to disappear because the countertop is
slightly uneven.

==================================================
8. CRITICAL DEFLECTION TARGETS
==================================================

Prefer:

rounder datum relative displacement:
<0.15 mm under normal forming load

deck service displacement:
<1.0 mm under 300 N screening

C-frame elastic forming displacement:
<0.10 mm preferred

No design may consume more than 25% of the 4 mm boss/deck clearance
through reasonable structural deformation.

==================================================
9. VIBRATION / RESONANCE SCREEN
==================================================

The orbital rounder will normally operate roughly 180–260 rpm,
with design range around 100–320 rpm.

This corresponds to approximately:

1.7–5.3 Hz operating excitation.

Perform at least a crude modal/natural-frequency screening if
possible.

Avoid a chassis fundamental mode close to the orbital operating
frequency.

If reliable modal calculation is not possible, mark:

NOT VALIDATED — PHYSICAL VIBRATION TEST REQUIRED.

Do not invent results.

==================================================
10. CARRY OVER EVERY D01/D02 COLLISION TEST
==================================================

Repeat:

D01 regression checks

D02C01–D02C12

No lightweight candidate may invalidate an existing PASS.

==================================================
11. CHECK D02C06
==================================================

Current D02 report states:

rear spine vs A04 drive:
PASS
clearance 0.00 mm

Audit this carefully.

If 0.00 mm represents an INTENDED mounting-face contact between
A04 adapter and rear structure:

change the validation wording to:

INTENTIONAL INTERFACE CONTACT — PASS

and explicitly identify the mating surfaces.

If it is not an intentional interface:

0.00 mm is not acceptable.

Create appropriate assembly clearance.

Do not leave ambiguous zero-clearance collision reporting.

==================================================
12. MASS ESTIMATE OF COMPLETE MACHINE
==================================================

Create a first budgeting mass model.

Use:

actual D02/D02.1 chassis mass

plus conservative estimated envelopes for:

A02
A03
A04
A05
A06
A07
A08
A09
A10

Clearly separate:

MEASURED CAD MASS
ESTIMATED FUTURE MASS

Calculate estimated:

dry machine mass

machine + 4 kg mixture

Do not pretend provisional future-subassembly masses are exact.

Preferred product direction:

dry machine approximately ≤25–28 kg if achievable

loaded approximately ≤30–32 kg

If not achievable, report honestly.

==================================================
13. HANDLING
==================================================

Evaluate whether the finished mass permits:

one-person repositioning

versus

two-person lifting.

If expected dry mass exceeds approximately 25 kg, consider in the
product architecture:

- recessed side carrying handles
- hand clearance
- optional small trolley/base
- transport feet/casters

Do NOT add casters automatically.

Recommend only.

==================================================
14. COST COMPARISON
==================================================

For baseline D02 and LW1/LW2/LW3 compare:

material mass
sheet complexity
laser-cut complexity
bending complexity
welding complexity
machining complexity
estimated prototype fabrication cost category

Use:

LOWER
SIMILAR
HIGHER

rather than inventing vendor prices if actual quotations are absent.

==================================================
15. OUTPUT
==================================================

Create:

docs/D02_1_LIGHTWEIGHTING_REPORT.md
docs/D02_1_STRUCTURAL_COMPARISON.md
docs/D02_1_MASS_BUDGET.md
docs/D02_1_DECISION.md

Generate STEP review models:

A01_BASELINE_D02.step
A01_LW1.step
A01_LW2.step
A01_LW3.step

Generate mass table CSV.

Do not generate final laser-cut files yet.

==================================================
16. DECISION MATRIX
==================================================

Score each candidate on:

MASS
STIFFNESS
HYGIENE
FABRICABILITY
COST
ALIGNMENT
SERVICEABILITY
CORROSION RISK
PROTOTYPE RISK

Use 1–5 scoring with written reasoning.

Recommend one candidate.

==================================================
17. DO NOT ALTER BASELINE AUTOMATICALLY
==================================================

D02 remains the accepted DFM baseline.

Do not replace it with LW1/LW2/LW3 until explicitly approved.

==================================================
18. FINAL RESPONSE
==================================================

Return:

BASELINE A01 MASS

TOP FIVE MASS CONTRIBUTORS

LW1 MASS
LW2 MASS
LW3 MASS

ESTIMATED COMPLETE DRY MACHINE MASS FOR EACH

STRUCTURAL SCREEN RESULTS

D01/D02 REGRESSION RESULTS

D02C06 AUDIT RESULT

RECOMMENDED CANDIDATE

REASON

Then choose one:

D02.1 LIGHTWEIGHT CANDIDATE READY FOR APPROVAL

or

D02 BASELINE SHOULD BE RETAINED

Do not begin D03.