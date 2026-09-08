# VALIDATION REPORT — D01 REV-A1 ACCEPTANCE GATE

All geometric PASS results derive from current CadQuery solids or sampled swept paths. Locked product axes and process geometry remain unchanged.

## A. LOCKED PARAMETER VALIDATION

| ID | Validation | Result | Evidence |
|---|---|---|---|
| LP01 | overall locked envelope | **PASS** | 430x380x625 |
| LP02 | rounder axis | **PASS** | (215, 115) |
| LP03 | doser axis | **PASS** | (215, 205) |
| LP04 | sanitary plane | **PASS** | 250 |
| LP05 | ball centre | **PASS** | 178 |
| LP06 | orbit radius | **PASS** | 3.0 |
| LP07 | upper travel | **PASS** | 55 |
| LP08 | retracted cartridge | **PASS** | 225 |
| LP09 | chute termination | **PASS** | 155 |
| LP10 | A01-A10 hierarchy | **PASS** | A01, A02, A03, A04, A05, A06, A07, A08, A09, A10 |
| LP11 | actual operational X envelope | **PASS** | 0.00..430.00 |
| LP12 | actual operational Y envelope | **PASS** | -90.00..380.00 |
| LP13 | actual operational Z envelope | **PASS** | 0.00..625.00 |

## B. ACTUAL ASSEMBLY BUILD

| ID | Validation | Result | Evidence |
|---|---|---|---|
| AB01 | Rev-A1 machine build | **PASS** | 67 real CAD leaf parts |
| AB02 | A01-A10 | **PASS** | 10 actual cq.Assembly subassemblies |

## C. MOTION VALIDATION

| ID | Validation | Result | Evidence |
|---|---|---|---|
| MV01 | S0 home | **PASS** | head retracted, gates closed, ejector parked |
| MV02 | S1 loading | **PASS** | head retracted, G2 open, route clear |
| MV03 | S2 quadrants | **PASS** | 0deg=(218,115); 90deg=(215,118); 180deg=(212,115); 270deg=(215,112) |
| MV04 | S3 ejection | **PASS** | 8 x 22 x 16 mm pusher traverses +X at Z178 |
| MV05 | non-rotating orbit | **PASS** | fixed orientation plus orthogonal X/Y guides |
| MV06 | bellows accommodation | **WARNING** | geometric +/-3 mm room represented; fatigue and sanitary certification not validated |
| MV07 | S4 hopper service | **PASS** | dog +30Y, hopper +175Z/-100Y |

## D. INTERFERENCE VALIDATION

| ID | Validation | Result | Evidence |
|---|---|---|---|
| IC01 | upper cup vs transfer chute | **PASS** | intersection 0.000 mm3; clearance 17.20 mm |
| IC02 | upper cup vs loading corridor | **PASS** | intersection 0.000 mm3 |
| IC03 | ejector vs transfer chute | **PASS** | minimum clearance 29.27 mm |
| IC04 | ejector vs cartridge hardware | **PASS** | minimum hardware clearance 3.00 mm across C34-C52; ball contact face TEST-DEPENDENT |
| IC05 | moving boss vs deck aperture | **PASS** | minimum radial metal clearance 4.00 mm at full 3 mm orbit; intersection 0.000 mm3 |
| IC06 | belt/pulleys vs chassis | **PASS** | minimum chassis clearance 8.50 mm; HTD-3M 20T/24T provisional |
| IC07 | feeder rotor/housing/throat | **PASS** | rotor OD68, housing ID80: radial clearance 6.00 mm; shaft X 209.0..221.0, Y 170.0..240.0, Z 369.0..381.0 |
| IC08 | G1 full travel | **PASS** | wall clearance 25.00 mm |
| IC09 | G2 full travel | **PASS** | wall clearance 80.00 mm |
| IC10 | hopper service vs fixed controls/drives | **PASS** | sampled full +175Z/-100Y path; minimum fixed-hardware clearance 40.50 mm; max overlap 0.000 mm3 |
| IC11 | weigh-cup removal | **PASS** | 100 mm -Y swept endpoint clears C-frame |
| IC12 | cartridge removal | **PASS** | all four maximum envelopes fit the 320 x 330 mm front opening |
| IC13 | ejector vs chassis | **PASS** | C-frame clearance 34.71 mm |
| IC14 | motors vs electrical volume | **PASS** | A03/A04/A07 motor envelopes occupy reserved dry volumes |
| IC15 | wiring keep-outs vs moving mechanisms | **PASS** | 9 explicit D01 routes; moving-envelope intersection 0.000 mm3 |
| IC16 | hopper vs disengaged A03 coupling | **PASS** | 30 mm dog retraction; sampled swept path clearance 10.53 mm; overlap 0.000 mm3 |

## E. SERVICE ACCESS

| ID | Validation | Result | Evidence |
|---|---|---|---|
| SV01 | hopper removal | **PASS** | sampled full +175Z/-100Y path; minimum fixed-hardware clearance 40.50 mm; max overlap 0.000 mm3 |
| SV02 | weigh cup | **PASS** | 100 mm -Y extraction clears frame |
| SV03 | output tray | **PASS** | external -Y extraction clear |
| SV04 | C34-C52 cartridges | **PASS** | front extraction envelopes clear |
| SV05 | normal cleaning releases | **PASS** | explicit clamps, removable blades/cup/chute, keyed cartridges and detachable polymer pad represented at D01 envelope level |

