"""Render actual CAD meshes, with no generated illustrative geometry."""
from pathlib import Path
import sys,os
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/'src'),str(ROOT)]
import cadquery as cq
import vtk
from laddoomaker.model import build_subassemblies
from laddoomaker.a07_orbital_rounder.cartridges import installed_cartridge
OUT=ROOT/'exports'/'engineering_review'
def actor(shape,rgb,opacity=1):
    vs,ts=shape.tessellate(.5)
    points=vtk.vtkPoints()
    for v in vs: points.InsertNextPoint(v.x,v.y,v.z)
    cells=vtk.vtkCellArray()
    for tri in ts:
        cells.InsertNextCell(3)
        for i in tri: cells.InsertCellPoint(i)
    data=vtk.vtkPolyData(); data.SetPoints(points); data.SetPolys(cells)
    mapper=vtk.vtkPolyDataMapper(); mapper.SetInputData(data)
    a=vtk.vtkActor(); a.SetMapper(mapper); a.GetProperty().SetColor(*rgb); a.GetProperty().SetOpacity(opacity)
    return a
def render(items,title,path,labels=()):
    ren=vtk.vtkRenderer(); ren.SetBackground(.95,.96,.97)
    for shape,rgb,opacity in items: ren.AddActor(actor(shape,rgb,opacity))
    for label,pos in labels:
        text=vtk.vtkBillboardTextActor3D(); text.SetInput(label);text.SetPosition(*pos)
        text.GetTextProperty().SetFontSize(20);text.GetTextProperty().SetColor(.1,.15,.2);ren.AddActor(text)
    txt=vtk.vtkTextActor();txt.SetInput(title);txt.SetPosition(35,840);txt.GetTextProperty().SetFontSize(24);txt.GetTextProperty().SetColor(.1,.15,.2);ren.AddActor2D(txt)
    win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(1400,900);win.AddRenderer(ren)
    cam=ren.GetActiveCamera();cam.SetPosition(1300,-1800,1200);cam.SetFocalPoint(215,150,300);cam.SetViewUp(0,0,1);cam.ParallelProjectionOn();ren.ResetCamera();cam.Zoom(.85)
    win.Render();capture=vtk.vtkWindowToImageFilter();capture.SetInput(win);capture.Update()
    writer=vtk.vtkPNGWriter();writer.SetFileName(str(path));writer.SetInputConnection(capture.GetOutputPort());writer.Write();win.Finalize()
groups=build_subassemblies();items=[];labels=[]
palette=[(.45,.55,.64),(.81,.66,.37),(.34,.60,.69),(.52,.67,.38),(.65,.49,.75),(.75,.5,.37),(.26,.65,.7),(.7,.45,.62),(.56,.66,.37),(.4,.52,.66)]
for i,(group,asm) in enumerate(groups.items()):
    dx=(i%5)*650; dz=-(i//5)*850
    items.append((asm.toCompound().translate((dx,0,dz)),palette[i],1))
    labels.append((group,(215+dx,-100,660+dz)))
render(items,'LaddooMaker | 10 separated subassemblies | actual CAD / review only',OUT/'SUBASSEMBLIES.png',labels)
lower=installed_cartridge('C52',False,218,115,150).val(); upper=installed_cartridge('C52',True,215,115,170).val()
render([(lower,(.25,.6,.75),.65),(upper,(.8,.6,.25),.65),(lower.intersect(upper),(1,.05,.05),1)],'C52 forming position | red = solid collision (2899.929 mm3)',OUT/'CUP_COLLISION.png')
print('Rendered CAD review and collision evidence',flush=True);os._exit(0)
