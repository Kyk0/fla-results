from pathlib import Path
import subprocess,json,shlex,sys,datetime
r=Path(__file__).parent
hosts=['adder','viper']
def remote(host,code):
 return subprocess.check_output(['ssh','-S',str(Path.home()/f'.ssh/gpumon-kkolesni@{host}.cs.kent.edu:22'),f'kkolesni@{host}.cs.kent.edu','python3 -c '+shlex.quote(code)],text=True)
inventory='''import os,pwd,json,pathlib,subprocess
uid=pwd.getpwnam('kkolesni').pw_uid
allp=[]
for p in pathlib.Path('/proc').iterdir():
 if not p.name.isdigit():continue
 try:
  if p.stat().st_uid!=uid:continue
  cmd=(p/'cmdline').read_bytes().replace(b'\\0',b' ').decode(errors='replace').strip()
  stat=(p/'stat').read_text().split(') ',1)[1].split()
  allp.append(dict(pid=int(p.name),ppid=int(stat[1]),start=stat[19],cmd=cmd))
 except (OSError,IndexError):pass
# Exclude inspection process and its ancestors even when its command contains search strings.
excluded=set(); pid=os.getpid()
while pid and pid not in excluded:
 excluded.add(pid); q=next((p for p in allp if p['pid']==pid),None);pid=q['ppid'] if q else 0
markers=['manager_loop.sh','watchdog.sh','run_agent.sh','/claude','claude --','run_v3.py','train_v3','v3_run','qc_unseen','tmux']
selected={p['pid'] for p in allp if p['pid'] not in excluded and any(m in p['cmd'] for m in markers)}
while True:
 more={p['pid'] for p in allp if p['ppid'] in selected and p['pid'] not in excluded}
 if more<=selected:break
 selected|=more
try:
 t=subprocess.run(['tmux','list-sessions'],capture_output=True,text=True);tmux=t.stdout+t.stderr
except FileNotFoundError:tmux='tmux not installed/on PATH; no tmux process found unless listed below'
print(json.dumps(dict(all_processes=allp,selected=[p for p in allp if p['pid'] in selected],tmux=tmux)))
'''
if sys.argv[1]=='plan':
 data={h:json.loads(remote(h,inventory)) for h in hosts};(r/'STOP_PLAN.json').write_text(json.dumps(data,indent=2))
 lines=['# Agent shutdown record','', 'Plan recorded before creating stop files: '+datetime.datetime.now(datetime.timezone.utc).isoformat(), 'Scope: kkolesni agent processes only; preserve files and other users’ processes.', 'Mac verification complete: COPY_VERIFICATION.json has zero mismatches; Chrome opened index.html from disk, loaded all five figures and decoded, sought and played all six videos.','']
 for h,d in data.items():
  lines+=['## '+h,'','Will stop:','```']+[f"{p['pid']} (parent {p['ppid']}, start ticks {p['start']}): {p['cmd']}" for p in d['selected']]+['```' if d['selected'] else 'No running agents found.\n```','Tmux: '+d['tmux'].strip(),'']
 lines+=['Will create /data/kkolesni/fla-terrain/agents/STOP on both hosts, and STOP_DEPUTY on viper.', 'Manager/watchdog/Claude/worker/tmux processes absent from the inventory need no termination.', 'System user services and SSH monitoring connections are not experiment agents and will remain.']
 (r/'STOPPED.md').write_text('\n'.join(lines)+'\n');print((r/'STOPPED.md').read_text())
elif sys.argv[1]=='stop':
 data=json.loads((r/'STOP_PLAN.json').read_text());out={}
 for h,d in data.items():
  code='''import os,pwd,pathlib,json,signal,time
assert os.getuid()==pwd.getpwnam('kkolesni').pw_uid
root=pathlib.Path('/data/kkolesni/fla-terrain/agents');(root/'STOP').touch()
'''
  if h=='viper':code+="(root/'STOP_DEPUTY').touch()\n"
  code+='targets='+repr(d['selected'])+'''
log=[]
for sig in [signal.SIGTERM,signal.SIGKILL]:
 for p in targets:
  q=pathlib.Path('/proc')/str(p['pid'])
  try:
   if q.stat().st_uid!=os.getuid():raise RuntimeError('owner changed')
   start=(q/'stat').read_text().split(') ',1)[1].split()[19]
   if start!=p['start']:raise RuntimeError('PID reused')
   os.kill(p['pid'],sig);log.append([p['pid'],sig.name])
  except FileNotFoundError:pass
 time.sleep(2)
print(json.dumps(log))
'''
  out[h]=json.loads(remote(h,code))
 (r/'STOP_ACTIONS.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
 with (r/'STOPPED.md').open('a') as f:f.write('\n## Actions executed\n'+json.dumps(out,indent=2)+'\nSTOP sentinels created on both hosts; no files deleted.\n')
elif sys.argv[1]=='verify':
 data={h:json.loads(remote(h,inventory)) for h in hosts};(r/'POST_STOP_PROCESSES.json').write_text(json.dumps(data,indent=2))
 for h,d in data.items():print(h,'Remaining agents:',d['selected'])
 assert all(not d['selected'] for d in data.values())
