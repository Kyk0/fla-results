walkable course, v2 foot, plain command 0.35 m/s, auto-T, seeds 1000..1039; commit 72f6fd3 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 38/40 | 0 | 1 | 2 | 0.338 |
| K1V3_r1_m300 | 0/40 | 0 | 1 | 39 | 0.299 |
| K1V3_r1_m600 | 8/40 | 0 | 24 | 9 | 0.313 |
| K1V3_r1_m1000 | 0/40 | 0 | 31 | 9 | 0.291 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 53 / 0 / 0.00 | 52 / 0 / 0.00 | 61 / 0 / 0.00 | 28 / 0 / 0.00 | 27 / 0 / 0.00 | 1 |
| K1V3_r1_m300 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 52 / 1 / 0.02 | 51 / 0 / 0.00 | 58 / 0 / 0.00 | 27 / 0 / 0.00 | 27 / 0 / 0.00 | 0 |
| K1V3_r1_m600 | 43 / 4 / 0.09 | 45 / 1 / 0.02 | 42 / 5 / 0.12 | 40 / 6 / 0.15 | 50 / 5 / 0.10 | 21 / 1 / 0.05 | 20 / 1 / 0.05 | 1 |
| K1V3_r1_m1000 | 37 / 6 / 0.16 | 39 / 6 / 0.15 | 35 / 6 / 0.17 | 34 / 3 / 0.09 | 40 / 6 / 0.15 | 18 / 0 / 0.00 | 17 / 4 / 0.24 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 5952 | 24.25 / 30.99 | 5.15 / 6.47 | 19.9 / 32.1 | 0.00 / 0.00 | 0.071 |
| K1V3_r1_m300 | 6115 | 25.39 / 33.74 | 5.28 / 7.09 | 21.7 / 34.1 | 0.00 / 0.00 | 0.080 |
| K1V3_r1_m600 | 4881 | 25.92 / 33.96 | 5.46 / 7.12 | 15.8 / 31.6 | 0.00 / 0.00 | 0.076 |
| K1V3_r1_m1000 | 4432 | 25.62 / 31.73 | 5.45 / 6.57 | 17.8 / 34.4 | 0.00 / 0.00 | 0.086 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.06 | 0.552 | 0.56 | 20.5 | 158 | 0.41 |
| K1V3_r1_m300 | 2.12 | 0.540 | 0.54 | 19.7 | 145 | 0.55 |
| K1V3_r1_m600 | 2.09 | 0.532 | 0.50 | 22.9 | 111 | 0.66 |
| K1V3_r1_m1000 | 2.14 | 0.523 | 0.48 | 19.6 | 88 | 0.64 |
