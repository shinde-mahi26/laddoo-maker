# LaddooMaker Mini — Rev-A CAD

Parametric mechanical architecture prototype implemented in Python/CadQuery. The engineering specification is authoritative: locked geometry is never silently changed, while provisional and development geometry is labelled in metadata and the design logs.

## Current engineering status — 2026-09-06

Independent review found forming-cup collisions in all four cartridges and incomplete food/drive interfaces. Earlier D01/D02 spatial passes do not prove that the machine functions. The current CAD is **not fabrication-ready**. User target: 50 g each, 2 per minute; recipe and weight tolerance remain unspecified.

See [feasibility review](docs/FEASIBILITY_REVIEW_2026_09_06.md). Generate the measured part catalog and 70 separated review solids with `python scripts/engineering_review.py`; render CAD evidence with `python scripts/render_engineering_review.py`. Open `exports/engineering_review/PART_CATALOG.html` for dimensions, specifications and individual STEP links.

## Toolchain

- Python 3.12
- CadQuery 2.8.x
- millimetres throughout

## Commands

```powershell
uv sync --extra dev
uv run python scripts/build_machine.py
uv run python scripts/validate_all.py
uv run python scripts/export_all.py
uv run pytest
```

Generated neutral files are outputs, never source of truth. This revision stops at D01 spatial/interface review; it does not contain production bend allowances, GD&T, welding symbols, or fabrication drawings.
