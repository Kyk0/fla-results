v2 course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..19; commit ee73f36 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 11/20 | 5 | 0 | 4 | 0.330 |
| K1V3_r2_m500 | 10/20 | 5 | 0 | 5 | 0.323 |
| K1V3_r2_m1000 | 0/20 | 3 | 14 | 3 | 0.276 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 22 / 0 / 0.00 | 26 / 0 / 0.00 | 21 / 1 / 0.05 | 22 / 1 / 0.05 | 24 / 0 / 0.00 | 15 / 3 / 0.20 | 13 / 0 / 0.00 | 0 |
| K1V3_r2_m500 | 21 / 0 / 0.00 | 24 / 1 / 0.04 | 19 / 0 / 0.00 | 22 / 0 / 0.00 | 25 / 0 / 0.00 | 14 / 4 / 0.29 | 13 / 0 / 0.00 | 0 |
| K1V3_r2_m1000 | 17 / 6 / 0.35 | 13 / 0 / 0.00 | 15 / 0 / 0.00 | 14 / 2 / 0.14 | 16 / 4 / 0.25 | 10 / 4 / 0.40 | 6 / 1 / 0.17 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 3033 | 23.77 / 31.29 | 5.13 / 6.49 | 19.4 / 35.6 | 0.00 / 0.00 | 0.085 |
| K1V3_r2_m500 | 2960 | 24.32 / 36.03 | 5.14 / 7.41 | 18.8 / 37.1 | 0.00 / 0.00 | 0.088 |
| K1V3_r2_m1000 | 2014 | 22.82 / 29.83 | 4.87 / 6.19 | 15.7 / 41.7 | 0.00 / 0.00 | 0.088 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.36 | 0.547 | 0.54 | 19.7 | 146 | 0.41 |
| K1V3_r2_m500 | 2.35 | 0.537 | 0.48 | 19.1 | 143 | 0.53 |
| K1V3_r2_m1000 | 2.28 | 0.544 | 0.46 | 14.9 | 115 | 0.44 |
