from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path[:0]=[str(ROOT/"src"),str(ROOT)]
from checks.validate import write_report
raise SystemExit(0 if write_report(ROOT/"docs"/"VALIDATION_REPORT.md") else 1)
