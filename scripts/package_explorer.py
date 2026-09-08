"""Stage the existing offline viewer for GitHub Pages; no CAD changes."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.site-build'
OUT.mkdir(exist_ok=True)
for name in ('explorer', 'output', 'part_images', 'transform'):
    shutil.copytree(ROOT / 'rev_b' / name, OUT / name, dirs_exist_ok=True)
(OUT / 'index.html').write_text('''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="0;url=transform/">
<title>Laddoo Engineering Explorer</title></head><body>
<a href="transform/">Open Laddoo Transformation Studio</a></body></html>''', encoding='utf-8')
(OUT / '.nojekyll').touch()
print(f'Static site prepared: {OUT}')
