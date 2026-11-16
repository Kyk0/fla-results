# STATUS

## v3 status

Last tick: 2026-11-15 18:06 UTC (manager, on adder). Run v3 started 2026-11-14 22:25 UTC. Older sections below are v1/v2 history.

### Answer to Kyrylo's message of 00:00 UTC (change of scope)

Sorry for the delay: my inbox check missed your message for about 2.5 hours (it only looked for headers written by the relay; fixed, D36).

- **Done:** the big sweep is stopped (02:27 UTC). The quick check runs exactly as you wrote: 8 layouts (pooled pressure 4, 8, 18, full x shear 0 or 4 vectors), sole-only, 3 seeds.
- **In-distribution (24 models):** already finished by the sweep before it was stopped. Table (a) below.
- **Unseen gait (48 models, leave out SONIC, leave out G113):** training now (Worker C), up to 4 at once on adder, plus viper if it has room. ETA about 2-3 hours.
- **Robustness (no new training):** Worker B is scoring the 24 models on the existing sensitivity sets now; the real-like reading sets are generated and valid; Worker B is scoring them now (B10).
- **Why a model takes about 10 minutes, not 5:** being measured (Worker C). What is known: the network is tiny (152k parameters), about 19 epochs to early stop at about 32 s each; every batch gathers and randomly perturbs the full 152-point map on the GPU even for 4-pad inputs; and the GPU is shared with another user's job running at 90-100 %. Numbers follow.
- Waiting for the rest of your table spec (b), (c). The final three tables go here when the quick check is complete.

**(b, draft) Robustness: terrain F1 of the 24 in-distribution models (3 seeds each) scored, without retraining, on changed sensors. Sole only, K1 humanoid simulation.** Columns: the sensor it was trained on, shifted parameters, pad sole, foot-shaped mask, no saturation, and the "real-like" reading (each sensing point sees only 30 / 60 / 100 % of its cell), the last also with the foot-shaped mask.

| Pressure points / shear | Trained-on sensor | Shifted | Pads | Foot mask | No sat. | Real-like 30 % | 60 % | 100 % | 60 % + foot mask |
|---|---|---|---|---|---|---|---|---|---|
| 4, no shear | 0.80 | 0.78 | 0.56 | 0.73 | 0.70 | 0.57 | 0.72 | 0.79 | 0.70 |
| 4 + 4 shear | 0.83 | 0.82 | 0.63 | 0.75 | 0.76 | 0.63 | 0.79 | 0.82 | 0.73 |
| 8, no shear | 0.84 | 0.82 | 0.34 | 0.40 | 0.75 | 0.58 | 0.75 | 0.83 | 0.47 |
| 8 + 4 shear | 0.86 | 0.85 | 0.48 | 0.47 | 0.82 | 0.64 | 0.82 | 0.86 | 0.55 |
| 18, no shear | 0.85 | 0.84 | 0.30 | 0.32 | 0.81 | 0.52 | 0.69 | 0.81 | 0.30 |
| 18 + 4 shear | 0.88 | 0.87 | 0.42 | 0.35 | 0.85 | 0.59 | 0.78 | 0.86 | 0.34 |
| full (152), no shear | 0.87 | 0.84 | 0.19 | 0.08 | 0.75 | 0.50 | 0.62 | 0.75 | 0.09 |
| full (152) + 4 shear | 0.89 | 0.87 | 0.23 | 0.10 | 0.82 | 0.58 | 0.74 | 0.81 | 0.10 |

In plain words: parameter shifts hurt nobody. Anything that changes how the sole forms the picture (pads, foot-shaped mask, small sensing footprints) hurts the fine layouts most: the full map falls to 0.08-0.23 on pads and the foot-shaped mask, 4 pooled points keep 0.56-0.75. Block shear helps on nearly every variant (not on the foot-shaped mask). Caveat from A4: in the real-like reading small footprints also overcount edge load (x1.3-2.1 at 30 %).

**(c) Unseen gait: terrain F1 when the model never saw that gait. All 48 models done, 3 seeds each, mean ± std over seeds, sole only.** Left: gaits seen in training (from table a).

| Pressure points / shear | Seen gaits | Leave out SONIC | Leave out G113 |
|---|---|---|---|
| 4, no shear | 0.78 | 0.22 ± 0.02 | 0.46 ± 0.01 |
| 4 + shear | 0.82 | 0.34 ± 0.02 | 0.60 ± 0.02 |
| 8, no shear | 0.82 | 0.30 ± 0.02 | 0.56 ± 0.02 |
| 8 + shear | 0.85 | 0.41 ± 0.01 | 0.72 ± 0.01 |
| 18, no shear | 0.84 | 0.32 ± 0.02 | 0.57 ± 0.01 |
| 18 + shear | 0.87 | 0.40 ± 0.01 | 0.71 ± 0.01 |
| full, no shear | 0.86 | 0.42 ± 0.02 | 0.65 ± 0.03 |
| full + shear | 0.88 | 0.53 ± 0.02 | 0.72 ± 0.05 |

**Shear benefit on an unseen gait** (terrain F1 with shear minus without, paired by seed; real difference by the D14 rule = more than twice the seed spread and at least 2 points):

| Pressure points | Leave out SONIC | Leave out G113 |
|---|---|---|
| 4 | +0.12 ± 0.03 (real) | +0.14 ± 0.03 (real) |
| 8 | +0.11 ± 0.03 (real) | +0.16 ± 0.03 (real) |
| 18 | +0.09 ± 0.02 (real) | +0.14 ± 0.01 (real) |
| full | +0.11 ± 0.02 (real) | +0.07 ± 0.05 (not a real difference) |

