from pathlib import Path
import json, csv, statistics as st, html, base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=Path(__file__).parent
views=['Npool4','Npool8','Npool18','Nreal']; counts=[4,8,18,152]
raw={}
for kind in ['main','logo_walk_sonic','logo_walk_g113']:
 for v in views:
  for sh in ['', '+Sblk']:
   raw[kind,v+sh]=[json.loads((r/f'worker_a/sweep/{kind}/{v}{sh}_s{s}.json').read_text())['test']['M1'] for s in range(3)]
rob=[json.loads(l) for l in (r/'qc/robust.jsonl').read_text().splitlines()]
arms=sorted({x['arm'] for x in rob});print('sensor arms',arms)
# Changed-sensor curve: equal-weight mean of all eight non-nominal arms, per seed.
changed=[a for a in arms if a!='nominal']
def sensor(v,a):return [next(x['M1'] for x in rob if x['view']==v and x['seed']==s and x['arm']==a) for s in range(3)]
def avg(a,b):return [(x+y)/2 for x,y in zip(a,b)]
def cm(v):return [st.mean(sensor(v,a)[s] for a in changed) for s in range(3)]
def f(a):return f'{st.mean(a):.3f} ± {st.pstdev(a):.3f}'
def diff(a,b):return [x-y for x,y in zip(a,b)]
rows=[]
for v,n in zip(views,counts):
 for sh in ['', '+Sblk']:
  w=v+sh; seen=raw['main',w]; unseen=avg(raw['logo_walk_sonic',w],raw['logo_walk_g113',w]); ch=cm(w)
  verdict='Fragile' if st.mean(seen)-st.mean(ch)>.1 else ('Insufficient' if .881-st.mean(seen)>.05 else 'Adequate')
  rows.append([w,n,n+(4 if sh else 0),f(seen),f(raw['logo_walk_sonic',w]),f(raw['logo_walk_g113',w]),f(unseen),f(ch),verdict])
with (r/'REVIEW_TABLE.csv').open('w') as out:
 wr=csv.writer(out);wr.writerow(['source_layout','pressure_points','sensing_elements','seen_F1','unseen_SONIC_F1','unseen_G113_F1','two_gait_mean_F1','eight_changed_sensor_mean_F1','D26_label_reduced_scope']);wr.writerows(rows)
with (r/'SHEAR_BENEFIT.csv').open('w') as out:
 wr=csv.writer(out);wr.writerow(['source_layout','seen_paired_delta','unseen_SONIC_paired_delta','unseen_G113_paired_delta','changed_sensor_mean_paired_delta'])
 for v in views:wr.writerow([v]+[f(diff(raw[k,v+'+Sblk'],raw[k,v])) for k in ['main','logo_walk_sonic','logo_walk_g113']]+[f(diff(cm(v+'+Sblk'),cm(v)))])
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(10,4.8));xs=range(4)
for label,vals in [('Seen gaits',[raw['main',v] for v in views]),('Unseen gait (two-gait mean)',[avg(raw['logo_walk_sonic',v],raw['logo_walk_g113',v]) for v in views]),('Changed sensor (eight-arm mean)',[cm(v) for v in views])]:ax.errorbar(list(xs),[st.mean(a) for a in vals],yerr=[st.pstdev(a) for a in vals],marker='o',capsize=4,label=label)
ax.set(xticks=list(xs),xticklabels=counts,xlabel='Pressure points per foot (without shear)',ylabel='Terrain macro-F1',ylim=(0,1));ax.legend();fig.tight_layout();fig.savefig(r/'review_pressure.png',dpi=150);plt.close(fig)
fig,axs=plt.subplots(1,3,figsize=(13,4.5),sharey=True)
for ax,kind,title in zip(axs,['main','logo_walk_sonic','logo_walk_g113'],['Seen gaits','Unseen SONIC gait','Unseen G113 gait']):
 for sh,label in [('', 'Without shear'),('+Sblk','With four shear vectors')]:
  vals=[raw[kind,v+sh] for v in views];ax.errorbar(list(xs),[st.mean(a) for a in vals],yerr=[st.pstdev(a) for a in vals],marker='o',capsize=3,label=label)
 ax.set(title=title,xticks=list(xs),xticklabels=counts,xlabel='Pressure points per foot',ylim=(0,1))
