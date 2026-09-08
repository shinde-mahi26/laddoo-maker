# D02 Validation Report

Status: **D02 DETAIL DESIGN — DFM REVIEW**

## D01 regression

| ID | Check | Result | Evidence |
|---|---|---|---|
| D01R-01 | overall locked envelope | **PASS** | 430x380x625 |
| D01R-02 | rounder axis | **PASS** | (215, 115) |
| D01R-03 | doser axis | **PASS** | (215, 205) |
| D01R-04 | sanitary plane | **PASS** | 250 |
| D01R-05 | ball centre | **PASS** | 178 |
| D01R-06 | orbit radius | **PASS** | 3.0 |
| D01R-07 | upper travel | **PASS** | 55 |
| D01R-08 | retracted cartridge | **PASS** | 225 |
| D01R-09 | chute termination | **PASS** | 155 |
| D01R-10 | A01-A10 hierarchy | **PASS** | A01, A02, A03, A04, A05, A06, A07, A08, A09, A10 |
| D01R-11 | actual operational X envelope | **PASS** | 0.00..430.00 |
| D01R-12 | actual operational Y envelope | **PASS** | -90.00..380.00 |
| D01R-13 | actual operational Z envelope | **PASS** | 0.00..625.00 |
| IC04 | ejector vs cartridge hardware | **PASS** | minimum hardware clearance 3.00 mm across C34-C52; ball contact face TEST-DEPENDENT |
| IC05 | moving boss vs deck aperture | **PASS** | minimum radial metal clearance 4.00 mm at full 3 mm orbit; intersection 0.000 mm3 |
| IC06 | belt/pulleys vs chassis | **PASS** | minimum chassis clearance 8.50 mm; HTD-3M 20T/24T provisional |
| IC07 | feeder rotor/housing/throat | **PASS** | rotor OD68, housing ID80: radial clearance 6.00 mm; shaft X 209.0..221.0, Y 170.0..240.0, Z 369.0..381.0 |
| IC10 | hopper service vs fixed controls/drives | **PASS** | sampled full +175Z/-100Y path; minimum fixed-hardware clearance 40.50 mm; max overlap 0.000 mm3 |
| IC11 | weigh-cup removal | **PASS** | 100 mm -Y swept endpoint clears C-frame |
| IC12 | cartridge removal | **PASS** | all four maximum envelopes fit the 320 x 330 mm front opening |
| IC15 | wiring keep-outs vs moving mechanisms | **PASS** | 9 explicit D01 routes; moving-envelope intersection 0.000 mm3 |
| IC16 | hopper vs disengaged A03 coupling | **PASS** | 30 mm dog retraction; sampled swept path clearance 10.53 mm; overlap 0.000 mm3 |

## D02 collision/interface checks

| ID | Check | Result | Evidence |
|---|---|---|---|
| D02C01 | base pan vs A07 lower mechanism | **PASS** | intersection 0.000 mm3; clearance 6.50 mm |
| D02C02 | C-frame vs A07 full orbit envelope | **PASS** | intersection 0.000 mm3; clearance 5.00 mm |
| D02C03 | C-frame vs A08 full Z travel | **PASS** | intersection 0.000 mm3; clearance 17.00 mm |
| D02C04 | sanitary deck vs orbital boss | **PASS** | 4.00 mm minimum radial clearance retained |
| D02C05 | rear spine vs A03 drive | **PASS** | clearance 10.00 mm |
| D02C06 | rear spine vs A04 drive | **PASS** | INTENTIONAL INTERFACE CONTACT — PASS: A04 dry motor-envelope rear face Y365 mates the rear-spine structural front face Y365; zero volumetric overlap; final motor bolts remain adapter-dependent |
| D02C07 | panels vs wiring keep-outs | **PASS** | intersection 0.000 mm3 |
| D02C08 | service door vs cartridge removal | **PASS** | validated 320 x 330 mm clear opening preserved |
| D02C09 | service door vs weigh-cup removal | **PASS** | 100 mm -Y route passes through clear opening |
| D02C10 | hopper S4 vs detailed sheet edges | **PASS** | S4 final clearance 41.85 mm; intersection 0.000 mm3; installed sanitary interface excluded from translated-phase test |
| D02C11 | foot hardware vs internal mechanisms | **PASS** | intersection 0.000 mm3 |
| D02C12 | C-frame alignment range | **PASS** | four 7 x 14 mm M6 slots provide +/-3.5 mm primary adjustment; two non-collinear Ø6 dowels lock aligned condition |

## Structural and manufacturing gates

| ID | Check | Result | Evidence |
|---|---|---|---|
| D02EX | D02 exports | **PASS** | A01/review STEP, 14 DXF, BOM and 15 drawing views |
| D02ST | structural screening | **WARNING** | conservative 300 N deck screening estimate approximately 0.6 mm; physical fixture/load test required |
| D02BA | bend allowance | **WARNING** | R2.0/K0.42 preliminary; replace with fabricator tooling data |

## A01 mass

Calculated from detailed sheet/plate solids and explicit purchased-hardware estimates: **20.892 kg**. This is A01 only and must not be extrapolated to machine mass.

## Counts

- PASS: 35
- FAIL: 0
- WARNING: 2
- NOT VALIDATED: 0

## Decision

**D02 ACCEPTED FOR FABRICATOR DFM REVIEW**

Acceptance is for fabricator DFM discussion, not cutting. Bend compensation, motor patterns, shaft seals, HMI cutout, glands, ventilation and supplier-dependent interfaces remain provisional.
