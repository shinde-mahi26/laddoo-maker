from pathlib import Path
import sys,json,os
ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT/'src'),str(ROOT)]
import cadquery as cq
from laddoomaker.model import build_subassemblies
out=[]
for group,assembly in build_subassemblies().items():
    for name,node in assembly.objects.items():
        if node.obj is None or '-KO-' in name or 'paddle_sweep' in name:continue
        shape=node.obj.val() if isinstance(node.obj,cq.Workplane) else node.obj
        vs,ts=shape.tessellate(.6)
        out.append({'group':group,'name':name,'vertices':[round(c,4) for v in vs for c in (v.x,v.y,v.z)],'triangles':[i for t in ts for i in t]})
p=ROOT/'exports'/'operation_video';p.mkdir(exist_ok=True,parents=True)
(p/'cad_meshes.js').write_text('window.CAD_MESHES='+json.dumps(out,separators=(',',':'))+';',encoding='utf-8')
print('CAD mesh objects:',len(out),flush=True);os._exit(0)
