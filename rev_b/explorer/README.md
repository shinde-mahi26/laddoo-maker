# Laddoo / Engineering explorer

An offline, editable Three.js explorer of the existing **Rev-B concept**, using its 46 physical CAD instances (39 matching name/material/dimension types). The original Rev-A files, Rev-B builder, baseline CAD, tooling variants and older viewer are preserved.

## Start

From the project root in PowerShell:

```powershell
.venv\Scripts\python.exe -m http.server 8767 --bind 127.0.0.1 --directory rev_b
```

Open **http://127.0.0.1:8767/explorer/**. No npm install, build step, network dependency or API key is required. Keep the `explorer` and `output` directories beside each other. Opening `explorer/index.html` directly also works in browsers allowing local scripts and WebGL.

## Controls

- Drag to orbit; shift-drag or right-drag to pan; wheel or +/− buttons to zoom. Keyboard arrows orbit; R resets; Escape assembles.
- Front, side and top use orthographic cameras. ISO returns to perspective.
- The 0–100% slider separates the whole machine or the chosen source subassembly. It is an inspection layout, not a validated disassembly path.
- Select a solid, tree row, CAD tile or BOM row for the same stable instance ID. Transparent parts remain selectable. Hide or isolate obstructing components to reach interior components.
- Isolate exposes a separate Z-rotation slider. Dimensions and extension lines follow that part. Return to assembly restores the original pose and hidden items; Reset also clears selection, filters and display settings.
- All parts provides scrollable source-CAD preview tiles, names, IDs and bounding-box sizes. Previews are fitted independently to their tiles, not to a common scale. Selecting a tile opens that component in the interactive viewport. Click All parts again to return to the atlas.
- BOM supports search, repeated-type grouping, instance selection and a full-instance CSV export with millimetres, revision and evidence columns. The displayed group count is not a count of final procurement items.
- On mobile, Components and Inspector open collapsible panels. Close Inspector to regain the full viewport; use the zoom buttons for touch zoom.

## Source and evidence

`../build.py` and `../output/DESIGN.md` document the existing Rev-B mechanism. `../output/parts.js` supplies the exact existing tessellated vertices, triangles, source group and motion assignments. No generic mechanism or reconstructed photographs were used. The explorer uses the baseline Ø46 inserts. A link retains access to the earlier configurable 30/50/100 g tooling viewer.

All geometry is in **millimetres**, explicitly mapped with `POSES.UNIT = 1`. Meshes are centered locally, with the corresponding center retained as their immutable assembled position. The source's semantic assembly groups are preserved in the records and tree. Repeated identical local geometry is shared between physical mesh instances; selections remain per instance.

Dimensions are **CAD bounding boxes calculated from the supplied concept**, not fabrication dimensions. Known cavity/shaft/sheet features are listed separately and marked documented concept. Three-axis dimension lines always show the source bounding box, even during explosion; normal orthographic projection can make a depth-axis line appear end-on. Feature tolerances are not invented.

Existing motors, rails, support and electronics envelopes remain envelopes. Documented material choices and process instructions do not prove that a manufactured machine exists. Mass is unknown. Generic procurement notes are retained verbatim where applicable; they are not supplier selections. Missing individual maintenance/removal/cleaning instructions remain “Not specified.” The dossier contains the wider commissioning and validation plan.

Still required: supplier/model selections and mounting patterns; finished bearing/shaft/seal/fastener interfaces; per-part masses; toleranced drawings; complete guards and wiring; measured feeding, dose accuracy, forming and release trials. The six-step motion is illustrative commanded movement, not collision/food/physics validation. It makes no measured production-rate claim.

## Files and regeneration

| File | Purpose |
| --- | --- |
| `index.html`, `style.css`, `app.js` | Editable interface, rendering and interaction |
| `transforms.js` | Explicit units, assembly centers, explosion and grid targets |
| `catalog.json` / `catalog.js` | Structured evidence and stable instance/type IDs |
| `BOM.csv` | Full instance BOM with units and revision |
| `meshes/RB-*.stl` | Visualization tessellations, original assembly coordinates, mm |
| `../output/*.step` | Original supplied concept CAD, unchanged |
| `../prepare_explorer.py` | Catalog and visualization-mesh processing script |
| `../verify_explorer.py` | Independent CAD, units, hash and mesh verification |
| `asset-verification.json` | Per-part downloadable-asset check results |

Run `.venv\Scripts\python.exe rev_b\prepare_explorer.py` after intentionally rebuilding source CAD. The preparation script never rebuilds or alters source CAD. Source IDs receive an `RB-` namespace; matching type IDs receive `RBT-`. Unknown fields have explicit null/source or “Not specified” values. For additional documented feature metadata, edit the preparation script's evidence mapping before regenerating.

STEP files are linked in their original format and assembly coordinates. STL is binary visualization geometry with a millimetre header (STL has no standardized unit field); consumers must explicitly import as mm. No mesh is renamed STEP. Original full assembly and alternate cup STEP files remain in `../output/`.

## Verification

```powershell
node --check rev_b/explorer/app.js
node --check rev_b/explorer/transforms.js
.venv\Scripts\python.exe rev_b/verify_explorer.py
```

Open **http://127.0.0.1:8767/explorer/?verify** for opt-in integration checks against the running renderer. In about 25 seconds it displays a JSON report covering actual transforms, exact reassembly, scoped explosion, selection synchronization, dimensions, isolation, independent rotation, visibility, grid separation, search and reset. Reload the normal URL to leave test mode. These are viewer tests only.

Bundled Three.js is reused under `../output/THREE_LICENSE.txt`. Its legacy-script deprecation notice is expected; the explorer makes no external script or font requests. Browser fullscreen support depends on the host and gives a useful message when unavailable.
