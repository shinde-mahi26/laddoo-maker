# Laddoo Mini — Rev B design dossier

6 September 2026 · Independent new concept in `rev_b/` · millimetres unless stated.

## Decision and scope

Use **mass-controlled portioning**, followed by a matched split spherical mould. Presets: **30, 50 and 100 g**. Target 2–4 pieces/minute. Main envelope **600 W × 400 D × 635 H mm**. A 600 mm-deep countertop accommodates 400 mm machine depth plus 100 mm rear service clearance, subject to the actual kitchen. Allow 200 mm overhead for cassette removal; no claim that it fits beneath every wall cabinet. Estimated assembled weight budget 22–30 kg, not a measured BOM mass. Plan two-person installation and a bench rated at least 40 kg for this appliance.

Prepared motichoor, cooked besan/ghee mixture and soft jaggery/peanut mixture are the intended inputs. This machine does not cook, make boondi, roast nuts, grind peanuts or soften hardened chikki. Cohesion and adhesion are the feasibility limits, not electrical power. Initially restrict inclusions to ≤4 mm and manually confirm that a portion can be moulded without crumbling. Working-temperature trial range 25–45°C is an assumption, not a validated recipe specification.

This package is **an end-to-end concept and testable development specification, not a fabrication release or a working physical prototype**. Purchased mechanisms, bearings, couplings, seals, fasteners and electrical modules have functional specifications but not verified manufacturer part numbers or complete manufacturing interfaces. The CAD viewer identifies those envelopes explicitly. Generating STEP files cannot close these gaps.

## Process architecture

1. Lift-off 2 L working-fill hopper supplies a removable low-speed belt. An intermittent soft bridge-breaker prevents some bridging without an auger's high compression; performance must be tested.
2. A scraper feeds a 0.4 L tipping weigh cup. Complete cup, tip servo and cradle sit on the live end of a 2 kg load cell. Stop belt and agitator before accepting a stable weight.
3. Tip the weighed portion vertically into the lower forming cup. Return the weigh cup to home. Do not command the shuttle before cup-home confirmation.
4. Shuttle 160 mm from X270 to X430 beneath the raised head. The lower cup remains upright.
5. Lower the head 95 mm and regulate force through a compression sensor and a spring. No lateral orbit. Matched spherical cavities compress the portion; texture, seam and release remain trial-dependent.
6. Raise fully, then tip the lower cup outward 120° towards the open output chute. Return the cup upright and shuttle home. A stuck portion triggers a stop, not repeated crushing.

The food ball in the animation follows an illustrative path. It is not a simulated discrete-element or viscoelastic food body, and simulated ejection is not evidence of release.

## Portion size and tooling

`diameter_mm = 10 × (6 × mass_g / (pi × density_g_per_cm3))^(1/3)`.

| Mass | Diameter at 0.8 g/cm³ | At 1.0 g/cm³ | At 1.2 g/cm³ |
|---|---:|---:|---:|
| 30 g | 41.53 | 38.55 | 36.28 |
| 50 g | 49.24 | 45.71 | 43.01 |
| 100 g | 62.04 | 57.59 | 54.19 |

These are illustrative densities, not measurements of the three recipes. Tooling range: **Ø36–64 mm in 2 mm steps**, 15 matched upper/lower pairs, all provided as STEP. The main assembly is the Ø46 baseline. The viewer swaps actual alternate CAD meshes when mass/density changes. Selecting the closest cavity is a starting point: a fixed cavity and a fixed mass can disagree. Measure formed density and adjust the recipe or machine a recipe-specific final cavity; never silently change the requested mass to fill a mould. A 2 mm tooling step can change cavity volume appreciably.

Each cup has a 5 mm radial shell and 0.3 mm equatorial relief, yielding a 0.6 mm rigid rim gap. No hard cup overlap is commanded. Actual spherical tolerance, flattening at the seam and flash need trials. Use replaceable food-contact POM-C for the development inserts; obtain declarations for fatty food and operating temperature. Do not use ordinary printed resin or exposed FDM layers for food trials. Alternative polished SS316L inserts may be tested if polymer release or wear is unacceptable.

The food geometry in the presentation remains spherical throughout forming for clarity. It must not be interpreted as proof of the forming physics.

## Drives and load calculations

All power and torque values below are **procurement requirements derived from assumed loads**, not verified vendor selections. Check continuous torque at operating speed, not stall torque or motor wattage alone. Encoders, drivers, duty rating, seals, thermal rise and gearbox backlash must be checked on selected products.

