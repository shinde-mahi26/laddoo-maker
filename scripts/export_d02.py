from pathlib import Path
import csv,json,os,shutil,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
import cadquery as cq, yaml
from laddoomaker.a01_chassis.d02 import build_a01,build_parts,mass_properties,flat_patterns,PART_RECORDS,BEND_RADIUS,K_FACTOR,STATUS
from laddoomaker.model import build_machine
from laddoomaker.parameters.motion_states import State

step=ROOT/"exports"/"step"/"D02"; dxf=ROOT/"exports"/"dxf"/"D02_PRELIMINARY_DFM"; drawings=ROOT/"exports"/"drawings"/"D02"; rfq=ROOT/"exports"/"D02_Rfq_Package"
for p in (step,dxf,drawings,rfq): p.mkdir(parents=True,exist_ok=True)
parts=build_parts(); masses=mass_properties(); flats=flat_patterns()
cq.exporters.export(build_a01().toCompound(),str(step/"A01_D02_CHASSIS.step"))
cq.exporters.export(build_machine(State.S0_HOME).toCompound(),str(step/"LADDOOMAKER_D02_REVIEW.step"))
for name,shape in parts.items(): cq.exporters.export(shape,str(step/f"{name}.step"))
for pid,data in flats.items(): cq.exporters.export(data["shape"],str(dxf/f"{pid}_REV_A1_D02_PRELIMINARY_DFM.dxf"))

record_by_id={r.part_id:r for r in PART_RECORDS}; rows=[]
for r in PART_RECORDS:
    matches=[v for k,v in masses.items() if k.startswith(r.part_id)]
    mass=sum(matches)
    rows.append({"part_id":r.part_id,"description":r.description,"quantity":r.quantity,"material":r.material,"thickness":r.thickness,"manufacturing_process":r.process,"raw_blank_size":r.blank,"finished_mass_kg":round(mass,3),"make_or_buy":r.make_or_buy,"finish":r.finish,"drawing_number":f"D02-{min(len(rows)+2,15):02}","revision":"Rev-A1/D02","classification":r.classification,"notes":STATUS})
fields=list(rows[0])
with (ROOT/"manifest"/"D02_A01_BOM.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
(ROOT/"manifest"/"D02_A01_BOM.yaml").write_text(yaml.safe_dump({"status":STATUS,"bend_radius_mm":BEND_RADIUS,"k_factor_preliminary":K_FACTOR,"parts":rows},sort_keys=False),encoding="utf-8")
areas={}
for data in flats.values(): areas[data["thickness"]]=areas.get(data["thickness"],0)+data["width"]*data["height"]/1e6
summary={str(k):{"net_m2":round(v,3),"with_15pct_scrap_m2":round(v*1.15,3)} for k,v in sorted(areas.items())}
(ROOT/"manifest"/"D02_MATERIAL_AREA.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

def svg(name,shape,d=(1,-1,1)):
    cq.exporters.export(shape,str(drawings/f"{name}.svg"),opt={"projectionDir":d,"showAxes":False,"width":1400,"height":1000,"marginLeft":50,"marginTop":50})
drawing_map=[("D02-01_A01_GENERAL",build_a01().toCompound()),("D02-02_BASE_PAN",parts["A01-001_base_pan"]),("D02-03_REAR_SPINE",parts["A01-002_rear_spine"]),("D02-04_SANITARY_PARTITION",parts["A01-003_sanitary_partition"]),("D02-05_ROUNDER_DECK",parts["A01-004_food_deck"]),("D02-06_CFRAME_PLATES",cq.Compound.makeCompound([parts["A01-009_cframe_left"].val(),parts["A01-009_cframe_right"].val()])),("D02-07_CFRAME_WELDMENT",cq.Compound.makeCompound([parts[k].val() for k in parts if k.startswith("A01-009")])) ,("D02-08_SIDE_PANELS",cq.Compound.makeCompound([parts["A01-005_left_enclosure"].val(),parts["A01-006_right_enclosure"].val()])),("D02-09_REAR_COVER",parts["A01-007_rear_cover"]),("D02-10_FRONT_DOOR",cq.Compound.makeCompound([parts["A01-008_front_door_frame"].val(),parts["A01-008P_inspection_panel"].val()])),("D02-11_FASCIA",parts["A01-014_fascia_carrier"]),("D02-12_FEET_REINFORCEMENT",cq.Compound.makeCompound([parts["A01-010_reinforcement_set"].val(),parts["A01-011_feet_set"].val()])),("D02-13_WELD_MAP",build_a01().toCompound()),("D02-14_ASSEMBLY_SEQUENCE",build_a01().toCompound()),("D02-15_INTERFACE_CONTROL",cq.Compound.makeCompound([parts["A01-004_food_deck"].val(),parts["A01-009_cframe_left"].val(),parts["A01-009_cframe_right"].val()]))]
for n,s in drawing_map: svg(n,s)

disclaimer="PRELIMINARY - VERIFY BEND ALLOWANCE WITH FABRICATOR. NOT RELEASED FOR CUTTING.\n"
(dxf/"PRELIMINARY_FLAT_PATTERN_DISCLAIMER.txt").write_text(disclaimer,encoding="utf-8")
rfq_sources=[step/"A01_D02_CHASSIS.step",ROOT/"manifest"/"D02_A01_BOM.csv",ROOT/"manifest"/"D02_A01_BOM.yaml",ROOT/"manifest"/"D02_MATERIAL_AREA.json",ROOT/"docs"/"D02_MANUFACTURING_SPEC.md",ROOT/"docs"/"D02_DFM_REPORT.md",ROOT/"docs"/"D02_ALIGNMENT_PROCEDURE.md",ROOT/"docs"/"D02_CHASSIS_ASSEMBLY.md",ROOT/"docs"/"D02_STRUCTURAL_SCREENING.md",ROOT/"docs"/"D02_VALIDATION_REPORT.md",ROOT/"docs"/"D02_FABRICATOR_RFQ_NOTES.md"]
for source in rfq_sources:
    if source.exists(): shutil.copy2(source,rfq/source.name)
for source in dxf.glob("*"): shutil.copy2(source,rfq/source.name)
for source in drawings.glob("*.svg"): shutil.copy2(source,rfq/source.name)
(rfq/"PACKAGE_STATUS.txt").write_text(STATUS+"\n"+disclaimer,encoding="utf-8")
print(f"D02 exports complete: {len(parts)} solids, {len(flats)} preliminary DXFs, {len(drawing_map)} drawings, A01 mass {sum(masses.values()):.3f} kg")
sys.stdout.flush(); os._exit(0)