In plain words: an unseen gait costs 30-60 points of accuracy; SONIC is the hard one. 4 shear vectors help the unseen gait by 9-16 points at every resolution (except G113 with the full map), against 2.5-4 points on seen gaits. Reading both: more pressure points help (4 to full: +20 points leave-out-SONIC), shear helps about as much as going from 4 to 18 points, and the best unseen-gait result (full map + shear) is still only 0.53 on SONIC. Sanity check: the full-map rows leave-out-SONIC (0.418 / 0.526) equal v2's held-out SONIC values (0.418 / 0.526).

**Quick check status:** (a), (b), (c) are complete on the numbers above. Still open: your table spec (b), (c) was cut off after "on a known"; tell me if you want a different cut. Nothing is running now; the agents are idle until you reply.

**Why a model takes about 10 minutes, not 5:** being measured (Worker C). What is known: the network is tiny (152k parameters), about 19 epochs to early stop at about 32 s each; every batch gathers and randomly perturbs the full 152-point map on the GPU even for 4-pad inputs; and the GPU is shared with another user's job running at 90-100 %. Numbers follow.
- Waiting for the rest of your table spec (b), (c). The final three tables go here when the quick check is complete.

**(b, draft) Robustness: terrain F1 of the 24 in-distribution models (3 seeds each) scored, without retraining, on changed sensors. Sole only, K1 humanoid simulation.** Columns: the sensor it was trained on, shifted parameters, pad sole, foot-shaped mask, no saturation, and the "real-like" reading (each sensing point sees only 30 / 60 / 100 % of its cell), the last also with the foot-shaped mask.

| Pressure points / shear | Trained-on sensor | Shifted | Pads | Foot mask | No sat. | Real-like 30 % | 60 % | 100 % | 60 % + foot mask |
|---|---|---|---|---|---|---|---|---|---|
| 4, no shear | 0.80 | 0.78 | 0.56 | 0.73 | 0.70 | 0.57 | 0.72 | 0.79 | 0.70 |
| 4 + 4 shear | 0.83 | 0.82 | 0.63 | 0.75 | 0.76 | 0.63 | 0.79 | 0.82 | 0.73 |
| 8, no shear | 0.84 | 0.82 | 0.34 | 0.40 | 0.75 | 0.58 | 0.75 | 0.83 | 0.47 |
| 8 + 4 shear | 0.86 | 0.85 | 0.48 | 0.47 | 0.82 | 0.64 | 0.82 | 0.86 | 0.55 |
| 18, no shear | 0.85 | 0.84 | 0.30 | 0.32 | 0.81 | 0.52 | 0.69 | 0.81 | 0.30 |
| 18 + 4 shear | 0.88 | 0.87 | 0.42 | 0.35 | 0.85 | 0.59 | 0.78 | 0.86 | 0.34 |
| full (152), no shear | 0.87 | 0.84 | 0.19 | 0.08 | 0.75 | 0.50 | 0.62 | 0.75 | 0.09 |
| full (152) + 4 shear | 0.89 | 0.87 | 0.23 | 0.10 | 0.82 | 0.58 | 0.74 | 0.81 | 0.10 |

In plain words: parameter shifts hurt nobody. Anything that changes how the sole forms the picture (pads, foot-shaped mask, small sensing footprints) hurts the fine layouts most: the full map falls to 0.08-0.23 on pads and the foot-shaped mask, 4 pooled points keep 0.56-0.75. Block shear helps on nearly every variant (not on the foot-shaped mask). Caveat from A4: in the real-like reading small footprints also overcount edge load (x1.3-2.1 at 30 %).

**(c, interim, 45 of 48 models) Unseen gait: terrain F1 when the model never saw that gait** (mean of seeds finished so far; same layouts, sole only):

| Pressure points / shear | Leave out SONIC | Leave out G113 |
|---|---|---|
| 4, no shear | 0.22 | 0.46 |
| 4 + shear | 0.34 | 0.60 |
| 8, no shear | 0.30 | 0.56 |
| 8 + shear | 0.41 | 0.72 |
| 18, no shear | 0.32 | 0.57 |
| 18 + shear | 0.40 | 0.71 |
| full, no shear | 0.42 (2 seeds) | 0.65 |
| full + shear | 0.52 (2 seeds) | 0.72 |

In plain words (interim): an unseen gait costs 30-60 points of accuracy, SONIC being much harder to predict than G113. Shear adds 8-15 points on an unseen gait, far more than the 2.5-4 points it adds on seen gaits, in both directions. More points still help.

**Why a model takes about 10 minutes, not 5:** being measured (Worker C). What is known: the network is tiny (152k parameters), about 19 epochs to early stop at about 32 s each; every batch gathers and randomly perturbs the full 152-point map on the GPU even for 4-pad inputs; and the GPU is shared with another user's job running at 90-100 %. Numbers follow.
- Waiting for the rest of your table spec (b), (c). The final three tables go here when the quick check is complete.

**Robustness, interim (b) draft: terrain F1 of the 24 in-distribution models (3 seeds) on the existing sensor variants, sole only.** Real-like reading columns follow when the test sets are ready.

| Pressure points / shear | Trained-on sensor | Shifted parameters | Pad sole | Foot-shaped mask | No saturation |
|---|---|---|---|---|---|
| 4, no shear | 0.782 | 0.782 | 0.560 | 0.727 | 0.696 |
| 4 + shear | 0.821 | 0.822 | 0.630 | 0.745 | 0.764 |
| 8, no shear | 0.817 | 0.817 | 0.338 | 0.399 | 0.750 |
| 8 + shear | 0.851 | 0.855 | 0.484 | 0.466 | 0.825 |
| 18, no shear | 0.839 | 0.838 | 0.303 | 0.321 | 0.813 |
| 18 + shear | 0.866 | 0.870 | 0.417 | 0.347 | 0.854 |
| full, no shear | 0.856 | 0.843 | 0.189 | 0.084 | 0.753 |
| full + shear | 0.881 | 0.870 | 0.231 | 0.098 | 0.815 |

