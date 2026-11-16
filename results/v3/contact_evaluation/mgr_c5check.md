flat course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..3; commit 5af738c clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V3_r1_m1000 | 0/4 | 0 | 0 | 4 | 0.304 |
| K1V2_r4_m1000 | 0/4 | 0 | 0 | 4 | 0.351 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | flat | start/end |
|---|---|---|
| K1V3_r1_m1000 | 4 / 0 / 0.00 | 0 |
| K1V2_r4_m1000 | 4 / 0 / 0.00 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V3_r1_m1000 | 145 | 26.00 / 30.39 | 5.47 / 6.25 | 16.8 / 19.0 | 0.00 / 0.00 | 0.000 |
| K1V2_r4_m1000 | 146 | 26.10 / 31.56 | 5.42 / 6.37 | 19.1 / 23.2 | 0.00 / 0.00 | 0.000 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V3_r1_m1000 | 1.91 | 0.506 | 0.50 | 22.7 | 97 | 0.68 |
| K1V2_r4_m1000 | 1.92 | 0.524 | 0.55 | 21.7 | 167 | 0.44 |