| Axis | Selected architecture | Minimum working specification | Electrical budget |
|---|---|---|---:|
| Agitator | 24 V BLDC gearmotor | 5–15 rpm, ≥3 N·m continuous, current limit | 20 W |
| Metering belt | 24 V BLDC gearmotor | 0–35 rpm, ≥1 N·m continuous, encoder | 25 W |
| Weigh-cup tip | Geared position servo | ≥1.5 N·m continuous, 150° travel | 15 W |
| Shuttle | Closed-loop NEMA17 stepper | ≥0.3 N·m at 200 rpm, 160 mm travel | 30 W |
| Forming head | 24 V screw linear actuator | ≥150 N at 40 mm/s, ≥95 mm stroke | 50 W |
| Lower-cup tip | Geared position servo | ≥2 N·m continuous, 120° travel | 20 W |
| Controls, drivers, sensors allowance | 24 VDC | Includes interface/controller overhead | 35 W |
| Total allocated | | | **195 W** |

Use an enclosed **24 V, 10 A, 240 W** supply. Reserve is 45 W, or 23.1% above the 195 W allocation (18.75% of PSU rating). Peak servo currents may exceed this allocation; verify with selected drives and measured startup before purchase. BLDC is preferred for continuous feeder duty; geared servos and a closed-loop stepper give position control for intermittent axes. A single large motor with cams would make recipe adjustment and fault recovery harder.

**Belt:** assume 20 N tangential resistance at 10 mm radius. Torque 0.20 N·m; factor 2 gives **0.40 N·m**. Specify ≥1 N·m at intended output speed. The factor is not permission to force a jam. Use a lower experimentally calibrated current cutoff.

**Shuttle:** assume 1.5 kg moving mass, 0.5 m/s² acceleration and 8 N friction. Required force 8.75 N. With 9.55 mm pulley radius and factor 2, torque **0.167 N·m**. A 160 mm move in 1.2 s can use a symmetric trapezoid with 0.2 m/s peak speed and 0.5 m/s² acceleration: 0.4 s acceleration, 0.4 s cruise, 0.4 s deceleration. Pulley speed ≈200 rpm. A motor specified only by holding torque is insufficient.

**Press:** at 150 N, 4 mm screw lead and assumed 0.35 efficiency, torque is **0.273 N·m**, screw speed **600 rpm** at 40 mm/s, and input mechanical power **17.14 W**. A 50 W actuator budget leaves allowance for losses, but its simultaneous speed/force rating must be verified. Forming trial force is 10–80 N, hard cutoff 120 N; 150 N is actuator capability. A 5 N/mm spring uses 2–16 mm compression over that trial range. Head geometry and stop stack must be calibrated with each tool pair. Do not assume a screw cannot back-drive; use a brake or positive support for service.

**Tip axes:** assume 0.7 kg cup/cradle at 30 mm eccentricity for the weigh cup: gravity torque ≈0.206 N·m, ×3 ≈0.62 N·m before sticking. Lower tip assumes 0.6 kg at 35 mm: 0.206 N·m, ×3 ≈0.62 N·m. Selected 1.5/2 N·m requirements include provisional margin; adhesion could exceed it and requires a controlled stop. Tip acceleration and gearbox efficiency are not yet measured.

**Agitator:** assume ≤20 N tangential food load at 40 mm radius, or 0.8 N·m; ×2 gives 1.6 N·m. 3 N·m continuous is a procurement ceiling with adjustable current limiting. It is not evidence of flow in jaggery mixtures.

## Cycle budget and sensitivity

Coarse feed `(mass−5)/20` seconds at assumed 20 g/s; fine feed 5 g at 2 g/s; 0.8 s settle; 1.2 s cup tip; 1.2 s transfer; 2.375 s head down; 4 s form; 2.375 s head up; 1.2 s eject; 1.2 s return.

| Mass | Nominal cycle, 4 s form | Estimated rate | With 7 s form |
|---|---:|---:|---:|
| 30 g | 18.10 s | 3.31/min | 2.84/min |
| 50 g | 19.10 s | 3.14/min | 2.71/min |
| 100 g | 21.60 s | 2.78/min | 2.44/min |

Nominal calculations meet the requested **range**, not its maximum at every size. They exclude refill, cleaning, rejects and long weight settling. If a 100 g recipe only feeds at 5 g/s coarse, cycle rises by 14.25 s, giving **1.67/min** with a 4 s form. At 100 g, nominal 4 s forming needs coarse flow ≥7.31 g/s to stay within 30 s; 7 s forming needs ≥9.13 g/s. These are useful feeder bench gates.

