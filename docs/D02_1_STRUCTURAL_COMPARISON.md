# D02.1 Structural Comparison

These are conservative section-property screens, not FEA or modal certification.

| Candidate | C-frame mass | Forming deflection screen | Deck 300 N screen | Base torsion/2 mm foot mismatch | Collision regression | Modal screen |
|---|---:|---:|---:|---:|---|---|
| Baseline | 2.675 kg | <0.06 mm | ~0.6 mm | ~0.05 mm datum shift | PASS | NOT VALIDATED |
| LW1 | 2.288 kg | ~0.075 mm | ~0.6 mm | ~0.08 mm | PASS | NOT VALIDATED |
| LW2 | 2.288 kg SS | ~0.075 mm | ~0.6 mm | ~0.08 mm | PASS | NOT VALIDATED |
| LW3 | 1.780 kg | ~0.095 mm | ~0.6 mm | ~0.12 mm | PASS, 4.24 mm A08 clearance | NOT VALIDATED |

The deck, Ø72 dry-side ring, sanitary wall, AX_R interface pads, four M6 slots and two Ø6 post-alignment dowels remain unchanged. All screens stay below the preferred 0.10 mm C-frame and 1.0 mm deck targets, but LW3 is too close to the screening limits for adoption without FEA and a fixture test.

Orbital excitation is 1.7–5.3 Hz. A reliable natural-frequency prediction is not possible from the current joint/fastener/motor stiffness model: **NOT VALIDATED — PHYSICAL VIBRATION TEST REQUIRED**. Instrumented run-up through 100–320 rpm is mandatory for any selected candidate.

## C-frame options

| Option | Mass | Stiffness/complexity assessment |
|---|---:|---|
| A: existing 4 mm SS | 2.675 kg | Highest stiffness and repeatability; simplest risk profile; greater mass |
| B: 3 mm flanged SS | ~2.14–2.29 kg | Good stiffness if brake-formed accurately; higher bend sensitivity |
| C: 3 mm SS + local 4 mm pads | 2.288 kg | Preferred: preserves machined datums and dowel strategy; moderate welding |
| D: dry aluminium frame | ~0.8 kg geometry-only | Low modulus, galvanic isolation and alignment creep risk; rejected for LW2 |
