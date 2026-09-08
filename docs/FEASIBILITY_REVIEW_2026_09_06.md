# LaddooMaker Mini — independent feasibility review

Date: 2026-09-06. Basis: approved LW2 CAD at checkpoint e2059b7, source inspection and additional solid-intersection calculations. Scope: engineering feasibility and dimensioned review CAD; no physical machine or food trial has been observed.

## Verdict

A machine that portions and forms a selected laddoo mixture is a credible development project. **This CAD configuration cannot presently be approved as a working machine or sent straight to fabrication.** Its working principle remains test-dependent and its current forming geometry contains a measured collision. Completing manufacture-ready detail before the food process is proven would risk expensive rework.

The earlier 68 D01 and 35 D02 passes did not establish functional feasibility. They cover selected spatial checks, and several are unconditional assertions. In particular, IC04 tests a pusher against lower-cup hardware, not the two forming cups against each other. Motion checks describe commanded transforms rather than a physically constrained drive. The lightweight chassis approval is a configuration choice, not proof of stiffness, sanitation, or production performance.

## Confirmed defects and missing functional interfaces

| ID | Finding from source or geometry | Consequence / required change |
|---|---|---|
| FR01 | C52 lower cup at Z150 and upper cup at Z170 in forming position intersect by approximately 2899.929 mm³ at the 0° orbit position. See exported evidence for all four cartridges/quadrants. | Rigid bodies cannot occupy the same space. Redesign cup rims, mating geometry and/or working head stop in a separately reviewed revision; validate every orbital phase and spring compression. |
| FR02 | Cavity centres are not the nominal finished-ball centre. Lower cavity centre is Z170; upper forming cavity centre is Z175; nominal ball centre is Z178. Lower cup also orbits laterally by 3 mm. | Food-space compatibility cannot be inferred from nominal cavity diameter. Quantify the complete changing gap and food deformation; current nominal-sphere intersections are diagnostics, not a constitutive simulation of food. |
| FR03 | Hopper is a solid loft, with no inner cavity or through throat; A03 has a shaft but no agitator arms. | Model is a packaging envelope. Build hollow 1.2 mm nominal sheet hopper, seams, flange/gasket and removable agitator only after confirming flow and cleanability. |
| FR04 | A04 contains a hub and a cylindrical sweep, not four physical paddles. Housing is an unported annular tube; drive and sanitary shaft interfaces are incomplete. | No continuous hopper-to-weigh-cup food passage or complete torque path is demonstrated. The sweep must not be manufactured. |
| FR05 | Weigh cup is a straight ring without the specified conical lower discharge. Its lower extent is Z290 and G2 top is Z286.5, leaving an unsealed 3.5 mm vertical gap in the represented geometry. | Mixture retention, discharge and weighing load path are unresolved. Cup, gate and any supported actuator mass require a deliberate weighed assembly with no parallel force path. |
| FR06 | Chute is a solid wedge, 10 mm vertical depth, rather than a developed 1 mm sheet channel; it has no sidewall retention or supports. | Dimensioned envelope is not a fabricated chute. Its actual inlet, lip and ball trajectory must be tested. |
| FR07 | Final transfer is 40 mm horizontally forward. A tangent departure follows a 70/50 downward slope, giving at least 56 mm drop before gravity. Lip Z208 to nominal ball-centre Z178 is only 30 mm. | A point particle following the chute tangent cannot reach that nominal centre. Finite ball radius, rolling/contact geometry and possible lip redirection can change the result, so this is a serious transfer-risk screen rather than proof that every real portion misses. A removable guided transfer or a deliberately shaped launch lip requires a separately approved geometric change and testing. |
| FR08 | A07 uses commanded offsets, placeholder guide bars, pulleys and a belt volume. Eccentric, shaft supports, bearing fits and complete drive constraint are absent. A08 has no spring, actuator, guide bearings or stops. | CAD motion is not proof of an assembled mechanism. Complete load paths and torque/force selection after bench results. |
| FR09 | Ejector has a translated pad and output tray, but no actuator/linkage or connecting discharge chute. | Moving the pad does not demonstrate that a ball exits and lands intact on the tray. |
| FR10 | LW2 materials are recorded, but galvanic isolation, detailed joints and structural validation are unresolved. The sanitary partition has no complete sealed shaft/gate interfaces. | Chassis mass is an estimate, not an assembled-machine mass or strength certificate. Detail isolation and verify the structural and hygienic interfaces. |
| FR11 | Several apparent hole cutters use the XY-cylinder helper, whose axis is Z, on plates normal to Y: A03/A04 adapter holes and fascia E-stop opening. | These must be audited/corrected in the detail revision; existing appearance and checks do not establish usable through-holes or a selected motor bolt pattern. |
| FR12 | Only generic electrical envelopes are present. | Functional interlocks, stopped-state access, E-stop behaviour, motor protections, thermal design and commissioning remain unverified. |

