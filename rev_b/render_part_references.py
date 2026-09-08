"""Render unmodified source tessellation as references for part illustrations."""
from pathlib import Path
import json, os
import vtk
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'part_images';(OUT/'references').mkdir(parents=True,exist_ok=True)
parts=json.loads((ROOT/'output/parts.js').read_text(encoding='utf-8').split('=',1)[1].rstrip(';\r\n '))
catalog=json.loads((ROOT/'explorer/catalog.json').read_text(encoding='utf-8'))
unique={}
for p in catalog['parts']:unique.setdefault(p['typeId'],p)
for p in unique.values():
 raw=next(q for q in parts if q['id']==p['sourceId'])
 points=vtk.vtkPoints()
 for i in range(0,len(raw['vertices']),3):points.InsertNextPoint(*raw['vertices'][i:i+3])
 cells=vtk.vtkCellArray()
 for i in range(0,len(raw['triangles']),3):
  cells.InsertNextCell(3)
  for n in raw['triangles'][i:i+3]:cells.InsertCellPoint(n)
 data=vtk.vtkPolyData();data.SetPoints(points);data.SetPolys(cells)
 normals=vtk.vtkPolyDataNormals();normals.SetInputData(data);normals.SetFeatureAngle(35);normals.Update()
 mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normals.GetOutputPort())
 actor=vtk.vtkActor();actor.SetMapper(mapper)
 actor.GetProperty().SetColor(.66,.7,.72);actor.GetProperty().SetSpecular(.4);actor.GetProperty().SetSpecularPower(35)
 ren=vtk.vtkRenderer();ren.SetBackground(.96,.96,.95);ren.AddActor(actor)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(1024,1024);win.AddRenderer(ren)
 c=[(a+b)/2 for a,b in zip(p['bounds']['min'],p['bounds']['max'])]
 cam=ren.GetActiveCamera();cam.SetFocalPoint(*c);cam.SetPosition(c[0]+1000,c[1]-1400,c[2]+1100);cam.SetViewUp(0,0,1);cam.ParallelProjectionOn();ren.ResetCamera();cam.Zoom(.8)
 win.Render();capture=vtk.vtkWindowToImageFilter();capture.SetInput(win);capture.Update()
 writer=vtk.vtkPNGWriter();writer.SetFileName(str(OUT/'references'/f"{p['typeId']}.png"));writer.SetInputConnection(capture.GetOutputPort());writer.Write();win.Finalize()
print(f'Rendered {len(unique)} unique unmodified CAD references',flush=True)
os._exit(0)
