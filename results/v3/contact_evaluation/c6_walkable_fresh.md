walkable course, v2 foot, plain command 0.35 m/s, auto-T, seeds 1000..1039; commit ee73f36 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 38/40 | 0 | 1 | 2 | 0.338 |
| K1V3_r2_m500 | 24/40 | 0 | 1 | 15 | 0.330 |
| K1V3_r2_m1000 | 0/40 | 0 | 36 | 4 | 0.279 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | hard_grip | hard_slip | soft | rough | slope | edge-planks | edge-steps | start/end |
|---|---|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 53 / 0 / 0.00 | 52 / 0 / 0.00 | 61 / 0 / 0.00 | 28 / 0 / 0.00 | 27 / 0 / 0.00 | 1 |
| K1V3_r2_m500 | 50 / 0 / 0.00 | 49 / 0 / 0.00 | 53 / 0 / 0.00 | 52 / 1 / 0.02 | 61 / 0 / 0.00 | 27 / 0 / 0.00 | 27 / 0 / 0.00 | 0 |
| K1V3_r2_m1000 | 28 / 5 / 0.18 | 31 / 5 / 0.16 | 27 / 1 / 0.04 | 32 / 6 / 0.19 | 28 / 11 / 0.39 | 14 / 4 / 0.29 | 15 / 4 / 0.27 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 5952 | 24.25 / 30.99 | 5.15 / 6.47 | 19.9 / 32.1 | 0.00 / 0.00 | 0.071 |
| K1V3_r2_m500 | 6081 | 24.62 / 35.73 | 5.12 / 7.36 | 19.6 / 33.4 | 0.00 / 0.00 | 0.079 |
| K1V3_r2_m1000 | 3332 | 23.72 / 29.74 | 5.00 / 6.15 | 15.9 / 33.5 | 0.00 / 0.00 | 0.066 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 2.06 | 0.552 | 0.56 | 20.5 | 158 | 0.41 |
| K1V3_r2_m500 | 2.11 | 0.543 | 0.50 | 19.4 | 151 | 0.54 |
| K1V3_r2_m1000 | 2.08 | 0.539 | 0.50 | 15.9 | 120 | 0.42 |