The belt width/bed-depth assumption must support that flow: at 100 mm width, 10 mm bed depth, 20 mm/s and 1 g/cm³, ideal flow is 20 g/s before voids/slip. Hopper flow is not guaranteed to maintain that bed.

Weight cutoff should compensate measured in-flight mass and delay. Example: fine flow 2 g/s × 0.15 s latency = 0.30 g before dribble and in-flight material. Proposed acceptance targets: ±2 g for 30/50 g and ±3 g for 100 g, ≥95% of portions. These are targets, not achieved specifications. Accept a reading only when range over a 0.5 s window is ≤0.2 g; require empty tare plausibility and overload detection. A 24-bit ADC does not guarantee accuracy.

## Materials, interfaces and cleaning

`BOM.csv` lists all 46 modelled items, dimensions, material and purpose. Quantity is one per row; repeated feet, rollers and paddles are separate rows. These are CAD items, not a final purchase order. Supplementary procurement list:

- M5/M6/M8 SS A2-70 hardware with captive dry-side nuts; no exposed threads over food. Mould fastening must be captive and positively keyed.
- Four sealed shuttle blocks and two guide rails; dry timing belt, two pulleys, tensioner, home/end flags and cable chain. CAD shows rail and belt envelopes, not catalogue hole patterns.
- Weigh cup: pair of trunnion bearings on the weighed cradle, keyed shaft, motor coupling, flexible cable loop and overload stops. The fixed cell end bolts to frame; live end supports every cup-related load. No hard stop may touch in normal weighing.
- Lower cup: trunnion shaft, pair of bearings, rear offset yoke, keyed insert carrier, home switch. The pedestal in CAD is a support envelope; complete yoke and shaft fits before machining.
- Head: guided anti-rotation actuator, compression sensor, spring, adjustable stop, removable bellows and retention brake. Final joint stack is not released.
- Wet shaft seals: food-contact silicone/EPDM selected for actual fat/temperature/cleaner exposure; external bearings and drip barriers. Food-grade lubricant only in isolated bearings, never intentionally on food.
- Complete side/end guards, hinges, captive latches, coded interlocks and protected output opening. Front sheet is represented; current guard CAD alone is not a complete safe enclosure.

Food-contact metal: SS304 sheet, SS316L shafts; smooth continuous welds, no pits, removable radiused corners, proposed Ra ≤0.8 µm finish. Use certified food-contact PU belt, POM-C cups, PEEK scraper and silicone paddles/liner with supplier declarations. Dry aluminium must be isolated from wet stainless steel with insulating spacers and kept outside wash paths. Finish/tolerance targets are design choices, not certification claims.

Daily cleaning: isolate mains, verify stored motion is safe, remove hopper and belt cassette, lift out weigh cup and both mould inserts, remove chute/tray; wash/rinse/sanitise according to validated recipe/material-compatible procedure, dry completely, reassemble and re-tare. Do not hose the assembled machine. For peanut-to-non-peanut changeover use dedicated removable food kits or validate allergen removal; visual cleanliness alone is insufficient. Provisional teardown target <10 minutes remains untested.

## Controls and electrical architecture

Functional topology (not a certified wiring drawing):

`230 V inlet → disconnect/fuse → earthed 24 V PSU → fused branch circuits → motor drives`

`E-stop + guard channels → monitored safety relay → drive power/enable removal`

`24 V controller → belt / agitator / tip servos / shuttle driver / head driver`

`2 kg load cell → shielded ADC → controller; head force sensor → controller + independent overload cutoff`

Inputs: E-stop feedback, front/side/lid interlocks, weigh-home, shuttle-home, shuttle-press, head-up, head-low, lower-cup-home, tray-present/full, head force, dose mass, motor fault signals. Output wiring: six drive channels, fault lamp/buzzer, UI. Allocate separate fused branches for 50 W head, 30 W shuttle, each 15–25 W axis and logic. Final fuse ratings/wire sizes follow actual cable installation, driver current and selected PSU; they are not inferred from this schematic.

Earthing: mains PE bonds frame and enclosure using dedicated studs; detachable metal panels require bonding. Keep mains in segregated rear compartment with strain relief and touch-safe terminals. A qualified builder must verify earthing, insulation, fault behaviour and applicable Indian requirements before energising. This package makes no BIS/FSSAI/electrical compliance claim.

