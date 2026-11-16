v2 course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..19; commit 72f6fd3 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 11/20 | 5 | 0 | 4 | 0.330 |
| K1V3_r1_m300 | 0/20 | 5 | 1 | 14 | 0.284 |
| K1V3_r1_m600 | 2/20 | 3 | 11 | 4 | 0.301 |
| K1V3_r1_m1000 | 0/20 | 4 | 12 | 4 | 0.281 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 22 / 0 / 0.00 | 26 / 0 / 0.00 | 21 / 1 / 0.05 | 22 / 1 / 0.05 | 24 / 0 / 0.00 | 15 / 3 / 0.20 | 13 / 0 / 0.00 | 0 |
| K1V3_r1_m300 | 21 / 0 / 0.00 | 23 / 1 / 0.04 | 19 / 0 / 0.00 | 19 / 0 / 0.00 | 24 / 0 / 0.00 | 13 / 5 / 0.38 | 12 / 0 / 0.00 | 0 |
| K1V3_r1_m600 | 21 / 1 / 0.05 | 23 / 4 / 0.17 | 19 / 1 / 0.05 | 17 / 1 / 0.06 | 21 / 2 / 0.10 | 12 / 3 / 0.25 | 10 / 2 / 0.20 | 0 |
| K1V3_r1_m1000 | 18 / 4 / 0.22 | 18 / 3 / 0.17 | 16 / 1 / 0.06 | 15 / 0 / 0.00 | 17 / 1 / 0.06 | 11 / 5 / 0.45 | 9 / 2 / 0.22 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 3033 | 23.77 / 31.29 | 5.13 / 6.49 | 19.4 / 35.6 | 0.00 / 0.00 | 0.085 |
| K1V3_r1_m300 | 2840 | 24.82 / 33.76 | 5.21 / 7.07 | 20.8 / 38.5 | 0.00 / 0.54 | 0.099 |
| K1V3_r1_m600 | 2568 | 25.47 / 34.61 | 5.41 / 7.17 | 15.6 / 36.3 | 0.00 / 0.00 | 0.088 |
| K1V3_r1_m1000 | 2233 | 25.73 / 32.67 | 5.46 / 6.80 | 17.6 / 39.3 | 0.00 / 0.89 | 0.110 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.36 | 0.547 | 0.54 | 19.7 | 146 | 0.41 |
| K1V3_r1_m300 | 2.28 | 0.539 | 0.52 | 18.8 | 138 | 0.55 |
| K1V3_r1_m600 | 2.31 | 0.531 | 0.48 | 21.5 | 99 | 0.65 |
| K1V3_r1_m1000 | 2.23 | 0.520 | 0.48 | 18.1 | 88 | 0.65 |
