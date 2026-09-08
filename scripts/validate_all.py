from pathlib import Path
import sys
import os
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
from checks.validate import run_checks
from checks.report import write_acceptance_report

counts,decision=write_acceptance_report(ROOT)
for name, passed, detail in run_checks(): print(f"{'PASS' if passed else 'FAIL'}: {name} ({detail})")
print("ACCEPTANCE:",counts)
print("DECISION:",decision)
sys.stdout.flush()
os._exit(0)
