# Worker C notes (v3, Part H)

## C1: walkable course and baseline (CPU only)

`python -m k1v3.course_walkable` (40 seeds, measured from the geoms):

| quantity | n | min | max | limit |
|---|---|---|---|---|
| gap | 297 | 0.0200 | 0.0598 | < 0.070 m (foot width), drawn 0.02-0.06 |
| mu | 14674 | 0.2182 | 1.2985 | >= 0.2 |
| bump | 13796 | 0.0025 | 0.0100 | <= 0.01 m |
| slope | 110 | 5.0026 | 6.9083 | <= 7.0 deg |

v2 course, same 40 seeds: gap 0.030-0.322 m (the last gap before the far lead was the leftover space, 22 of 269 gaps > 8 cm), mu 0.085-1.30, bump 0.0025-0.0199 m, slope 5.0-9.8 deg.

`python -m k1v3.eval_walkable --procs 16` (results /data/kkolesni/fla-terrain/k1v3/eval/c1_walkable.{json,md}, log logs/wC_c1_eval.log):

walkable course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..19; commit 311601f clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 19/20 | 0 | 0 | 1 | 0.337 |
| G113_m2200 | 20/20 | 0 | 0 | 0 | 0.356 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 26 / 0 / 0.00 | 29 / 0 / 0.00 | 23 / 0 / 0.00 | 23 / 0 / 0.00 | 28 / 0 / 0.00 | 15 / 0 / 0.00 | 14 / 0 / 0.00 | 0 |
| G113_m2200 | 26 / 0 / 0.00 | 29 / 0 / 0.00 | 23 / 0 / 0.00 | 23 / 0 / 0.00 | 28 / 0 / 0.00 | 15 / 0 / 0.00 | 14 / 0 / 0.00 | 0 |

K1V2_r4_m1000 seed 4: did not fall, timed out at x 24.85 m (y -1.28 m), i.e. slow + drifting as in v2 (B13).
Plausibility: every v2 failure of G113 on seeds 0-19 except one (seed 8, slip mu 0.289, unchanged here) was on a hazard this course removes or softens (8 slip chunks at mu 0.09-0.12, 2 planks, a 1.75 cm bump, a 6.0 deg slope); run4 m1000's v2 failures were planks 3, bump 1.75 cm 1, soft 1 (soft is unchanged: stochastic).
Policy: b_runs/k1v2/policies/K1V2_r4_m1000.npz (already imported in v2, B13; not re-imported).

## C2: fresh seeds, contact quality, gait descriptors (CPU only)

Code: k1v3/contact_quality.py (definitions in its docstring), k1v3/eval_walkable.py --course {walkable,v2,flat} --monitor (hooks the source pre_step; scripts/walk_eval_course.run unchanged). Runs: /data/kkolesni/fla-terrain/k1v3/c2_run.sh, log logs/wC_c2.log, results k1v3/eval/c2_{flat,walkable_fresh,v2course}.{json,md}, all at commit 049e426, clean tree. Check: the v2-course rerun reproduces B13 for run4 m1000 (11/20 crossed; planks 3, rough 1, soft 1), so the monitor does not change the run.

Amended after a 2-episode smoke test, before the full runs (also in the docstring): impact also as the 10 ms moving-mean peak (rigid heel-corner touchdown = one 2 ms step of ~3 kN); slip integrated over steps with Fz > 20 N from 10 ms after touchdown; CoP travel as p90-p10 (max-min is the full 180 mm sole for every source). CoP travel is still uninformative on the box foot (CoP sits on the heel edge, then the toe edge); the back-third fraction carries that information.

### c2_walkable_fresh