State sequence: IDLE → TARE → DOSE_COARSE → DOSE_FINE → SETTLE → WEIGH_ACCEPT → TIP → SHUTTLE → LOWER → DWELL → RAISE → EJECT → RETURN. Every commanded motion has timeout and expected sensor feedback. Any interlock loss, overload, unexpected limit state or emergency stop latches FAULT; stop drive energy, retain head safely, require manual reset and re-home. Never automatically resume a partial portion after reset. Reject an overweight dose before forming; design a removable catch/reject cup for commissioning, because automated reject hardware is not in this CAD.

## Assembly and commissioning order

1. Weld/finish base and rear frame in a fixture; confirm flatness and frame squareness. Fit feet.
2. Fit partition and rear enclosure; bond metalwork. Install PSU/drivers/safety modules with mains isolated.
3. Install and align shuttle rails, blocks, belt drive and travel stops. Hand-check the full 160 mm stroke.
4. Install lower-cup trunnion/yoke, servo and keyed tooling. Check tip sweep and cable clearance.
5. Mount press actuator, anti-rotation guides, sensor/spring/retention mechanism. Set hard stop with the largest cavity first.
6. Fit weighed cup cradle and tip axis, then cell to frame. Verify no parasitic contact, set overload stops and calibrate with traceable test masses.
7. Install feed cassette and hopper; verify scraper and shaft clearance by hand. Fit seals and catch trays.
8. Install output chute/tray and complete guards/interlocks. Verify guard reach distances and fault behaviour before enabling motion.
9. Dry-jog at reduced speed, first with no food, then inert test pieces. Recheck all fasteners and current limits.
10. Run food trials per the plan below. Manufacturing drawings and production procurement follow the results.

The viewer's assembly slider progressively adds CAD items. It is a presentation order, not a verified tool-access/removal sequence.

## Simulation evidence and release gates

`SIMULATION.json` is generated from `../build.py`, alongside neutral CAD and meshes. Checks: 15 real solid cup pairs × 7 head clearances (0, 0.5, 1, 5, 20, 50, 95 mm). Maximum rigid cup overlap is zero in those sampled aligned states. Rear support and matched upper spacer are also checked against the nominal food sphere for all 15 sizes; no intrusion is allowed. Visual review exposed an earlier support/rod intrusion; the final revision moves the support behind the cup and terminates the rod above the head load module. This is not an all-part interference audit. Screw torque, belt load, shuttle torque, mass/diameter and serial timing are reproducible algebraic screens. No food constitutive model, FEA or measured force data were supplied, so no successful physical operation is asserted.

Minimum bench trial matrix: 3 mixtures × 3 masses × 30 portions = **270 portions**, record input temperature, density, grain size, target/actual mass, cycle time, peak force, motor current, release failures, shape and breakage. Start with one recipe at 50 g to avoid wasting food; expand after stable operation. Provisional goals: ≥95% within mass tolerance, ≥95% intact release, 2–4/min sustained for 15 minutes at each approved setting; no jam requiring hand access while powered. Inspect texture blind against hand-made samples. Log failed conditions rather than averaging them away.

Before fabrication release: finish bearing/shaft/mould fastener stack, complete guard and seal CAD, verify all moving swept volumes including weigh tip and output path, select actual drives, produce dimensioned toleranced drawings and wiring diagrams, then validate stiffness/thermal/noise/cleaning and fault response. Main development risk is sticky-food feeding and release. If tests fail, revise the feed cassette or add a positive release insert; do not claim the animation proves the mechanism works.

## Primary engineering references

- [Oriental Motor — sizing calculations](https://www.orientalmotor.com/motor-sizing/index.html): selection uses torque, speed and inertia. Used as sizing-method guidance, not a motor endorsement.
- [FDA Food Code 2022, Chapter 4](https://www.fda.gov/files/food/published/FDA-FoodCode2022-FullDocument-01182023_0.pdf): smooth, cleanable food-contact design principles. Reference guidance only, not Indian certification.
- [FDA allergen removal research](https://www.fda.gov/food/retail-food-protection/allergen-removal-and-transfer-using-wiping-and-cleaning-methods-retail-food-establishments): cleaning effectiveness depends on surface/food/procedure; informs peanut changeover validation.

Rebuild from the project root: `.venv\Scripts\python.exe rev_b\build.py`. Open `index.html` locally in a WebGL browser; all graphics dependencies are bundled and no Internet is needed. Local server option: `.venv\Scripts\python.exe -m http.server 8766 --bind 127.0.0.1 --directory rev_b\output`.