In plain words: all layouts survive changed sensor parameters; the finer the layout, the worse it fails when the sole itself works differently (pads, foot-shaped mask). That is the same flip as in v2. Shear helps on every variant.

**Why a model takes about 10 minutes:** alone it takes about 5 (16-19 s per epoch, 737 batches, 91 % forward/backward). It took 15 in the sweep because three jobs shared the already saturated GPU, so more parallel jobs add little. Nothing was changed that would alter results.

**Model change (your 02:40 message):** all agents now run on Sonnet 5.5; tickets are small and I re-run every check.

**(a) Interim: terrain accuracy (macro-F1, six classes) by number of pressure points per foot, sole only, test split, mean ± std over 3 seeds** (from `a/results/v3/sweep/main/*.json`). Support-state F1 = airborne / partial / full per foot.

| Pressure points per foot | Terrain F1, no shear | Terrain F1, + 4 shear vectors | Support F1, no shear | Support F1, + 4 shear vectors |
|---|---|---|---|---|
| 4 | 0.782 ± 0.003 | 0.821 ± 0.006 | 0.792 ± 0.006 | 0.794 ± 0.002 |
| 8 | 0.817 ± 0.001 | 0.851 ± 0.003 | 0.879 ± 0.003 | 0.881 ± 0.003 |
| 18 | 0.839 ± 0.003 | 0.866 ± 0.001 | 0.896 ± 0.001 | 0.900 ± 0.005 |
| 152 (full map) | 0.856 ± 0.001 | 0.881 ± 0.002 | 0.923 ± 0.006 | 0.934 ± 0.003 |

In plain words, in the simulation and on gaits the model has seen: more points help steadily (4 to full: +7 points terrain F1, +13 support F1), and 4 shear vectors add 2.5-4 points of terrain F1 at every resolution but almost nothing to support state. The full-map rows reproduce v2 (0.856 and 0.881). Unseen-gait and robustness columns are still to come, and those are the ones that decide the recommendation.

**Part H closed:** two attempts to train the walking policy for gentler contact did not improve contact and made it drift sideways; the best v2 policy already crosses 38 of 40 walkable courses (D36).

### Workers
| Worker | Ticket | State | Since (UTC) |
|---|---|---|---|
| A (`a/`, worker-a) | A5 done (real-like test sets generated, valid, cached); idle | idle | 03:48 |
| B (`b/`, worker-b) | B10 done; idle | idle | 04:05 |
| C (`c/`, worker-c) | C7 done (48 unseen-gait models, 0 failed); idle | idle | 04:15 |

### Detached jobs
| Job | Where, PID | Log | ETA |
|---|---|---|---|
| v3 sweep | stopped 02:27 UTC by Kyrylo's scope change (D36); 45 models finished | `logs/v3_sweep.log` | - |

### adder (and viper)
adder: load about 140 on 96 cores (mostly other users). GPU 100 %, 43 GB used (3 of our sweep models + the other user). `/data`: 89 GB free after deleting 3.6 GB of stale caches (rule: >= 50 GB).
viper: GPU has 80 GB held by another user's vLLM jobs and 0 % compute in use; Part H training goes there (< 12 GB). `/data` 163 GB free.

### Done
- A5 accepted (D38): real-like test sets (footprint 30/60/100 %, foot-shaped mask), 288 episodes each, identical to the nominal simulations apart from the sensor reading. Early look with the v2 models: the real-like reading costs the full-map model about 17 points even at full footprint; the 4-block model is unaffected.
- B6 accepted (D35): PUTany (ANYmal, one foot F/T): force + torque 91.0 % (published 91.7 %), 3-axis force 64.9 %, normal only 65.8 %. Q5 table/figure script ready; sim rows fill in as the sweep runs.
- B5 accepted (D34): clips of the real-like reading next to the v2 reading for the same step (`render/v3/reallike_vs_v2_{edge,hard_grip}.mp4`).
- A4 accepted (D33): real-like reading (each sensing point reads only the load under its footprint). Finding: small footprints overcount the foot force while walking (x1.3-2.1 at 30 %) because the rigid box foot concentrates load at its edge; the foot-shaped mask misses a median 44-82 % of the force while walking. One check (centre of pressure vs v2 within 1 mm) failed at 1.57 mm and is reported as failed.
- B4 accepted (D33): SONIC sole close-ups and G113-vs-SONIC side-by-sides in `render/v3/` (EGL on adder works). SONIC lands flatter (9-10 degrees vs 16-17).
- C5 accepted (D33): the first contact-quality training failed its pre-set rule: contact did not improve and the policy drifts sideways (0-8 of 40 walkable courses crossed). One diagnosed retry (C6); if it fails, Part H closes with run4 m1000 as the walking result and fourth gait.
- B3 accepted (D32), real robot data (QCAT quadruped, one 3-axis force per foot): our model matches the published accuracy (force + IMU 98.2 % vs 97.6 %). On an unseen walking speed, 3-axis force 89.0 %, normal force only 83.4 %, IMU only 78.1 %. 3-axis beats normal-only on every split. Manager recomputed the table and re-ran the shuffled-label control (16.2 %).
- A3 accepted (D31): sweep runner launched; first model reproduces A2 exactly. Tier 5 reordered so Q5's matching rows and the shear-1 / shear-only models come first and D26's cut-first items last.
- C4 accepted: penalties for touchdown impact, slip in contact and partial support added to run4's task (blind policy), each about 3-5 % of the reward; training runs on viper. Manager checked the process and log.
- A2 accepted (D30): new layout inputs in the loader; v2's full-map + 4 shear-block model reproduces exactly (seed 0 test terrain F1 0.8827 = v2's 0.883); 91 tests pass; about 10 GPU-minutes per model.
- C3 accepted (D30): 444 test episodes of the fourth gait (run4 m1000), all valid, no overlap with training data.
- D30: the sweep (about 700 models, 3.5-4 days at 2 in parallel) is ordered so the pre-registered headline comparisons finish first: tier 1 = sole-only pooled layouts and v2 blocks, with and without shear, in-distribution and unseen gait (240 models).
- C2 accepted (D29): on 40 fresh walkable courses the best v2 policy (run4 m1000) crosses 38, G113 40, G80 39, SONIC 19 (fails on 3-6 cm steps). run4 m1000 is a distinct, more heel-first gait (touchdown pitch 21.7 vs 16.7 degrees for G113), so it becomes an extra unseen-gait test set. Manager re-ran the flat slice and matched the numbers.
- B2 accepted (D28): QCAT step dataset (2880 steps), normal axis per foot, offset rule, splits; manager reproduced the sanity baseline exactly (logistic regression, trial-level 10-fold: normal force 75.9 %, 3-axis force 92.5 %, IMU 82.6 %, force + IMU 95.1 %). Caveat: the force sensors read less load on soft ground (four-foot sum 68 N on concrete, 28 N on sand, robot weighs about 54 N), which is itself a terrain cue.
- C1 accepted (D28): walkable course built (gaps 2-6 cm, friction >= 0.22, bumps <= 1 cm, slopes <= 7 degrees). The best v2 policy crosses 19 of 20, G113 20 of 20, no falls: Part H's 80 % target is met before training. Next for H: fresh-seed confirmation, contact quality, and whether that policy is a distinct gait.
- A1 accepted (D27): layout matrices `fla_terrain/sim/layouts_v3.py` (pooled and subsampled pressure 1-40/full, shear 0/1/2/4), 16 tests pass in the manager's checkout, picture `results/v3/layouts_v3.png`. First number: the foot-shaped mask misses about half of the normal force in walking stance (box foot loads its edges).
- B1 accepted (D27): QCAT downloaded (CC BY 4.0, 0.43 GB, 360 trials = 6 terrains x 6 speeds x 10, 12 force + 10 IMU channels; front-left force sensor looks faulty). PUTany downloaded (ANYmal one-foot F/T, 8 classes, no speed labels, no data licence stated: internal use only). Published QCAT accuracy: 96.6 % force, 97.6 % force + IMU (10-fold step-level CV, optimistic).
- D27: the one amendment of D26 Q5 (splits: published-comparable step-level CV, trial-level CV, leave-one-speed-out), fixed before any real-data model.
- D25, D26 (pre-registered metrics) written at start.