axs[0].set_ylabel('Terrain macro-F1');axs[-1].legend(fontsize=9);fig.tight_layout();fig.savefig(r/'review_shear.png',dpi=150);plt.close(fig)
fig,ax=plt.subplots(figsize=(10,4.5))
for off,k,title in [(-.17,'logo_walk_sonic','Unseen SONIC'),(.17,'logo_walk_g113','Unseen G113')]:
 vals=[diff(raw[k,v+'+Sblk'],raw[k,v]) for v in views];ax.bar([x+off for x in xs],[st.mean(a) for a in vals],width=.32,yerr=[st.pstdev(a) for a in vals],capsize=4,label=title)
ax.set(xticks=list(xs),xticklabels=counts,xlabel='Pressure points per foot',ylabel='Terrain macro-F1 gained from shear',ylim=(0,.22));ax.legend();fig.tight_layout();fig.savefig(r/'review_gait.png',dpi=150);plt.close(fig)
# Real hardware values retained exactly from original table.
real=[['QCAT: unseen speed, normal force','83.4 ± 0.6%'],['QCAT: unseen speed, three-axis force','89.0 ± 0.4%'],['QCAT: unseen speed, motion sensor','78.1 ± 0.9%'],['QCAT: unseen speed, force + motion sensor','88.8 ± 0.5%'],['PUTany: normal force','65.8 ± 1.0%'],['PUTany: three-axis force','64.9 ± 2.7%'],['PUTany: force + torque','91.0 ± 0.5%']]
fig,ax=plt.subplots(figsize=(10,4.8));ax.axis('off');t=ax.table(cellText=real,colLabels=['Real quadruped hardware; no humanoid pressure map','Terrain accuracy (five seeds)'],loc='center',cellLoc='left',colWidths=[.68,.32]);t.auto_set_font_size(False);t.set_fontsize(10);t.scale(1,2);fig.tight_layout();fig.savefig(r/'review_real.png',dpi=150);plt.close(fig)
lines=['# V3 summary for outside review',
'Completion: the owner-reduced quick check finished; the original full experiment did not (DECISIONS.md D36, D40; STATUS.md v3).',
'Archive: adder manager checkout commit b8f0b07154ef5cbed566337eace56c5863ef0afb; REPORT_V3.md does not exist in any inspected checkout.',
'Question definitions below are DECISIONS.md D26, not the unrelated historical Q1–Q5 in QUESTIONS.md.',
'Notation: terrain macro-F1; ± population standard deviation over seeds; quick-check seeds 0–2 (D36); real-data accuracy uses five seeds (q5_table.md).',
'Sources: R = qc/robust_table.md (row, column); J = worker_a/sweep/{condition}/{layout}_s{0,1,2}.json, test.M1.',
'Derived values and exact layout rows: REVIEW_TABLE.csv and SHEAR_BENEFIT.csv; build_review.py documents averaging and pairing.',
'',
'Q1: No universal pressure count is established: without shear, seen-gait F1 rises from 0.782 ± 0.003 at four points to 0.856 ± 0.001 at full resolution (R Npool4/Nreal, in-distribution).',
'Unseen SONIC also improves: 0.222 ± 0.017 → 0.418 ± 0.016 (J logo_walk_sonic, Npool4/Nreal; recomputed values in REVIEW_TABLE.csv).',
'Changed sensor reverses that ranking: foot mask 0.727 ± 0.007 → 0.084 ± 0.018 (R Npool4/Nreal, g1); therefore the pressure-count conclusion does not hold across sensor models.',
'',
'Q2: Four block shear vectors help the tested layouts, but the minimum shear count is unknown because one/two-vector comparisons were cut (D36; R).',
'At four pooled points, seen-gait F1 is 0.782 ± 0.003 without vs 0.821 ± 0.006 with shear (R Npool4/Npool4+Sblk, in-distribution).',
'Four-point shear benefit holds on unseen SONIC (0.116 ± 0.034), G113 (0.142 ± 0.030), and the changed-sensor mean (0.049 ± 0.005); individual arm significance is not established (SHEAR_BENEFIT.csv Npool4; R).',
'',
'Q3: Greater shear benefit on SONIC is not supported by the tested held-out results; the complete original gait comparison remains untested (D26 Q3, D40).',
'Full-map held-out benefits: '+f(diff(raw['logo_walk_sonic','Nreal+Sblk'],raw['logo_walk_sonic','Nreal']))+' SONIC vs '+f(diff(raw['logo_walk_g113','Nreal+Sblk'],raw['logo_walk_g113','Nreal']))+' G113 (SHEAR_BENEFIT.csv Nreal; J logo_* Nreal[+Sblk]).',
'The second benefit fails the stated real-difference rule (D40); no gait-specific changed-sensor comparison or held-out G80 is available, so neither setting establishes the original hypothesis.',
'',
'Q4: No layout earns a robust recommendation under the original rule; four-point layouts are insufficient and finer layouts fragile under the explicitly stated reduced-scope eight-arm average (REVIEW_TABLE.csv, D26 Q4).',
'Four points + shear: seen '+f(raw['main','Npool4+Sblk'])+', two-gait mean '+f(avg(raw['logo_walk_sonic','Npool4+Sblk'],raw['logo_walk_g113','Npool4+Sblk']))+', changed sensor '+f(cm('Npool4+Sblk'))+' (REVIEW_TABLE.csv Npool4+Sblk).',
'Full map + shear: seen '+f(raw['main','Nreal+Sblk'])+', two-gait mean '+f(avg(raw['logo_walk_sonic','Nreal+Sblk'],raw['logo_walk_g113','Nreal+Sblk']))+', changed sensor '+f(cm('Nreal+Sblk'))+' (REVIEW_TABLE.csv Nreal+Sblk).',
'Unseen-gait and sensor objectives favour different layouts; course metrics and original full recommendation grid were not completed (D26, D36).',
'',
'Q5: The real-data shear analogue holds on QCAT but not PUTany; neither dataset validates a humanoid pressure layout (q5_table.md, real-data sections).',
'QCAT unseen speed: three-axis 89.0 ± 0.4% vs normal-only 83.4 ± 0.6%; PUTany: 64.9 ± 2.7% vs 65.8 ± 1.0% (q5_table.md force3/normal rows).',
'Changed hardware sensor model was not tested; unseen robot gait was not tested (unseen speed is the QCAT proxy); matching simulation comparisons remain pending (q5_table.md).',
'',
'V2 observation: confirmed for the tested pooled layouts on both unseen gaits, and for the full map on unseen SONIC; full-map unseen G113 is inconclusive (D40; SHEAR_BENEFIT.csv).',
'Four-point paired benefit: SONIC '+f(diff(raw['logo_walk_sonic','Npool4+Sblk'],raw['logo_walk_sonic','Npool4']))+', G113 '+f(diff(raw['logo_walk_g113','Npool4+Sblk'],raw['logo_walk_g113','Npool4']))+' (SHEAR_BENEFIT.csv Npool4).',
'The original H2 confirmation is NOT established: v2-block replication and the complete held-out-gait mean were cut; D40 calls the pooled result confirmed, whereas D26 explicitly excludes pooled four-point results from the strict H2 verdict.',
'',
'Missing/wrong: no REPORT_V3.md or existing v3 HTML page; old/pending sections remain in STATUS.md and q5_table.md, alongside completed quick-check results.',
'STATUS.md final table rounds SONIC four-point no-shear to 0.22 ± 0.02; use recomputed REVIEW_TABLE.csv/J for exact values.',
'STATUS.md draft robustness mixes nominal sensor results with in-distribution results: four-point no-shear 0.80 vs 0.782 ± 0.003; R separates nominal 0.799 ± 0.002 from in-distribution 0.782 ± 0.003.',
'No report/table reconciliation is possible for REPORT_V3.md because it is missing; original tables and STATUS.md are retained.',
'Sensor checks: maximum centre-of-pressure difference 1.57 mm failed the 1 mm limit; small footprints overcount edge load and foot masks omit box-foot edge loads (DECISIONS.md D33; reallike_checks.json).',
'Viper was used for contact-policy training; both attempts failed the contact-improvement rule (D33, D36; contact_evaluation/ and NOTES_C.md).',
'Weights remain on the servers; WEIGHTS.txt and WEIGHTS_VIPER.txt list their paths and sizes; this collection contains results and a weight inventory, not checkpoint binaries.'
]
# Replace illustrative Q1 held-out values with exact recomputation.
lines[9]='Unseen SONIC also improves: '+f(raw['logo_walk_sonic','Npool4'])+' → '+f(raw['logo_walk_sonic','Nreal'])+' (J logo_walk_sonic, Npool4/Nreal; REVIEW_TABLE.csv).'
(r/'V3_SUMMARY.md').write_text('\n'.join(lines)+'\n');assert len(lines)<=60

