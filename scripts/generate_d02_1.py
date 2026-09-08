from pathlib import Path
import csv,os,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
import cadquery as cq
from laddoomaker.a01_chassis.d02 import build_a01,build_parts,mass_properties,PART_RECORDS,DENSITY_KG_MM3
from laddoomaker.a01_chassis.d02_1 import CANDIDATES,build_candidate,build_approved_a01,candidate_masses
from laddoomaker.model import build_machine

out=ROOT/"exports"/"step"/"D02_1"; out.mkdir(parents=True,exist_ok=True)
cq.exporters.export(build_a01().toCompound(),str(out/"A01_BASELINE_D02.step"))
for code in CANDIDATES: cq.exporters.export(build_candidate(code).toCompound(),str(out/f"A01_{code}.step"))
cq.exporters.export(build_approved_a01().toCompound(),str(out/"A01_LW2_APPROVED.step"))
cq.exporters.export(build_machine().toCompound(),str(out/"LADDOOMAKER_D02_1_LW2_REVIEW.step"))

desc={r.part_id:(r.description,r.material,r.thickness) for r in PART_RECORDS}; masses=mass_properties(); parts=build_parts(); total=sum(masses.values())
category={"001":"STRUCTURAL","002":"STRUCTURAL","003":"FOOD/WET BARRIER","004":"FOOD/WET BARRIER","004R":"FOOD/WET BARRIER","005":"COSMETIC PANEL","006":"COSMETIC PANEL","007":"SERVICE PANEL","008":"SERVICE PANEL","008P":"SERVICE PANEL","009":"STRUCTURAL","010":"REINFORCEMENT","011":"HARDWARE","012":"HARDWARE","013":"HARDWARE","014":"SERVICE PANEL","015":"REINFORCEMENT","016":"REINFORCEMENT","017":"REINFORCEMENT"}
rows=[]
for name,mass in masses.items():
    token=name.split("_")[0]; pid=token.replace("A01-004R","A01-004") if token=="A01-004R" else token
    d=desc.get(pid,(name,"SS304",0)); volume=parts[name].val().Volume(); area=volume/d[2] if d[2] else 0
    catkey=token.split("-")[1]
    rows.append({"part_id":token,"description":d[0],"material":d[1],"thickness_mm":d[2],"area_mm2":round(area,1),"volume_mm3":round(volume,1),"mass_kg":round(mass,4),"percent_total":round(100*mass/total,2),"category":category.get(catkey,"REINFORCEMENT")})
rows.sort(key=lambda r:-r["mass_kg"])
with (ROOT/"manifest"/"D02_1_BASELINE_MASS_BREAKDOWN.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
allrows=[]
for code in CANDIDATES:
    for pid,v in candidate_masses(code).items(): allrows.append({"candidate":code,"part_id":pid,"material":v["material"],"category":v["category"],"volume_mm3":round(v["volume_mm3"],1),"mass_kg":round(v["mass_kg"],4)})
with (ROOT/"manifest"/"D02_1_CANDIDATE_MASS_TABLE.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=list(allrows[0])); w.writeheader(); w.writerows(allrows)
print("D02.1 STEP and mass tables generated:",", ".join(f"{c}={sum(v['mass_kg'] for v in candidate_masses(c).values()):.3f}kg" for c in CANDIDATES))
sys.stdout.flush(); os._exit(0)