walkable course, v2 foot, plain command 0.35 m/s, auto-T, seeds 1000..1039; commit 049e426 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 38/40 | 0 | 1 | 2 | 0.338 |
| G113_m2200 | 40/40 | 0 | 0 | 0 | 0.355 |
| G80_m4200 | 39/40 | 1 | 0 | 0 | 0.353 |
| SONIC | 19/40 | 22 | 17 | 0 | 0.422 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 53 / 0 / 0.00 | 52 / 0 / 0.00 | 61 / 0 / 0.00 | 28 / 0 / 0.00 | 27 / 0 / 0.00 | 1 |
| G113_m2200 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 53 / 0 / 0.00 | 52 / 0 / 0.00 | 61 / 0 / 0.00 | 28 / 0 / 0.00 | 27 / 0 / 0.00 | 0 |
| G80_m4200 | 49 / 0 / 0.00 | 49 / 0 / 0.00 | 52 / 0 / 0.00 | 50 / 0 / 0.00 | 59 / 0 / 0.00 | 28 / 0 / 0.00 | 27 / 1 / 0.04 | 0 |
| SONIC | 41 / 2 / 0.05 | 43 / 2 / 0.05 | 45 / 1 / 0.02 | 41 / 1 / 0.02 | 50 / 3 / 0.06 | 26 / 0 / 0.00 | 25 / 12 / 0.48 | 18 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 5952 | 24.25 / 30.99 | 5.15 / 6.47 | 19.9 / 32.1 | 0.00 / 0.00 | 0.071 |
| G113_m2200 | 5851 | 16.76 / 21.51 | 3.51 / 4.46 | 11.7 / 24.1 | 0.00 / 0.00 | 0.077 |
| G80_m4200 | 7021 | 26.01 / 32.45 | 5.69 / 7.65 | 7.1 / 19.1 | 0.00 / 0.00 | 0.068 |
| SONIC | 2895 | 4.36 / 11.52 | 1.24 / 3.09 | 14.2 / 37.4 | 0.00 / 0.00 | 0.067 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.06 | 0.552 | 0.56 | 20.5 | 158 | 0.41 |
| G113_m2200 | 2.02 | 0.601 | 0.60 | 16.1 | 149 | 0.30 |
| G80_m4200 | 2.47 | 0.503 | 0.48 | 11.9 | 120 | 0.25 |
| SONIC | 1.49 | 0.671 | 0.68 | 9.1 | 160 | 0.29 |

### c2_v2course

v2 course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..19; commit 049e426 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 11/20 | 5 | 0 | 4 | 0.330 |
| G113_m2200 | 7/20 | 13 | 0 | 0 | 0.350 |
| G80_m4200 | 14/20 | 6 | 0 | 0 | 0.353 |
| SONIC | 7/20 | 12 | 7 | 0 | 0.398 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 22 / 0 / 0.00 | 26 / 0 / 0.00 | 21 / 1 / 0.05 | 22 / 1 / 0.05 | 24 / 0 / 0.00 | 15 / 3 / 0.20 | 13 / 0 / 0.00 | 0 |
| G113_m2200 | 19 / 0 / 0.00 | 22 / 9 / 0.41 | 16 / 0 / 0.00 | 18 / 1 / 0.06 | 20 / 1 / 0.05 | 11 / 2 / 0.18 | 11 / 0 / 0.00 | 0 |
| G80_m4200 | 20 / 0 / 0.00 | 26 / 2 / 0.08 | 21 / 2 / 0.10 | 20 / 0 / 0.00 | 26 / 0 / 0.00 | 13 / 2 / 0.15 | 13 / 0 / 0.00 | 0 |
| SONIC | 22 / 0 / 0.00 | 26 / 3 / 0.12 | 21 / 1 / 0.05 | 20 / 0 / 0.00 | 23 / 0 / 0.00 | 15 / 5 / 0.33 | 12 / 4 / 0.33 | 6 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 3033 | 23.77 / 31.29 | 5.13 / 6.49 | 19.4 / 35.6 | 0.00 / 0.00 | 0.085 |
| G113_m2200 | 2237 | 17.25 / 23.39 | 3.64 / 4.99 | 11.7 / 28.2 | 0.00 / 0.00 | 0.093 |
| G80_m4200 | 3062 | 26.26 / 33.47 | 5.76 / 8.01 | 7.6 / 20.8 | 0.00 / 0.00 | 0.080 |
| SONIC | 1869 | 5.05 / 18.33 | 1.52 / 4.73 | 15.7 / 57.6 | 0.00 / 0.00 | 0.075 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.36 | 0.547 | 0.54 | 19.7 | 146 | 0.41 |
| G113_m2200 | 2.28 | 0.592 | 0.60 | 15.8 | 144 | 0.32 |
| G80_m4200 | 2.52 | 0.500 | 0.48 | 11.9 | 118 | 0.25 |
| SONIC | 1.76 | 0.691 | 0.62 | 8.1 | 133 | 0.30 |

### c2_flat

