from pathlib import Path
import subprocess,json,hashlib
r=Path(__file__).parent
mappings=[('adder','m/results/v3',''),('adder','a/results/v3','worker_a'),('adder','b/results/v3','worker_b'),('adder','c/results/v3','worker_c'),('adder','render/v3','videos'),('adder','k1v3/eval','contact_evaluation'),('viper','qc_viper/results/v3','viper')]
results=[]
for host,remote,local in mappings:
 script="import pathlib,hashlib,json; p=pathlib.Path('/data/kkolesni/fla-terrain/"+remote+"'); print(json.dumps({str(f.relative_to(p)):hashlib.sha256(f.read_bytes()).hexdigest() for f in p.rglob('*') if f.is_file()}))"
 import shlex
 out=subprocess.check_output(['ssh','-S',str(Path.home()/f'.ssh/gpumon-kkolesni@{host}.cs.kent.edu:22'),f'kkolesni@{host}.cs.kent.edu','python3 -c '+shlex.quote(script)],text=True)
 files=json.loads(out);bad=[]
 for path,digest in files.items():
  p=r/local/path
  if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:bad.append(path)
 results.append({'host':host,'remote':remote,'local':local,'files':len(files),'mismatches':bad,'sha256':files})
print(json.dumps([{k:v for k,v in x.items() if k!='sha256'} for x in results],indent=2))
(r/'COPY_VERIFICATION.json').write_text(json.dumps(results,indent=2))
assert all(not x['mismatches'] for x in results)
