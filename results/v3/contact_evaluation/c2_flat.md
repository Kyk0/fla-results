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