### Next
- A3 launches the sweep; then A4 = real-like point reading and foot-shaped mask (Part C) while the GPU trains.
- B3 (QCAT models) still running; then B4 = Part G renders.
- C4 smoke + launch on viper; C5 evaluates its checkpoints on contact quality.

### Blockers
- The account's 5-hour usage limit stopped Worker B once (reset 02:10 UTC). All agents share it; tickets are kept lean. If it recurs, agents are resumed after the reset.

Last update: 2026-11-14 14:40 EET by the deputy manager on viper (v1 run start 2026-11-13; all times EET = UTC+2). **Run v1 is finished and closed. Run v2 is in progress**: see the first section.

## Итог прогона v2 (14.11, 08:35–15:57 EET)

**Открой `~/fla/results/v2/index.html`.** Полный отчёт: `REPORT_V2.md`. Прогон закончен, на серверах ничего не запущено.

**Главное.** Подошва теперь читается как карта точек (19×8 на стопу) поверх жёсткой стопы. На основном датасете карта давления заметно лучше четырёх блоков, особенно по частичной опоре. Но этот вывод не выдержал заранее записанную проверку: модели по карте, обученные на одном способе чтения подошвы, на другом теряют почти всё. Симуляции в этом пункте верить нельзя, пока нет реальных записей.

| № | Вопрос брифа | Ответ |
|---|---|---|
| 1 | Карта давления лучше четырёх блоков? | Да на основном датасете, по всем метрикам (частичная опора F1 0.80 против 0.47; террейн 0.877 против 0.829). **Не устойчиво**, см. п. 7 |
| 2 | Блочный сдвиг поверх карты что-то даёт? | С проприоцепцией разницы нет. Без неё F1 террейна выше на 2.6 пункта, остальное без разницы |
| 3 | Сдвиг по точкам лучше блочного? | Нет (с проприоцепцией ошибка по трению ниже, 0.141 против 0.158, а F1 частичной опоры хуже). В этой симуляции вопрос не проверяем: сдвиг по точкам выводится из общего сдвига стопы |
| 4 | Модели только по подошве лучше переносятся на новую походку? | Да, для всех пяти вариантов. На SONIC: 0.53 против 0.07 с проприоцепцией |
| 5 | Смешанная трасса: подошва против проприоцепции и правил | Подошва точнее проприоцепции (0.842 против 0.785) и раньше на 0.09 с. Детектор на правилах: 0.311, половина границ пропущена |
| 6 | Частичная опора на касаниях края от 0.3 с | С картой пропускается 2–3 % касаний, с блоками 27–28 %, по одной проприоцепции 37 % |
| 7 | Выводы переживают смену деталей симуляции? | Ответы 2 и 3 да. Ответ 1 нет: модели по карте падают с 0.86–0.88 до 0.20–0.27 на другой модели подошвы; блочные держат 0.59–0.76 |

**Что не получилось.**
- **Новая политика ходьбы:** закрыта по правилу брифа после трёх исправлений (лучший результат 10–14 трасс из 20 при цели 16). Всё посчитано на трёх источниках: G113, G80, SONIC.
- **Ни один источник не проходит трассу в 80 % случаев** (G113 19 из 40, G80 22, SONIC 6). Прогоны оцениваются до падения.
- **При ходьбе нагрузка по-прежнему сидит в углах.** Жёсткая стопа-коробка перекатывается через рёбра; в стойке и на клипах стенда нос и пятка нагружены ровно, как ты описывал, а при ходьбе нет. Это главное, что на роликах будет не похоже на реальную подошву.
- **Короткие касания края** (меньше 0.3 с) пропускают все модели в 74–85 % случаев.

