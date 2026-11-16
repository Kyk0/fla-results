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
