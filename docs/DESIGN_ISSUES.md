# Design Issues

## DI-001

**LOCATION:** Toolchain / all assemblies  
**STATE:** All  
**DESCRIPTION:** The initiating workstation exposed Python 3.11 and no CadQuery installation, while the authoritative toolchain requires Python 3.12 and CadQuery 2.8.x.  
**LOCKED PARAMETERS INVOLVED:** CAD technology.  
**OBSERVED CONFLICT:** Geometry and exports cannot be verified until the pinned environment is installed.  
**PROPOSED OPTION A:** Provision Python 3.12 through `uv` and sync the pinned dependencies.  
**PROPOSED OPTION B:** Use a dedicated Conda environment with the same versions.  
**RECOMMENDED:** Option A.  
**CAD STATUS:** Original Rev-A geometry preserved.

**STATUS:** RESOLVED — pinned Python 3.12.11 and CadQuery 2.8.0 environment installed.

## DI-002

**LOCATION:** A08 upper cartridge vs nominal ball centre  
**STATE:** S2 Forming  
**DESCRIPTION:** A locked 55 mm head travel from the minimum retracted lower surface Z225 reaches Z170, while the nominal finished-ball centre is Z178. Cartridge depth/working compression is development geometry, so final contact geometry cannot yet be proven for all cartridge sizes.  
**LOCKED PARAMETERS INVOLVED:** 55 mm travel; Z178 ball centre; retracted surface Z225 minimum.  
**OBSERVED CONFLICT:** Exact forming closure depends on unresolved cartridge curvature and spring compression.  
**PROPOSED OPTION A:** Retain the envelope and validate with cartridge prototypes.  
**PROPOSED OPTION B:** Define cartridge-specific installed offsets after D01 review.  
**RECOMMENDED:** Preserve locked travel and add cartridge interface trials.  
**CAD STATUS:** Original Rev-A geometry preserved.

**STATUS:** CONTROLLED — TEST-DEPENDENT / NON-BLOCKING FOR D01. The Z225-to-Z170 usable envelope covers the calculated ball-top range Z189.5–210; curvature, spring compression and surface performance remain prototype tests.

## DI-003

**LOCATION:** A02 hopper removal vs A10 HMI  
**STATE:** Hopper service configuration  
**PROBLEM:** The actual +30 mm Z then -100 mm Y hopper endpoint intersects the HMI envelope.  
**LOCKED PARAMETERS INVOLVED:** Hopper geometry; required removal movement; body envelope.  
**MEASURED INTERFERENCE:** IC10 reports approximately 13,581 mm³ against the conservative HMI envelope.  
**OPTION A:** Change the service trajectory or use a removable/hinged HMI arrangement without moving locked process axes.  
**OPTION B:** Repackage the HMI inside its allowed front-control region after human-factor review.  
**RECOMMENDED RESOLUTION:** Rev-A1 service-layout study with purchased HMI dimensions, followed by explicit approval.  
**REV-A1 RESOLUTION:** Authorized service trajectory changed to +175 mm Z then -100 mm Y. A03/A04 provisional motor envelopes were repackaged deeper inside their authorized dry keep-outs. Full path sampling reports 40.50 mm minimum clearance from fixed controls/drives and stays below the Z805 overhead limit.  
**STATUS:** RESOLVED IN D01 REV-A1 — no locked axis/process geometry changed.

## DI-004

