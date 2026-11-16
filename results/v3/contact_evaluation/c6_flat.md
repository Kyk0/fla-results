flat course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..15; commit ee73f36 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 0/16 | 0 | 0 | 16 | 0.348 |
| K1V3_r2_m500 | 0/16 | 0 | 0 | 16 | 0.332 |
| K1V3_r2_m1000 | 0/16 | 0 | 0 | 16 | 0.278 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | flat | start/end |
|---|---|---|
| K1V2_r4_m1000 | 16 / 0 / 0.00 | 0 |
| K1V3_r2_m500 | 16 / 0 / 0.00 | 0 |
| K1V3_r2_m1000 | 16 / 0 / 0.00 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 579 | 25.73 / 30.80 | 5.40 / 6.27 | 18.6 / 22.0 | 0.00 / 0.00 | 0.000 |
| K1V3_r2_m500 | 601 | 26.90 / 36.62 | 5.62 / 7.45 | 18.4 / 22.9 | 0.00 / 0.00 | 0.000 |
| K1V3_r2_m1000 | 578 | 23.36 / 27.76 | 4.91 / 5.66 | 14.3 / 18.0 | 0.00 / 0.00 | 0.000 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 1.90 | 0.524 | 0.56 | 21.6 | 170 | 0.43 |
| K1V3_r2_m500 | 1.98 | 0.518 | 0.50 | 20.1 | 161 | 0.56 |
| K1V3_r2_m1000 | 1.90 | 0.512 | 0.51 | 15.7 | 136 | 0.41 |