flat course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..15; commit 049e426 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 0/16 | 0 | 0 | 16 | 0.348 |
| G113_m2200 | 0/16 | 0 | 0 | 16 | 0.357 |
| G80_m4200 | 0/16 | 0 | 0 | 16 | 0.354 |
| SONIC | 0/16 | 0 | 0 | 16 | 0.470 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | flat | start/end |
|---|---|---|
| K1V2_r4_m1000 | 16 / 0 / 0.00 | 0 |
| G113_m2200 | 16 / 0 / 0.00 | 0 |
| G80_m4200 | 16 / 0 / 0.00 | 0 |
| SONIC | 16 / 0 / 0.00 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 579 | 25.73 / 30.80 | 5.40 / 6.27 | 18.6 / 22.0 | 0.00 / 0.00 | 0.000 |
| G113_m2200 | 576 | 16.81 / 20.17 | 3.47 / 4.03 | 11.0 / 12.1 | 0.00 / 0.00 | 0.000 |
| G80_m4200 | 643 | 27.18 / 30.36 | 5.77 / 6.35 | 6.2 / 7.2 | 0.00 / 0.00 | 0.000 |
| SONIC | 368 | 4.46 / 7.69 | 1.27 / 2.16 | 13.3 / 15.4 | 0.00 / 0.00 | 0.000 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 1.90 | 0.524 | 0.56 | 21.6 | 170 | 0.43 |
| G113_m2200 | 1.89 | 0.572 | 0.60 | 16.8 | 180 | 0.30 |
| G80_m4200 | 2.12 | 0.506 | 0.48 | 11.5 | 131 | 0.27 |
| SONIC | 1.28 | 0.611 | 0.68 | 9.7 | 180 | 0.28 |

Notes:
- SONIC on the walkable course: 12 of its 22 falls are on the end pad after crossing (it walks 0.42 m/s and keeps going after the last chunk until auto-T, off the 6 m pad); these runs count as crossed. In-course failures: edge-steps 12 of 25 (steps are unchanged in the walkable course: 3-6 cm platforms) and lateral drift beyond |y| = 4 m (no heading control for SONIC, as in v2).
- Slip in stance includes MuJoCo soft-contact creep (G80 6 mm per stance on flat mu 1.0); compare between sources, not as absolute sliding.
- Partial support: median and p90 are 0 for every source (fewer than 10 % of stances have any partial frame); mean listed.
Gait descriptors on flat, per-episode mean +- std over the 16 episodes:
| policy | steps/s | stance fraction | pitch at touchdown (deg) | back third | impact 10 ms (x BW, episode median) |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 1.90 +- 0.03 | 0.52 +- 0.00 | 21.7 +- 0.4 | 0.43 +- 0.02 | 5.40 +- 0.09 |
| G113_m2200 | 1.89 +- 0.00 | 0.57 +- 0.00 | 16.7 +- 0.3 | 0.30 +- 0.01 | 3.50 +- 0.10 |
| G80_m4200 | 2.12 +- 0.03 | 0.51 +- 0.00 | 14.2 +- 2.5 | 0.27 +- 0.01 | 5.77 +- 0.06 |
| SONIC | 1.28 +- 0.14 | 0.61 +- 0.05 | 9.6 +- 0.6 | 0.28 +- 0.03 | 1.30 +- 0.38 |
run4 m1000 vs G113: same cadence, shorter stance, steeper heel-first touchdown, more stance time on the heel third, ~1.5x the touchdown impact; all differences far above the episode spread. Whether that is "a different gait" enough for a fourth source is the manager's call (D28).

## C3: test set of the fourth gait (walk_k1v2 = K1V2_r4_m1000), dataset-v2 format
- Plan configs/k1v2_test_v3.yaml: groups walk, strip, hardmid of dataset_v2.yaml (same classes, variants, bands,
  random sole, 20 s, seed 3001), source walk_k1v2, splits [0, 0, 1] with n = one v2 source's test count; the episode
  ids and so the per-episode rng are exactly those the full v2 plan would give this source's test cells.
- Registration: k1v3/gen_k1v2.py adds gen_data.WALKERS['k1v2'] = 'K1V2_r4_m1000' in every worker and runs
  scripts/gen_dataset.py unchanged (no change to walking/ or scripts/). Plan + wrapper at 003a4a2.
- Smoke (4 episodes, data/v3_k1v2_smoke): validator 4/4; metadata keys, npz keys, shapes and dtypes identical to
  data/v2 episode_walk_hard_grip_walk_g113_test_0000.
- Full: /data/kkolesni/fla-terrain/data/v3_k1v2, 444 episodes (2.47 h), 16 workers, 4.8 min, 0 failed
  (log logs/wC_c3_gen.log); 597 MB; /data 86 GB free after.