**Что решено без тебя** (подробно в `DECISIONS.md`, D12–D24):
- маска точек прямоугольная, а не в форме стопы; форма стопы со скриншота вошла в проверку чувствительности (Q8);
- карта строится от суммарной силы, центра давления и крутящего момента стопы, а не от сил по блокам из решателя: при ходьбе решатель в трети шагов сваливает всю нагрузку на один блок (D13);
- податливость слоя снижена с 0.5 до 0.2 мм, чтобы середина стопы не касалась пола (D16);
- предел датчика 60 Н на точку оставлен как условное значение; ответы 1 и 2 от него не зависят (D19).

**Нужно от тебя** (`QUESTIONS.md`, Q8–Q12): форма стопы и середина подошвы (Q8, Q9), реальный диапазон датчика на точку (Q12). Самое полезное следующее действие — короткая запись с реальной подошвы: стойка, нажатия рукой, ходьба по двум поверхностям.

**Проверки.** Worker B пересчитал ключевые числа своим кодом (совпали до четвёртого знака), веса всех 156 моделей воспроизводят сохранённые предсказания, утечек нет, контроль с перемешанными метками даёт 0.062. Отчёт проверен по фактам: 24 замечания внесены.

**Где что.**
- Страница и ролики: `~/fla/results/v2/` (3 трассы, 3 крупных плана подошвы, 5 клипов стенда, 5 графиков). Страница v1 не менялась.
- Веса моделей: `viper:/data/kkolesni/fla-terrain/models/v2_src3/` (504 МБ), список в `results/v2/WEIGHTS.md`.
- Данные на viper: `data/v2` (8 ГБ), `data/v2_sens` (16 ГБ), `data/v2_course`. Кэши `data/v2_cache_*.npz` (24 ГБ) и `data/v2_pilot` (3.8 ГБ) можно удалить, они пересоздаются.
- Рендер шёл на viper через EGL, облако не использовалось. На adder было только обучение политики.

**Как шло.** С 09:05 до 14:54 EET Mac был без VPN (закрытая крышка), прогон вёл заместитель-менеджер на viper; его записи ниже. Команда воспроизведения всех моделей и таблиц: `scripts/run_v2.sh walk_g113,walk_g80,walk_sonic results/v2/src3 <папка моделей>`, затем `scripts/run_v2_src3_followup.sh`.

## Журнал прогона v2 (записи по ходу, включая заместителя)

**Основной менеджер (Mac) вернулся в 14:54 EET** и ведёт прогон дальше (D21); в 14:55 EET выдан B16 (вердикт по третьему исправлению политики на чекпойнте 500). Ниже — записи заместителя за время его работы.

**Заместитель-менеджер на viper был активен с 09:53 до 14:54 EET:** Mac молчал 49 минут (последний heartbeat 09:04 EET). В 09:56 EET выданы тикеты A8 (Worker A) и B9 (Worker B); B9 принят в 10:25, в 10:26 выдан B10 (рендеры). A8 и B10 приняты в 10:55; в 10:56 выданы A9 (все модели и таблицы) и B11 (оценка политики, финальная подгонка детектора, правки роликов). B11 принят в 11:25; B12 (проверка сдвига в записи датчика) принят в 11:40. Решения: `DECISIONS.md` D15–D19.

A10 (ветка теста чувствительности без насыщения) принят в 12:09. B13 (оценка чекпойнта 1000 новой политики) принят в 12:54. B14 принят в 13:54. B15 принят в 14:39: чекпойнт 200 третьего исправления хуже лучшего (6 трасс из 20 пройдено, 11 без падения; у run4 1000 было 11 и 15). Обучение продолжается, решение по третьему исправлению по чекпойнту 500 около 15:10 EET: если он не лучше, маршрут новой политики закрывается. Оба воркера свободны; обучение моделей: готово 118 из 147, сбоев нет.

**Проверка сдвига закрыта, найдено другое (D19, вопрос Q12):**
- Ролик стенда не показывает дефекта датчика: в том кадре левая стопа в самой симуляции несёт только 26.5 Н сдвига (она то держится, то скользит). Модель датчика сдвиг не теряет.
- Но при ходьбе срабатывает ограничение датчика 60 Н на точку (условное значение, перенесённое из v1). Стопа-коробка при постановке пятки и отталкивании грузит 2–4 угловые точки сотнями ньютонов. Около трети нагруженных кадров обрезаны; записанная сила стопы за шаг в среднем на 9–11 % ниже истинной, в худших случаях вдвое. Отношение сдвига к давлению при этом примерно сохраняется.
- Решение: датасет и идущее обучение не трогаю, а в тест чувствительности добавлена пятая ветка «без насыщения». Отчёт скажет, зависит ли какой-нибудь вывод от этого ограничения. Реальный диапазон датчика на точку неизвестен: это вопрос Q12 к тебе.

Идёт второй прогон по `docs/V2_BRIEF.md`: реалистичная подошва (карта точек вместо 2×4 зон), сравнение пяти вариантов датчика, новая политика ходьбы, смешанная трасса.

