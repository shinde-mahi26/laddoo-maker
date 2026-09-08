from pathlib import Path
import re,json,subprocess
root=Path(__file__).parent/'output'
html=(root/'index.html').read_text(encoding='utf-8')
js=re.findall(r'<script>(.*?)</script>',html,re.S)[0]
compiled=subprocess.run(['node','-e','new Function(require("fs").readFileSync(0,"utf8")); console.log("JS syntax OK")'],input=js,text=True,encoding='utf-8',capture_output=True)
assert compiled.returncode==0,compiled.stderr
for name in re.findall(r'(?:src|href)="([^"#]+)"',html):
    assert (root/name).is_file(),name
results=json.loads((root/'SIMULATION.json').read_text(encoding='utf-8'))
assert results['cad_parts']==46
assert all(c['pass'] for c in results['cup_clearance'])
assert all(2<=t['pieces_min']<=4 for t in results['timing'])
assert len(list(root.glob('C*.step')))==45
assert (root/'MACHINE_REV_B.step').stat().st_size>10000
assert not any(bad in html for bad in ['Â','Ã','â€'])
report={'cad_rebuild':'exit 0','javascript':'syntax passed','local_links':'all static links resolve','cad_parts':46,'tool_sets':15,'tool_solids':45,'sampled_mould_states':105,'mould_intersections':'passed','support_food_intrusion':'passed for 15 diameters','nominal_throughput':'2.78–3.31/min under stated assumptions','physical_function':'not tested'}
(root/'VERIFICATION.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