## F. CARTRIDGES

| ID | Validation | Result | Evidence |
|---|---|---|---|
| CT-C34 | C34 upper/lower | **PASS** | range 31-36 mm; upper lowest Z=225.00; ball top envelope 189.5..201.0; separate 30deg keying; curvature TEST-DEPENDENT |
| CT-C40 | C40 upper/lower | **PASS** | range 36-42 mm; upper lowest Z=225.00; ball top envelope 192.0..204.0; separate 30deg keying; curvature TEST-DEPENDENT |
| CT-C46 | C46 upper/lower | **PASS** | range 42-48 mm; upper lowest Z=225.00; ball top envelope 195.0..207.0; separate 30deg keying; curvature TEST-DEPENDENT |
| CT-C52 | C52 upper/lower | **PASS** | range 48-54 mm; upper lowest Z=225.00; ball top envelope 198.0..210.0; separate 30deg keying; curvature TEST-DEPENDENT |

## KI. KINEMATIC / SERVICE SEQUENCE

| ID | Validation | Result | Evidence |
|---|---|---|---|
| KI01 | agitator dog disengagement | **PASS** | 30 mm axial retraction represented before lift |
| KI02 | hopper vertical lift | **PASS** | 175 mm lift; top reaches Z783 including lid, inside Z805 overhead reservation |
| KI03 | hopper forward extraction | **PASS** | 100 mm -Y at full lift, sampled in 5 mm increments |
| KI04 | weigh-cup extraction | **PASS** | 100 mm -Y |
| KI05 | cartridge removal | **PASS** | C34-C52 through front opening |
| KI06 | ejector parking | **PASS** | parked pusher remains outside processing cylinder |
| KI07 | G1/G2 service | **PASS** | removable blade envelopes translate toward -Y |

## SA. STEP/SOURCE COORDINATE AUDIT

| ID | Validation | Result | Evidence |
|---|---|---|---|
| SA01 | machine body | **PASS** | X 0.0..430.0, Y -4.0..380.0, Z 0.0..625.0 |
| SA02 | hopper | **PASS** | X 75.0..355.0, Y 65.0..305.0, Z 395.0..600.0 |
| SA03 | A03 shaft | **PASS** | X 209.0..221.0, Y 125.0..245.0, Z 449.0..461.0 |
| SA04 | A04 shaft | **PASS** | X 209.0..221.0, Y 170.0..240.0, Z 369.0..381.0 |
| SA05 | HMI | **PASS** | X 40.0..170.0, Y 5.0..15.0, Z 470.0..560.0 |
| SA06 | E-stop | **PASS** | X 330.0..370.0, Y -10.0..30.0, Z 500.0..535.0 |
| SA07 | A06 chute | **PASS** | X 180.0..250.0, Y 155.0..205.0, Z 198.0..278.0 |
| SA08 | A07 rounder | **PASS** | X 155.0..280.0, Y 55.0..175.0, Z 43.0..175.0 |
| SA09 | A08 head | **PASS** | X 155.0..275.0, Y 55.0..155.0, Z 225.0..290.0 |
| SA10 | output tray | **PASS** | X 85.0..345.0, Y -90.0..90.0, Z 75.0..80.0 |

## EX. EXPORT VALIDATION

| ID | Validation | Result | Evidence |
|---|---|---|---|
| EX01 | mandatory STEP | **PASS** | 11/11 present |
| EX02 | prototype STL | **PASS** | 12 files |
| EX03 | Rev-A1 visual review | **PASS** | 17 CAD-derived SVG files |

## MC. MASS/CG

| ID | Validation | Result | Evidence |
|---|---|---|---|
| MC01 | dry mass/CG | **NOT VALIDATED** | spatial purchased envelopes and provisional solids are not realistic manufacturing mass geometry |
| MC02 | 4 kg loaded CG | **NOT VALIDATED** | depends on reliable dry mass/CG; non-blocking for D01 |

## H. DESIGN ISSUES

| ID | Validation | Result | Evidence |
|---|---|---|---|
| DI-002 | forming envelope | **WARNING** | CONTROLLED - TEST-DEPENDENT / NON-BLOCKING: 55 mm travel spans Z225 to Z170 and covers ball-top envelope Z189.5..210 |
| DI-003 | hopper/HMI service | **PASS** | RESOLVED by authorized +175Z/-100Y trajectory; 40.50 mm minimum fixed-hardware clearance |
| DI-004 | moving interfaces | **WARNING** | CONTROLLED: hardware clearances pass; bellows fatigue, food-contact performance and spring behavior remain physical tests |
| DI-005 | A03/A04 coordinate audit | **PASS** | RESOLVED: A03 Y125..245 and A04 Y170..240; axes agree with source and STEP audit |

## RESULT COUNTS

- PASS: 68
- FAIL: 0
- WARNING: 3
- NOT VALIDATED: 2

## D01 REV-A1 ACCEPTANCE

**D01 REV-A1 ACCEPTED FOR DETAIL DEVELOPMENT**

Test-dependent warnings remain for cartridge/food behavior, bellows fatigue/sanitary certification, spring force and feeder/ejector effectiveness. These do not claim physical validation and do not block D01 spatial detail development. D02-D12 have not begun.