| Шаг (раздел 8 брифа) | Состояние на 13:55 EET |
|---|---|
| Подошва v2 и проверки | принято (D13): 17/17 проверок, перепроверено заместителем на `c76c72f` |
| Источники ходьбы на новой стопе | принято: G113, G80, SONIC в допусках брифа (0 падений из 64, скорость ±0.1 %) |
| Пилот | принят (D16), подошва не сломана, полный прогон начат |
| Определения метрик | записаны до датасета (D14) |
| Датасет v2 | принят (D17): 6139 эпизодов, 33.2 ч (train 21.9 / val 3.2 / test 8.1), три источника ходьбы, стойка, стенд, подъём, полосы смены поверхности, `hard-mid` только в тесте. Валидатор проходит на всех эпизодах, утечек между частями нет (проверено и заместителем). Падений 310 из 5869 |
| Наборы для теста чувствительности | приняты, добавлена пятая ветка «без насыщения» (1455 эпизодов, те же симуляции; номинальное чтение совпало с сохранённым побитно в 12 из 12 проверенных эпизодов). Worker A нашёл и исправил свою ошибку: варианты чтения отличались от номинала ещё и шумом проприоцепции, теперь только картой стопы. Состав: обучение на номинальной подошве (5.7 ч), 288 тестовых эпизодов в четырёх вариантах (номинал, сдвинутые параметры, контур стопы, подошва из отдельных площадок) |
| Записи трасс | приняты: по 40 трасс на источник, 64–75 с. Прошли все участки: G113 19, G80 22, SONIC 12. Остальные учитываются до падения (D16) |
| Модели и все таблицы D14 | **идёт обучение на viper** (PID 839440, лог `logs/wA_run_v2_src3.log`): 147 моделей на трёх источниках, готова 21, сбоев нет, конец ожидается в 15:30–16:00 EET. За ним в очереди (PID 859444, лог `logs/wA_run_v2_src3_queued.log`) ветка «без насыщения», оценка детектора на правилах на трассах и итоговые таблицы, ещё около 30 минут. Проверка одной командой: `scripts/v2_status.sh`. Таблицы и вердикты считает код в конце. Модели по карте точек запоминали индивидуальную калибровку каждого эпизода; Worker A добавил случайные усиление и смещение на каждое окно при обучении (D19). Первые числа (тест, ходьба): P даёт F1 террейна 0.82 и F1 частичной опоры 0.34–0.37; P + карта давления + сдвиг по точкам даёт 0.85–0.88 и 0.79–0.82 |
| Новая политика ходьбы | **не принята; обучается третье, последнее исправление на adder**: v2_run6, PID 369097, лог `adder:/data/kkolesni/fla-terrain/k1v2/logs/v2_run6.log`, старт 13:43 EET. Лучший чекпойнт пока — run4 1000: все участки пройдены в 11 трассах из 20, без падения 15 из 20 (цель 16). Второе исправление (больше досок, щели, строгий критерий уровня) провалилось: политика разучилась, чекпойнт 300 не прошёл ни одной трассы; запуск остановлен. Третье: старт с run4 1000, прежний рельеф с чуть большей долей досок, меньший шаг обновления, больший вес скорости вперёд. Оценки около 14:20, 15:10 и 16:35 EET. Если и оно не даст прогресса, маршрут закрывается по правилу остановки, и отчёт строится на трёх источниках |
| Детектор на правилах | принят: пороги подобраны только на train-части v2. F1 террейна 0.30 (val) и 0.29 (test), F1 опоры 0.62. Предсказания для 120 трасс записаны |
| Рендеры | EGL на viper работает, облако не нужно. 10 роликов в `viper:/data/kkolesni/fla-terrain/render/v2/`; камера в роликах стенда исправлена. Итоговые ролики трасс ждут предсказаний моделей |
| Отчёт | не начато |

**Пилот** (G113; hard-grip, hard-slip, edge; 5 ч данных, один сид, поэтому это направление, а не результат):

| Вход | F1 террейна | F1 опоры | F1 частичной опоры |
|---|---|---|---|
| P + N_real + S_real | 0.792 | 0.804 | 0.559 |
| P + N_real + S_blk | 0.850 | 0.922 | 0.815 |
| P + N_real | 0.910 | 0.925 | 0.821 |
| P + N_blk + S_blk | 0.873 | 0.833 | 0.615 |
| P + N_blk | 0.887 | 0.842 | 0.636 |
| P | 0.854 | 0.794 | 0.518 |

- Реалистичная карта отличается от четырёх блоков на частичной опоре (0.82 против 0.62–0.64). По классу террейна на одном сиде различий не видно. Сдвиг по точкам ухудшил результат.
- Генерация в 2.3 раза медленнее v1 на секунду симуляции; 220 МБ на час данных (v1: 49 МБ). Датасет на 35 ч займёт около 8 ГБ.
- Странное в картах: при ходьбе по ровному полу средняя часть стопы несла 5–6 % нагрузки, хотя по твоему описанию она пола не касается. Причина в податливости слоя 0.5 мм на 100 Н. Перед полным прогоном она уменьшена до 0.2 мм (диапазон 0.1–0.4), проверки подошвы перезапускаются (D16).
- Вопрос 3 брифа (сдвиг по точкам против блочного) в этой симуляции проверяет только обработку шума, а не физику: сдвиг по точкам полностью выводится из карты давления и трёх чисел на стопу (Q11).

**Трасса, исходный уровень на стопе v2** (20 трасс, 60 с): G113 дошёл в 8 из 20, G80 в 14, SONIC в 10. Политики скорости падают в основном на скользких участках с трением около 0.1, SONIC на краях.

**Что стоит знать о данных v2:** с податливостью 0.2 мм средняя часть стопы при ходьбе по ровному полу несёт в среднем 4 % нагрузки (медиана 0, в стойке 0). В сырых картах при постановке пятки один угловой датчик упирается в предел 60 Н: так ведёт себя жёсткая стопа-коробка.

- Серверы: обучение политики на adder (GPU делится с чужим Folding@home, его процессы не трогаю), всё остальное на viper. Облачный GPU не арендуется.

## Дополнение 14.11, 07:52 EET: видео, графики и одна папка `~/fla`

**Открой `~/fla/results/index.html`.** Там сводка, монтаж, графики, все ролики, вердикт G1 дословно из отчёта и оговорки. Новых экспериментов не было, ни одно число отчёта не изменилось.