**LOCATION:** A07/A09 and lower sanitary deck  
**STATE:** S2 forming and S3 ejection  
**PROBLEM:** Coarse cartridge, pusher, carrier and deck solids cannot distinguish intended product contact from hardware collision; belt/pulley and wiring solids are absent.  
**LOCKED PARAMETERS INVOLVED:** AX_R, Z120 deck, Z150 cartridge datum, 3 mm orbit, +X ejection.  
**MEASURED INTERFERENCE:** IC04 and IC05 report envelope overlaps; they are not accepted as physical clearances.  
**OPTION A:** Detail the moving boss, bellows seat, cartridge rim and ejector pad interfaces.  
**OPTION B:** Validate those interfaces with a dedicated test fixture before freezing geometry.  
**RECOMMENDED RESOLUTION:** Option A followed by prototype test evidence.  
**REV-A1 RESOLUTION:** Added Ø38 boss, Ø52 deck aperture, Ø42/Ø72 bellows seats, 8 × 22 × 16 mm pusher, 3 mm rim clearance, HTD-3M belt drive, feeder rotor/housing and nine wiring keep-outs. IC04/05/06/07/15 now pass geometrically.  
**STATUS:** CONTROLLED FOR D01 — hardware spatial blockers resolved; bellows fatigue/sanitary certification and food-handling performance remain TEST-DEPENDENT.

## DI-005 — A03/A04 shaft coordinate audit

**LOCATION:** A03 agitator and A04 feeder transformed solids  
**STATE:** S0–S4  
**PROBLEM:** CadQuery `XZ` positive extrusion produced decreasing-Y shafts: A03 approximately Y5–125 and A04 Y100–170 despite correct parameter intent.  
**LOCKED PARAMETERS INVOLVED:** A03 X215/Z455/Y125–245; A04 X215/Z375/Y170–240.  
**MEASURED CONDITION:** Rev-A0 STEP/source transform disagreed with D01.  
**OPTION A:** Correct extrusion direction to increasing Y.  
**OPTION B:** Change D01 coordinates to match the error.  
**RECOMMENDED RESOLUTION:** Option A; never alter D01 to conceal transformed-solid errors.  
**REV-A1 RESULT:** A03 bbox X209–221/Y125–245/Z449–461; A04 bbox X209–221/Y170–240/Z369–381.  
**STATUS:** RESOLVED IN D01 REV-A1.

## DI-006 — D02 bend compensation and weld distortion

**LOCATION:** A01 folded sheets and C-frame weldment  
**STATE:** D02 fabricator DFM  
**PROBLEM:** Generic R2.0/K0.42 data and simplified distortion screening are insufficient for cutting release.  
**LOCKED PARAMETERS INVOLVED:** D01 envelope, Y250 wall, Z120 deck and AX_R alignment.  
**OPTIONS:** A — obtain shop tooling/bend tables and update flats; B — prototype coupons and measure developed lengths.  
**RECOMMENDED:** Fabricator feedback plus coupons before any cutting-file release.  
**STATUS:** CONTROLLED — does not block DFM review; blocks fabrication release.

## DI-007 — Functional feasibility review reopens acceptance

**DATE:** 2026-09-06

**LOCATION:** A02–A09 food path and motion, plus A01 interfaces.

**STATE:** S2 forming and S1 loading; target 50 g at 2 pieces/minute.

**OBSERVED CONFLICT:** All four forming cartridge pairs intersect at the four sampled orbit quadrants. C52 overlap is 2899.929 mm³; the previous acceptance checks did not test cup-to-cup interference. The tangent transfer trajectory, incomplete food passages and missing mechanical drive/load paths also prevent functional approval.

**LOCKED PARAMETERS INVOLVED:** 3 mm orbit, Z150 lower mount, Z225 retract, 55 mm stroke, Z178 ball centre, Y155/Z208 chute lip and Y115 rounder axis.

**PROPOSED OPTION A:** Separate revised cup/working-stop and guided-transfer candidates, then prove rounding, dosing and discharge with real 50 g portions before completing manufacturing detail.

**PROPOSED OPTION B:** Retain the exact geometry for archival packaging review only; it cannot be called a functioning mechanism.

**RECOMMENDED:** Option A after recipe definition. Complete findings FR01–FR12 and proposed physical verification gates are in `FEASIBILITY_REVIEW_2026_09_06.md`.

**CAD STATUS:** Approved geometry preserved. Additional inspection exports and independent evidence generated. **FUNCTIONAL ACCEPTANCE BLOCKED; historical spatial passes remain historical results only.**