- Checks: validator 444/444; counts per class equal to walk_g113's test counts in data/v2 (walk 48 per class,
  edge planks / steps 24 each, strip 24 per type, hard_mid 60); motion_source K1V2_r4_m1000 in all 444; falls 4
  (hard_slip 2, strip_slip_grip 1, edge-planks 1); split_keys shared with data/v2 train/val 0 of 444 (4607 keys);
  range_split {'test': 444}; band values: mu test_in 225, test_out 255, test_mid 60; stiffness test_in 41, test_out 31;
  none of them occurs in data/v2 train/val.

## C4: contact-quality training of run4 m1000 on viper (v3_run1)
- Tree: adder k1v2/ (code + resume_r4_m1000.pth, md5 2f16e495..., no logs) rsynced to viper:/data/kkolesni/fla-terrain/
  k1v3_train/. Asset: viper has no /data/kkolesni/K1; the same USD is at fla-terrain/b_ext/k1_assets_converted/
  (md5 of the whole folder identical to adder's); K1_V3.yaml points there.
- Code (repo): k1v3/isaac/patch_k1v3.py (three penalties + per-iteration term log; definitions and approximations in
  its docstring), k1v3/isaac/make_v3_yaml.py (K1_V3 = K1_V2b + the three scales + v3_* settings; everything else as
  run4: terrain generator and curriculum, command ranges, PPO), k1v3/sync_to_viper.sh W_IMPACT W_SLIP W_PARTIAL,
  k1v3/isaac/launch_viper.sh (nice 10, detached), k1v3/isaac/reap_when_done.sh.
- Approximations: impact = excess of the max substep |Fz| over 2 BW in the first 0.1 s of contact (contact sensor
  history 10 substeps = one policy step); slip = horizontal speed of the slowest sole corner within 1 cm of the ground
  while |Fz| > 20 N (rolling about an edge ~0); partial = fraction of the 4 sole corners whose ground height is
  > 2.5 cm below the highest ground under the 4 corners, while |Fz| > 20 N, from the training height map (4 cm cells,
  nearest cell): 4 corners instead of support.py's 24 points, gaps < ~4 cm missed, edges +-2 cm.
- Smoke 1 (64 envs, 20 it, scales -1): per-step scaled terms impact 0.0045, slip 0.0022, partial 0.00035 (20-it
  means; it 0: 0.0086 / 0.0029 / 0.00034) against sum|other terms| 0.1665. Smoke 2 (64 envs, 20 it, scales -3.5 / -7 /
  -45 = 7.5 % target): share of sum|terms| at it 0 0.140 / 0.094 / 0.072, 20-it mean ~0.07 each; per-step net
  reward fell from +0.03 to about -0.005. only_positive_rewards is false in run4's config, so a negative per-step
  total makes early termination attractive (the trap the k1.py comment describes); chosen: the LOW end, 5 % each:
  scales impact -2.2, slip -4.5, partial -28. GPU (64 envs): 3.5 GB per process (torch alloc 0.25 GB).
- Both smoke processes hung in Isaac shutdown after the last iteration (as NOTES_B B16), holding 3.5 GB each; killed
  (own PIDs). The run has a reaper (kills our PID 120 s after "epoch: 1000/1000").
- v3_run1 (viper, 4096 envs, 1000 it, from resume_r4_m1000.pth, checkpoints every 100 in
  k1v3_train/k1_gym/logs/<date>/nn/model_N.pth, log k1v3_train/logs/v3_run1.log, pid file v3_run1.pid):
  it 0 shares of sum|terms| impact 0.094, slip 0.063, partial 0.042; its 2-12 0.04-0.05 each; per-step net +0.012 to
  +0.023. GPU 8.2 GB (process), viper total 88.5 of 95.8 GB. ~2.7 s/it (sps 31-38k): ~22 it/min, ~45 min total.

## C5: evaluation of v3_run1 (contact-quality training)
- v3_run1 ended at epoch 1000 (00:22 UTC); the reaper stopped the hung process, viper GPU freed (only other users'
  processes left). Training log: episode length 1085 / 1125 / 831 / 1036 steps at it 100 / 300 / 600 / 1000 (run4
  end ~1190), terrain level mean 4.35-4.37 (run4 4.75): no collapse in Isaac.
- Imported model_300 / 600 / 1000 (1000 = last) as K1V3_r1_m{300,600,1000} (scripts/walk_k1v2_import.py, numpy vs
  torch <= 1.3e-6); registered for MuJoCo by k1v3/policies.py (walking.k1_velocity only accepts K1V2_* names).
- Tracking (python -m k1v3.tracking), cmd 0.2/0.35/0.5/0.8 -> vx: r4 m1000 0.198/0.355/0.498/0.724 (= B13);
  m300 0.149/0.330/0.455/0.655; m600 0.177/0.321/0.461/0.667; m1000 0.174/0.318/0.434/0.658 (no falls).
- Runs: /data/kkolesni/fla-terrain/k1v3/c5_run.sh, log logs/wC_c5.log, results k1v3/eval/c5_{flat,walkable_fresh,
  v2course}.{json,md}, commit 72f6fd3 clean. Full tables in those .md files.
- Verdict (D32 rule, walkable seeds 1000-1039 vs r4 m1000): impact = 10 ms peak median; slip = median; partial = mean.
| checkpoint | impact (x BW) | slip (mm) | partial mean | crossed /40 | verdict |
|---|---|---|---|---|---|
| r4 m1000 (ref) | 5.15 | 19.9 | 0.071 | 38 | - |
| v3 m300 | 5.28 (+2.5 %) | 21.7 (+9 %) | 0.080 (+13 %) | 0 | not better |
| v3 m600 | 5.46 (+6 %) | 15.8 (-21 %) | 0.076 (+7 %) | 8 | not better |
| v3 m1000 | 5.45 (+6 %) | 17.8 (-11 %) | 0.086 (+21 %) | 0 | not better |
- Why the crossings collapse: not falls but lateral drift and speed. Walkable: off course (|y| > 4 m) 1 / 24 / 31 runs
  (m300 / m600 / m1000), median off-course time 46 s; m300 is slow (0.299 m/s) and times out in 39 of 40. On flat,
  median |y| after 20 s: r4 m1000 0.11 m, v3 m1000 1.35 m. Plain command, no heading hold (rule of C1-C2).
- Gait shift: stance with CoP in the back third 0.43 -> 0.57 / 0.67 / 0.68 on flat, CoP travel 170 -> 92 mm:
  the policy stays on its heels; the 1-step and 10 ms impact did not drop.

## C6: drift diagnosis and the second (last) training attempt
Diagnosis (no training):
- Isaac Lab, flat plane, 64 envs, 20 s, command (0.35, 0, 0), gait 1.0 Hz, pushes/kicks off, other randomization as in
  training, deterministic (k1v3/isaac/drift_probe.py; logs viper k1v3_train/logs/drift_*.log):
  run4 m1000: 54/64 without fall, body vy +0.019 m/s (mean |vy| 0.031), yaw rate -0.0005 rad/s, lateral after 20 s
  mean +0.26 m, median |lat| 0.67 m. v3_run1 m1000: 53/64, vy +0.029 (|vy| 0.033), yaw -0.0074 rad/s, lateral mean
  +0.97 m, median |lat| 0.99 m. The drift is present in Isaac too and is systematic for v3 (one sign), larger in
  MuJoCo (C5: median |y| 1.35 m vs 0.11 m). (10-11 falls of 64 for both in Isaac on flat: domain randomization
  extremes; not investigated, same for both.)
- Training terms per step (k1v3/isaac/reward_terms_v3.py, tensorboard; run4 epochs 970-1000 vs v3_run1 last 30):
  tracking_lin_vel_y 0.0298 vs 0.0296, tracking_ang_vel 0.0074 vs 0.0073, heading_hold -0.0010 vs -0.00085,
  tracking_lin_vel_x 0.0326 vs 0.0311: unchanged. The three penalties fell per step during v3_run1 (impact -0.011 ->
  -0.004, slip -0.013 -> -0.007, partial -0.019 -> -0.012); partial was the largest (-12.5 per episode at the end).
- Reason the trainer does not see the drift: tracking_lin_vel_y = exp(-err^2 / 0.1); a 0.03 m/s bias gives 0.991,
  i.e. it is free; heading_hold catches yaw, nothing catches a sideways bias with a straight heading.
Fix (one change set, fixed before launch): task K1_V3b = K1_V3 with (1) the three penalties halved: impact -1.1,
slip -2.25, partial -14; (2) a new linear term lateral_vel_abs = |cmd_y - filtered body vy|, scale -4 (a 0.03 m/s bias
costs ~0.0024 per step, ~2.5 per episode, about heading_hold's size). Everything else as v3_run1: 4096 envs,
1000 iterations from resume_r4_m1000.pth, viper, nice 10, reaper. Run name v3_run2.
- v3_run2 launched 00:36 UTC on viper (pid 1212912, log k1v3_train/logs/v3_run2.log, reaper on), 4096 envs, 8.2 GB GPU,
  ~3.8 s/it (sps ~26k; viper busier than in C4) -> ETA ~01:40 UTC. It 0 shares of sum|terms|: impact 0.048, slip
  0.032, partial 0.021 (half of v3_run1's, as intended); per-step net -0.009 at it 0, +0.02 from it 2. The [v3terms]
  line does not list lateral_vel_abs (viper's k1.py keeps the C4 print list; the term itself is active, tensorboard
  episode/lateral_vel_abs).
- To do on completion: import model_500 and model_1000 as K1V3_r2_m{500,1000}; k1v3.tracking; c5_run.sh-equivalent
  evaluation with K1V2_r4_m1000 as reference; verdict by D32.
- v3_run2 ended at epoch 1000 (~01:40 UTC, reaper; viper GPU free of our processes). Imported model_500 / 1000 as
  K1V3_r2_m{500,1000} (numpy vs torch <= 2e-6). Tracking 0.2/0.35/0.5/0.8: m500 0.179/0.318/0.455/0.681,
  m1000 0.150/0.299/0.458/0.674 (no falls).
- Evaluation as C5 (k1v3/c6_run.sh, log logs/wC_c6.log, results k1v3/eval/c6_*.{json,md}, commit ee73f36 clean).
  Flat median |y| after 20 s: r4 m1000 0.11 m, v3_run1 m1000 1.35 m (C5), v3_run2 m500 0.58 m, m1000 2.73 m.
| checkpoint | impact (x BW) | slip (mm) | partial mean | crossed /40 | off course | verdict (D32) |
|---|---|---|---|---|---|---|
| r4 m1000 (ref) | 5.15 | 19.9 | 0.071 | 38 | 1 | - |
| v3_run2 m500 | 5.12 (-0.6 %) | 19.6 (-1.5 %) | 0.079 (+11 %) | 24 | 1 (15 timed out) | not better |
| v3_run2 m1000 | 5.00 (-2.9 %) | 15.9 (-20 %) | 0.066 (-7 %) | 0 | 36 | not better |
  v2 course crossed /20: r4 11, m500 10, m1000 0 (14 off course). The lateral term did not stop the drift (m1000
  drifts more than v3_run1). By D33 Part H closes: run4 m1000 stays the fourth gait; contact-quality reward shaping
  did not improve contact quality here.

## C7: owner's quick check, unseen-gait models (qc/)
- Timing (qc/time_epoch.py, Worker A's code at a/ 2405b0f imported unchanged; main, Npool4, seed 99, 2 epochs, alone
  except other GPU users: Folding@home 1.3 GB + one of our qc/robust_v3.py jobs 5.5 GB; GPU 96-100 % utilization):
  data load 15 s (cache), ViewInputs 31 s; 377,108 train windows -> 737 batches of 512; val 54,979 windows.
  Epoch 18.8 / 15.7 s: batch gather + augment 1.6 / 1.3 s (8 %), forward + backward + step 17.1 / 14.3 s (91 %),
  other 0.1 s; validation 0.8 / 0.6 s. Peak 10.8 GB allocated, 152,079 parameters.
  -> alone, 16 epochs ~ 4.5 min of training + ~1 min setup and prediction. The sweep's 901 s of training for
  main/Npool4_s0 (16 epochs, 56 s/epoch) is ~3.3x that: it ran beside 2 other sweep jobs on a compute-saturated GPU.
  Augmenting the full 152-point map is not the cost (8 %). Faster without changing the recipe: not by running more
  jobs per GPU (compute-bound); cudnn.benchmark / TF32 / torch.compile would be faster but change floating-point results
  slightly (not applied; Worker A's code).
- Driver qc/quick_v3.py (scheduler pid 891218, log logs/qc_logo.log, per-job logs logs/qc_jobs/): 48 jobs via
  a/scripts/run_v3.py --job (results a/results/v3/sweep/logo_*/, models models/v3/logo_*/). Viper: code clone at
  viper:qc_viper (2405b0f), data/v2 + identical v2pts4 cache index (md5); not used so far: viper GPU free 15.6 GB < 20 GB.
- First results: logo_walk_sonic/Npool4_s0 wall 421 s (4 at once), test M1 0.231 (val 0.823), 15 epochs, train 227 s;
  Npool4+Sblk_s0 wall 331 s, test M1 0.318 (val 0.848).