**Что где в `~/fla`:** `results/` (страница, `videos/`, `figures/`, копии отчётов), `fla-terrain/` (репозиторий, перенесён через `mv`, git и remote `viper` работают), `briefs/` (оба брифа), `data_sample/` (по два тестовых эпизода на класс и бандлы клипов), `README.md`.

**Ролики** (1280×720, 30 fps, H.264, по 10 с; слева робот, справа тепловая карта подошвы и ответ модели P+N рядом с истиной):

| Файл | Что показывает |
|---|---|
| `montage_terrains.mp4` | шесть поверхностей одновременно, G113 |
| `terrain_{hard_grip,hard_slip,soft,rough,slope,edge}_g113.mp4` | по одному клипу на класс, политика G113 |
| `terrain_{hard_grip,hard_slip}_sonic.mp4` | те же две поверхности с SONIC-K1: видно другую походку |
| `strip_grip_slip_g113.mp4` | смена grip → slip в 6.40 с; модель переключается в 6.80 с (0.40 с, 1 шаг) |
| `lifted_mid_walk_g113.mp4` | робота поднимают на ходу в 4.14 с; силы на карте падают до нуля, модель сообщает «airborne» через 0.02 с |
| `failure_edge_miss_g113.mp4` | ошибка: левая стопа 0.6 с стоит на краю доски, модель ни разу не говорит «partial» |

**Графики** (`figures/`, скрипт `scripts/make_figures.py`): абляция, матрица ошибок P+N, опора по классам, задержки, перенос между походками (помечен exploratory), схема подошвы. Все 237 значений сверены с `tables.md` самим скриптом.

**Где считалось и почему.** Ты сказал делать в Google Cloud на GPU, а не на Mac, поэтому варианты «Mac» и «viper» из брифа я не пробовал. Симуляция, графики, страница и тесты шли на viper (adder по-прежнему занят чужими задачами: загрузка 91–96 на 96 ядрах). Рендер шёл на одной машине `n1-standard-8` + Tesla P4 в проекте `sonic-506520`, 15 минут, примерно 0.3 USD по прайсу (точная сумма будет в биллинге). Машина и диск удалены:

```
$ gcloud compute instances list --project sonic-506520
Listed 0 items.
$ gcloud compute disks list --project sonic-506520
Listed 0 items.
```

**Проверки из брифа:**
- из каждого MP4 извлечены три кадра (начало, середина, конец) и просмотрены: робот виден и стоит, панель читается, чёрных кадров нет;
- в клипе со сменой поверхности класс на видео меняется в 6.80 с — это и есть заявленная для эпизода задержка 0.40 с;
- при подъёме сумма Fz не превышает 1.7 Н (шум датчика);
- в стойке сумма Fz обеих стоп 188–197 Н при весе 192.9 Н (в модели датчика ошибка усиления 3 %);
- тесты репозитория: 57 из 57 (запускал на viper на том же коммите, не на Mac).

**Что пошло не так или отличается от брифа:**
- **Чекпойнта P+N нет:** абляция сохраняла только предсказания, а переобучать бриф запрещает. На панели — сохранённые тестовые предсказания P+N seed 0 для того же эпизода; каждый эпизод пересимулирован и побитно совпал с датасетом (подробно в D11).
- **GPU достался не сразу:** spot-машину с T4 Google вытеснил через 2.5 минуты, on-demand T4 и L4 не было ни в одной зоне, взял P4; в образе пришлось заменить драйвер.
- **Ответ модели на панели обновляется раз в 0.2 с**, а не каждый кадр: так модель оценивалась в отчёте. Тепловая карта обновляется на каждом кадре датчика (50 Гц).
- **Клипы без падений.** На hard-slip G113 упал в 16 из 36 тестовых эпизодов; на странице это написано.
- **Одно новое число на странице:** из 594 пропущенных касаний края 477 короче 0.3 с. Оно посчитано по тем же предсказаниям и помечено как отсутствующее в отчёте.
- **Страницу в браузере проверял headless-снимком и проверкой ссылок**, вживую ролики не проигрывал.

## Утренняя сводка для Кирилла

**Что работает**
- Весь конвейер в симуляции: схема данных v0.2, виртуальная подошва на K1 (2 x 4 зоны на стопу, силы в системе подошвы, модель сенсора 150 -> 50 Гц), шесть классов террейнов с непересекающимися диапазонами train/val/test, датасет v1 (4572 эпизода, 24.7 ч), бейзлайн LightGBM, CNN с тремя головами, абляция на 3 сидах. Все обязательные проверки подошвы пройдены (6/6), 68 тестов зелёные.
- Ходьба есть, причём три разные походки: твои политики G113 m2200 и G80 m4200 и SONIC-K1. Обучать ничего не пришлось, все три проигрываются в MuJoCo. Заголовочные цифры получены на ходьбе.
- Дополнительно сделаны оба опциональных пункта: зонд «подошва из проприоцепции» и заглушка конвертера `real/convert.py` для реальной сетки такселей.

**Что не работает или не сделано**
- Сдвиг не прошёл критерий G1 (ниже).
- Модели жёстко привязаны к походке: на походке, которой не было в обучении, F1 падает на 17-54 пункта, а на SONIC перенос нулевой (0.07-0.11, как у контроля с перемешанными метками).
- Частичная опора распознаётся слабо даже с подошвой (F1 0.63), 28-29 % касаний с частичной опорой пропускаются.
- Распределение сил по зонам в твёрдотельном симуляторе - численный артефакт, не физика эластомера. Это главная оговорка ко всем выводам про зоны и сдвиг.
- Спайк в Isaac/PhysX не делался (решение D3). Видео нет: на viper нет рендера.

**Таблица абляции (ходьба, тест, среднее по 3 сидам)**

