from laddoomaker.model import build_subassemblies
def build():
    a=build_subassemblies(); return {k:a[k] for k in ("A02","A03","A04","A05","A06","A07","A08","A09")}
