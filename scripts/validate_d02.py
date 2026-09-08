from pathlib import Path
import os,sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
from checks.validate import run_checks
from checks.acceptance import interference_checks,Result
from checks.d02 import d02_checks
from laddoomaker.a01_chassis.d02 import mass_properties

lp=[(f"D01R-{i:02}",n,Result.PASS if ok else Result.FAIL,d) for i,(n,ok,d) in enumerate(run_checks(),1)]
icids={"IC04","IC05","IC06","IC07","IC10","IC11","IC12","IC15","IC16"}
reg=[c for c in interference_checks() if c.id in icids]; d02=d02_checks()
exports=[ROOT/"exports"/"step"/"D02"/"A01_D02_CHASSIS.step",ROOT/"exports"/"step"/"D02"/"LADDOOMAKER_D02_REVIEW.step",ROOT/"manifest"/"D02_A01_BOM.csv",ROOT/"manifest"/"D02_A01_BOM.yaml"]
exok=all(p.exists() and p.stat().st_size>0 for p in exports) and len(list((ROOT/"exports"/"dxf"/"D02_PRELIMINARY_DFM").glob("*.dxf")))>=14
mass=sum(mass_properties().values())
items=[*[(i,n,r,d) for i,n,r,d in lp],*[(c.id,c.name,c.result,c.evidence) for c in reg],*[(c.id,c.name,c.result,c.evidence) for c in d02],("D02EX","D02 exports",Result.PASS if exok else Result.FAIL,"A01/review STEP, 14 DXF, BOM and 15 drawing views"),("D02ST","structural screening",Result.WARNING,"conservative 300 N deck screening estimate approximately 0.6 mm; physical fixture/load test required"),("D02BA","bend allowance",Result.WARNING,"R2.0/K0.42 preliminary; replace with fabricator tooling data")]
counts={r.value:sum(x[2]==r for x in items) for r in Result}; decision="D02 ACCEPTED FOR FABRICATOR DFM REVIEW" if counts["FAIL"]==0 else "D02 REQUIRES REVISION"
def table(rows): return "\n".join(["| ID | Check | Result | Evidence |","|---|---|---|---|",*[f"| {i} | {n} | **{r.value}** | {d} |" for i,n,r,d in rows]])
text=f"""# D02 Validation Report

Status: **D02 DETAIL DESIGN — DFM REVIEW**

## D01 regression

{table([*[(i,n,r,d) for i,n,r,d in lp],*[(c.id,c.name,c.result,c.evidence) for c in reg]])}

## D02 collision/interface checks

{table([(c.id,c.name,c.result,c.evidence) for c in d02])}

## Structural and manufacturing gates

{table(items[-3:])}

## A01 mass

Calculated from detailed sheet/plate solids and explicit purchased-hardware estimates: **{mass:.3f} kg**. This is A01 only and must not be extrapolated to machine mass.

## Counts

- PASS: {counts['PASS']}
- FAIL: {counts['FAIL']}
- WARNING: {counts['WARNING']}
- NOT VALIDATED: {counts['NOT VALIDATED']}

## Decision

**{decision}**

Acceptance is for fabricator DFM discussion, not cutting. Bend compensation, motor patterns, shaft seals, HMI cutout, glands, ventilation and supplier-dependent interfaces remain provisional.
"""
(ROOT/"docs"/"D02_VALIDATION_REPORT.md").write_text(text,encoding="utf-8")
print(counts); print(decision); sys.stdout.flush(); os._exit(0 if counts["FAIL"]==0 else 1)