| Вход | macro-F1 террейна | F1 grip/slip | MAE трения | F1 опоры |
|---|---|---|---|---|
| P (суставы, IMU, команда) | 0.802 | 0.948 | 0.186 | 0.755 |
| P+N (+ Fz по зонам) | 0.861 | 0.975 | 0.166 | 0.866 |
| P+N+S (+ Fx, Fy по зонам) | 0.860 | 0.972 | 0.150 | 0.853 |

**Вердикт G1: не выполнен, 0 из 3.** Сдвиг не достиг ни одного заранее заданного порога.
- Критерий 1 (+5 пунктов F1 grip/slip): -0.3 пункта. Был арифметически недостижим: P+N уже даёт 0.975, максимум прироста +2.5.
- Критерий 2 (смена поверхности на шаг раньше): 2 и 2 шага; в секундах 0.52 и 0.55.
- Критерий 3 (MAE трения на 20 % ниже): -10 %.
- Сдвиг снизил ошибку трения во всех трёх сидах (-18 % на скользком, -23 % на стенде стопы), но выигрыш хрупкий: без каналов команды на одном сиде порядок переворачивается.
- Проприоцепция одна задачу не решает (частичная опора 0.35, края пропускает в половине случаев), но grip/slip решает почти полностью (0.948).
- Нормальная сила по зонам полезна: +6 пунктов по террейну, +11 по опоре, подъём в воздух обнаруживается за 0.07 с вместо 0.29 с.
- Вывод относится к этой симуляции. На реальной подошве сдвиг может вести себя иначе: в твёрдотельной модели нет частичного проскальзывания в пятне контакта.

**Сервер и симулятор**
- Всё считалось на **viper**: adder был целиком занят чужим Folding@home (нагрузка 101 на 96 ядер, GPU 91 %). С adder только читались твои K1-материалы.
- Симулятор **MuJoCo 4.0.1** на CPU: твои политики уже проигрываются в MuJoCo, на viper нет рендера и не работает конвертация URDF -> USD, MuJoCo отдаёт полную 3D-силу каждого контакта.
- Воркеры по твоей просьбе работали прямо на viper как headless-сессии Claude Code (Opus 5.5).

**Что я решил сам** (`DECISIONS.md`, D1-D10): перенос обоих треков на viper; MuJoCo вместо Isaac; воркеры на сервере; заместитель-менеджер на случай разряда Mac (не понадобился); маршрут SONIC передан Worker B; определения метрик и критериев G1 зафиксированы до генерации датасета (D7); после вердикта не добавлял ни новых диапазонов трения, ни вариантов критериев.

**Что нужно от тебя** (`QUESTIONS.md`, 7 вопросов). Главные:
1. Переформулировать ли критерий перед сбором реальных данных (частичная опора, начало проскальзывания, перенос на новую походку)?
2. Какой контроллер будет работать на реальном K1 при записи? Его походка обязана быть в обучении.
3. Стоит ли строить податливую модель подошвы? Моя оценка: твёрдотельная симуляция на вопрос о сдвиге больше не ответит.

**Одна команда для воспроизведения** (viper, чистый клон репозитория):

```
scripts/run_ablation.sh /data/kkolesni/fla-terrain/data/v1 results/v1
```

Воспроизводимость проверена трижды: два прогона Worker A и мой отдельный прогон в чистом клоне совпали до 0.0000. Ключевые метрики независимо пересчитаны Worker B своим кодом из сырых эпизодов, тоже с разницей 0.0000.

**Моя ошибка в ходе работы:** время в сообщениях и в логах я поначалу писал по оценке, а не по часам, и оно уплыло почти на три часа. Исправлено по времени коммитов (D9). На результаты не влияет.

## Where things are

- Mac: `~/fla/fla-terrain` (branch `main`, remote `viper`); moved there from `~/fla-terrain` on 2026-11-14. Results folder with videos and figures: `~/fla/results/` (open `index.html`). Read `REPORT.md` first, then `QUESTIONS.md`.
- viper: `/data/kkolesni/fla-terrain/` — `repo.git` (bare origin), `a/` and `b/` (worker checkouts), `m/` (manager checkout), `data/v1` (dataset, 1.2 GB), `mgr_results/v1` (manager's verification run), `logs/`, `agents/` (worker prompts and reports of every turn), `b_ext/` (copies of the K1 policies and assets), `b_runs/sonic` (SONIC weights and clips, 113 MB, not in git).
- Env: `/data/kkolesni/.conda/envs/env_fla`. `env_isaaclab` and the IsaacLab checkout were not touched.

## Tickets

| Ticket | Owner | State |
|---|---|---|
| T1 schema/loader | A | accepted |
| T2 shear spike (MuJoCo) | A | accepted |
| T3 virtual sole (6/6 checks) | A | accepted |
| A2 velocity policies, A1 SONIC-K1 | B | accepted |
| T4 terrains | A | accepted |
| T5 dataset v1 | A | accepted, independently QA'd by B |
| T6 LightGBM baseline | A | accepted |
| T7 model + ablation | A | accepted; clean run reproduced by A and by the manager |
| Optional: virtual-sole probe, real/convert stub | B | accepted |
| Independent metric recomputation, code review, shuffle control, report fact-check | B | accepted |
| T8 report | manager | done |

## Running jobs (v2)

- adder: policy training v2_run6, PID 369097, log `adder:/data/kkolesni/fla-terrain/k1v2/logs/v2_run6.log`.
- viper: model training pipeline (Worker A), PID 839440, log `logs/wA_run_v2_src3.log`.
- viper: both workers idle (A until the training job ends, B until the v2_run6 model_500 evaluation at about 13:10 UTC); queued follow-up job PID 859444, log `logs/wA_run_v2_src3_queued.log`; deputy watchdog `agents/watchdog.sh` ticking every 15 minutes.