def image(name,alt):return '<img alt="'+html.escape(alt)+'" src="data:image/png;base64,'+base64.b64encode((r/name).read_bytes()).decode()+'">'
def table(headers,rows):return '<table><thead><tr>'+''.join('<th>'+html.escape(str(x))+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(str(x))+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table>'
fig,ax=plt.subplots(figsize=(10,4.5))
for label,vals in [('Seen gaits',[raw['main',v+'+Sblk'] for v in views]),('Unseen gait (two-gait mean)',[avg(raw['logo_walk_sonic',v+'+Sblk'],raw['logo_walk_g113',v+'+Sblk']) for v in views]),('Changed sensor (eight-arm mean)',[cm(v+'+Sblk') for v in views])]:
 ax.errorbar(list(xs),[st.mean(a) for a in vals],yerr=[st.pstdev(a) for a in vals],marker='o',capsize=4,label=label)
ax.set(xticks=list(xs),xticklabels=counts,xlabel='Pressure points per foot (with four shear vectors)',ylabel='Terrain macro-F1',ylim=(0,1));ax.legend();fig.tight_layout();fig.savefig(r/'review_tradeoff.png',dpi=150);plt.close(fig)
blocks=[('1. How many pressure points?','More pressure points help on seen and unseen gaits, but the advantage reverses when the sole model changes.','review_pressure.png','Three curves: seen gaits, two tested unseen gaits, and changed sensor models.'),('2. Does shear help?','Four shear vectors improve terrain recognition in the tested comparisons; the minimum number of vectors was not tested.','review_shear.png','With and without shear; bars show seed standard deviation.'),('3. Does shear help more on SONIC?','The tested unseen-gait results do not establish a larger shear benefit for SONIC.','review_gait.png','Paired shear benefit by held-out gait; G80 is missing.'),('4. Which layout should we choose?','No tested layout passes the original robustness rule under the eight-model sensor average used here.','review_tradeoff.png','Layout trade-off with four shear vectors; recommendations depend on the sensor model.'),('5. Does it hold on real robots?','Three-axis force helps on QCAT but not PUTany; these quadruped recordings do not validate a humanoid pressure map.','review_real.png','QCAT and PUTany real hardware; mean and population standard deviation over five seeds.')]
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>V3 terrain sensing review</title><style>body{font:18px/1.55 system-ui,sans-serif;max-width:1150px;margin:40px auto;padding:0 24px;color:#162536;background:#f8fafc}h1{font-size:38px}h2{margin-top:40px}section{background:white;padding:22px;margin:22px 0;border:1px solid #dce2e9;border-radius:12px}img,video{width:100%;height:auto}figure{margin:20px 0}figcaption,.note{font-size:14px;color:#465566}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:9px;border:1px solid #ccd4dd;text-align:left}th{background:#eef3f8}.scroll{overflow:auto}.ok{color:#166534}a{color:#125aa3}.status{font-size:14px}</style><h1>V3: terrain sensing results</h1><p>The reduced quick check finished. The original full sweep did not finish.</p><p>All simulation scores below are terrain macro-F1, not the fraction of correct predictions. Error bars are population standard deviations over three seeds. Real-data scores are accuracy over five seeds.</p><p><a href="V3_SUMMARY.md">Reviewer summary</a> · <a href="STATUS.md">Original run status</a> · <a href="DECISIONS.md">Recorded decisions</a> · <a href="WEIGHTS.txt">Adder weights</a> · <a href="WEIGHTS_VIPER.txt">Viper weights</a></p><p class="note">The original final report was not written. The strict original claim about shear on unseen gaits remains incomplete because the replication using the old pressure blocks and the third held-out gait were cut.</p>'''
for title,sentence,im,cap in blocks:
 page+='<section><h2>'+title+'</h2><p>'+sentence+'</p><figure>'+image(im,cap)+'<figcaption>'+cap+'</figcaption></figure></section>'
page+='<section><h2>Layout recommendation table</h2><p>There is no robust winner under the recorded rule. More pressure points favour the tested unseen gaits; four pooled pressure points retain more information when the sole model changes.</p><p class="note">Unseen gait means an equal-weight average of SONIC and G113, paired by seed. Changed sensor means an equal-weight average of the eight non-nominal sensor variants: shifted parameters, pads, foot mask, no saturation, three footprint sizes, and a footprint with a foot mask. These reduced-scope averages are not the original complete experiment. “Fragile” means a drop larger than 0.10 from seen-gait F1.</p><div class="scroll">'
page+=table(['Pressure points','Shear vectors','Sensing elements','Seen gait F1','Unseen gait F1','Changed sensor F1','Rule verdict'],[[row[1],4 if '+Sblk' in row[0] else 0,row[2],row[3],row[6],row[7],row[8]] for row in rows])+'</div><p class="note">Source: <a href="REVIEW_TABLE.csv">recomputed table</a>, <a href="SHEAR_BENEFIT.csv">paired shear benefits</a>, <a href="qc/robust_table.md">original sensor table</a>, <a href="q5_table.md">original real-data table</a>. Original per-seed JSONs are retained in worker_a/sweep.</p></section>'
page+='<section><h2>Videos</h2><p>These clips show the simulated gaits and the effect of changing the pressure-reading footprint.</p>'
labels={'closeup_sonic_hard_grip':'SONIC foot on firm ground with grip','closeup_sonic_hard_slip':'SONIC foot on slippery firm ground','reallike_vs_v2_edge':'Pressure readings while stepping on an edge','reallike_vs_v2_hard_grip':'Pressure readings on firm ground with grip','side_g113_sonic_hard_grip':'Two gaits side by side on firm ground with grip','side_g113_sonic_hard_slip':'Two gaits side by side on slippery firm ground'}
for i,p in enumerate(sorted((r/'videos').glob('*.mp4'))):page+=f'<figure><figcaption>{labels.get(p.stem,p.stem)}</figcaption><video controls muted playsinline preload="auto" data-label="{labels.get(p.stem,p.stem)}" src="videos/{p.name}"></video><div class="status" id="v{i}">Checking video…</div></figure>'
page+='''</section><section><h2>Limits and checks</h2><p>The simulated foot is a rigid box. Small sensing footprints overcount concentrated edge loads; the foot mask misses loads at box corners. One centre-of-pressure check failed. Both contact-policy training attempts failed their improvement rule.</p><p>Some original status paragraphs and real-data comparison rows remain stale or pending. The reviewer summary preserves these gaps and the difference between nominal-sensor and seen-gait scores.</p><p id="media-check">Checking media…</p></section><script>
const vs=[...document.querySelectorAll('video')];
async function verify(v,i){try{if(v.readyState<2)await new Promise((res,rej)=>{v.addEventListener('loadeddata',res,{once:true});v.addEventListener('error',rej,{once:true});setTimeout(()=>rej(Error('load timeout')),20000)});v.currentTime=Math.min(1,v.duration/2);await new Promise((res,rej)=>{if(!v.seeking)return res();v.addEventListener('seeked',res,{once:true});setTimeout(()=>rej(Error('seek timeout')),10000)});await v.play();await new Promise(res=>setTimeout(res,350));v.pause();document.getElementById('v'+i).textContent='Verified: decoded, sought and played ('+v.duration.toFixed(1)+' seconds).';document.getElementById('v'+i).classList.add('ok');return true}catch(e){document.getElementById('v'+i).textContent='Video check failed: '+e.message;return false}}
Promise.all(vs.map(verify)).then(results=>{let imgs=[...document.images];let ok=imgs.filter(i=>i.complete&&i.naturalWidth>0).length;document.getElementById('media-check').textContent='Media check: '+ok+'/'+imgs.length+' figures loaded; '+results.filter(Boolean).length+'/'+vs.length+' videos decoded, sought and played.';});
</script></html>'''
(r/'index.html').write_text(page)
print('Summary lines',len(lines));print((r/'REVIEW_TABLE.csv').read_text());print((r/'SHEAR_BENEFIT.csv').read_text())