No locked dimensions were altered to hide these findings. The approved baseline is preserved, and the review exports expose what exists today.

## Quantitative engineering screens

**Transfer.** With horizontal lip velocity u, point-particle drop at horizontal distance L is `h = 1.4 L + g L²/(2 u²)`. For L=0.040 m, drops are about 252.2, 87.4 and 63.8 mm for u=0.2, 0.5 and 1.0 m/s. These velocities are illustrative, not measured mixture properties. Adhesion and shape further affect departure. A video of a real portion leaving the lip is required.

**Orbital drive.** For radius r=0.003 m, `v=rω` and `a=rω²`. At 100/200/320 rpm the operating frequencies are 1.67/3.33/5.33 Hz, velocities 0.0314/0.0628/0.1005 m/s and accelerations 0.329/1.316/3.369 m/s². Inertial force is those acceleration values multiplied by the entire orbiting mass in kg; mixture forming loads, friction, eccentric bearings and transients must be added. This is not a motor sizing calculation or a modal analysis.

**Head force.** A 1 N/mm spring needs 2–10 mm working compression to produce 2–10 N if preload is zero. Commanded 55 mm travel does not establish working force; free length, preload, hard stops, actual food height and mechanism stiffness must be specified. Test force versus displacement for each recipe before selecting the spring and drive.

**Mass versus diameter.** `d=(6m/(πρ))^(1/3)` with mass in g and density in g/cm³ gives diameter in cm. As an explicitly illustrative density range of 0.8–1.2 g/cm³, 20 g corresponds to about 31.7–36.3 mm, and 60 g to about 45.7–52.3 mm. Actual mixture density must be measured. Mass setting alone cannot select a cartridge or establish forming clearance.

**Dosing overshoot.** Approximate overshoot is `flow rate × control/actuator delay + in-flight material + dribble`. A hypothetical 10 g/s feed and 0.1 s delay already produce 1 g before in-flight mass. Use coarse/fine feed with stable weighing and measured compensation; no accuracy claim is justified by specifying a 1 kg cell.

**Throughput.** For a non-overlapped cycle, `pieces/min = 60/(feed + settle + discharge + transfer + form + retract + eject time)`. None of these durations is measured. Capacity, yield, temperature rise, noise, life and cleaning time remain unknown.

## What the 3D package contains

`exports/engineering_review/PART_CATALOG.html` is a printable visual catalog of every connected solid extracted from the actual S0 machine, excluding wire keep-outs and the rotor motion sweep. Each entry has an individual local-coordinate STEP, isometric CAD drawing, measured X/Y/Z envelope, material/development status and subsystem specifications. `PART_DIMENSIONS.csv` retains installed minimum coordinates so each local part can be placed back into the machine.

`assemblies/ASSEMBLED_REVIEW.step` contains the review assembly; `ALL_PARTS_SEPARATED.step` and A01–A10 separate STEP models lay out the connected solids in a spaced review grid. These are exploded inspection layouts, **not validated removal sequences**. A connected solid can contain multiple welded/fused manufacturing pieces. The number of extracted solids is not the final manufacturing BOM quantity. Hardware sets, food-contact material grades, exact purchased interfaces, bend allowances, tolerances and missing mechanisms are not invented.

The current model can therefore be inspected part by part, but these envelope sheets must not be misrepresented as complete production drawings. A fully specified working model depends on resolving FR01–FR12 and selecting actual components.

## Physical verification programme

The user has specified **50 g each and 2 laddoos per minute**. This permits a 30-second cycle and requires an average product flow of 100 g/min, or 6 kg/hour before rejects and downtime. Recipe, temperature range and acceptable weight tolerance remain unspecified. Use the following as **proposed engineering trial criteria**, not agreed requirements or measured results.

