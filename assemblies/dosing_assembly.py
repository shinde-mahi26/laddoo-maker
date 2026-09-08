from laddoomaker.model import build_subassemblies
def build():
    a=build_subassemblies(); return {k:a[k] for k in ("A04","A05")}
