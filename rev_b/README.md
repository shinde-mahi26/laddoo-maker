# Laddoo Mini Rev B

New engineering explorer: **explorer/index.html**. See **explorer/README.md** for setup, source evidence, continuous explosion, searchable CAD tiles, linked BOM, dimensions and verification. Preview from the project root with `.venv\Scripts\python.exe -m http.server 8767 --bind 127.0.0.1 --directory rev_b`, then open http://127.0.0.1:8767/explorer/. The original viewer below is preserved.

Open **output/index.html** in a WebGL-enabled desktop browser. All dependencies are local. For the running preview, use http://127.0.0.1:8766/ while the local server is active.

- Click any part or choose it from the component menu: automatic zoom, material, dimensions, purpose, drive requirement and individual STEP.
- Change 30/50/100 g, mixture and assumed density: matched cup geometry and cycle estimate update.
- Run/pause/scrub the illustrative operating sequence, explode the assembly, reveal the guard or build it progressively.
- Read **output/DESIGN.md** for the engineering assumptions, motors, control sequence, cleaning, assembly and test plan.
- **output/BOM.csv**, **output/MACHINE_REV_B.step**, **output/C*_*.step**, **output/SIMULATION.json** and **output/VERIFICATION.json** contain the portable outputs.

Rebuild CAD: `.venv\Scripts\python.exe rev_b\build.py`

Verify generated package: `.venv\Scripts\python.exe rev_b\verify.py`

The viewer source is **output/index.html**; the Python builder regenerates CAD, BOM and calculation data without overwriting it. `refine_viewer.py`, `finalize.py` and `repair_encoding.py` are one-time development migration scripts, not rebuild steps.

Scope: new independent concept; earlier Rev-A files have not been modified. This is a digital engineering concept with selected analytical checks. It is not a tested physical prototype, full physics simulation or manufacturing release. See the dossier for explicitly unfinished interfaces and trial gates.