An initial timing allocation to test is: feed 8 s, settle/final trim 3 s, gate/transfer 3 s, form 10 s, retract/eject/reset 4 s, and margin 2 s. This totals 30 s but is a design budget, not achieved performance. Filling 50 g within 8 s requires at least 6.25 g/s net average during feeding, with faster coarse dosing if fine trim consumes part of that time. At the illustrative density range 0.8–1.2 g/cm³, a 50 g sphere is approximately 43.0–49.2 mm diameter, spanning the nominal C46/C52 ranges; recipe density and actual forming behaviour must select the insert. A 4 kg hopper load represents 80 portions and about 40 minutes of ideal operation. Test all initial process gates at 50 g; use other masses only if later requested.

1. **Material characterisation:** record recipe by mass, mixing method, rest time, temperature, density and largest inclusion. Cover at least three independent mixture batches. Measure adhesion, discharge force and forming force at intended minimum/nominal/maximum temperatures.
2. **Rounder first:** use a guarded adjustable bench fixture with replaceable inserts, 3 mm orbit, controllable 100–320 rpm, compliant head, force measurement and current logging. First eliminate all cup collisions in CAD. Trial 20/40/60 g or the user's chosen sizes. Record three-axis dimensions, cracks, smearing, sticking, temperature and release force. Proposed gate: 30 consecutive portions per condition; at least 95% with max/min diameter ratio ≤1.10, no visible cracking and clean release. Reject the principle for any required recipe that cannot pass after controlled insert/force/speed tuning.
3. **Doser and weighing separately:** qualify load-cell mounting and shielding with traceable check masses across the working range. Dose 100 portions per target into an independent balance, at high and low hopper fill and with motors operating. Proposed gate: at least 95% within ±1 g and bias ≤0.5 g; record every outlier and jam. Do not tune by using only a mean value.
4. **Transfer/ejection:** transparent observation access and video of 100 consecutive cycles per tested size/recipe. Record missed capture, breakage, residue and tray landing. Proposed gate: zero missed transfers or manual recoveries in that trial. Include startup, last portion and restart conditions.
5. **Structure:** apply the already proposed 300 N deck test with specified support conditions and measure deflection/permanent set; define allowable values from required process alignment before testing. Measure base torsion and C-frame relative movement under actual forming load. Run instrumented speed sweeps through 100–320 rpm with loaded hopper, monitoring relative cup movement and fastener loosening. No FEA or vibration acceptance is claimed here.
6. **Integrated prototype:** run for one hour at the user-agreed production rate while weighing output independently and counting rejects, jams and interventions. Check power/current, temperatures and stop/restart sequence. Validate lid/door opening and E-stop responses with appropriate qualified supervision before food-production use.
7. **Cleaning and durability:** dismantle and reassemble every wet component; inspect shaft seals, cup/gate junctions, retained product and drain paths. Establish cleaning effectiveness and material compatibility with the intended process; perform repeated cleaning and endurance cycles before release.

A 30- or 100-cycle trial is an initial gate, not long-term reliability proof. No physical gate above has been completed in this review.

## Development recommendation

Proceed with a **process demonstrator**, starting with rounding and release, then dosing and guided transfer. Do not commission the whole enclosure first. If the 3 mm orbital/compliant-cup method cannot reliably form the required mixture, evaluate an alternative rolling mechanism separately instead of forcing the existing architecture through detail design. After process proof, issue a revised interface layout and component selection, then derive dimensioned manufacturing parts, assembly constraints and production drawings from that validated geometry.

## External evidence, checked 2026-09-06

- [Rheon manufacturer overview](https://www.rheon-europe.com/products/encrusting-machines/) documents commercial confectionery/encrusting machinery. It supports the broad feasibility of mechanised food forming, not this compact orbital design or any laddoo recipe.
- [Anton Paar food rheology](https://www.anton-paar.com/ae-en/food-rheology/) identifies texture and flow/yield behaviour as measurable food properties. This supports measuring the actual mixture rather than assuming a universal forming force.
- [HBK PW12C mounting guide](https://www.hbm.com/fileadmin/mediapool/hbmdoc/technical/A06421.pdf) identifies mounting-related force shunts. This is a mounting principle reference, not a selected load cell or accuracy guarantee for this machine.

No vendor quote, selected motor, certified food-contact grade, physical pass, final cost, lifetime or guaranteed output has been fabricated.
