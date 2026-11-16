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
