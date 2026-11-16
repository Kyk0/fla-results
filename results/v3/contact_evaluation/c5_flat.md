flat course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..15; commit 72f6fd3 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| K1V2_r4_m1000 | 0/16 | 0 | 0 | 16 | 0.348 |
| K1V3_r1_m300 | 0/16 | 0 | 0 | 16 | 0.313 |
| K1V3_r1_m600 | 0/16 | 0 | 0 | 16 | 0.321 |
| K1V3_r1_m1000 | 0/16 | 0 | 0 | 16 | 0.305 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | flat | start/end |
|---|---|---|
| K1V2_r4_m1000 | 16 / 0 / 0.00 | 0 |
| K1V3_r1_m300 | 16 / 0 / 0.00 | 0 |
| K1V3_r1_m600 | 16 / 0 / 0.00 | 0 |
| K1V3_r1_m1000 | 16 / 0 / 0.00 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 579 | 25.73 / 30.80 | 5.40 / 6.27 | 18.6 / 22.0 | 0.00 / 0.00 | 0.000 |
| K1V3_r1_m300 | 582 | 27.47 / 34.08 | 5.76 / 7.10 | 21.9 / 25.9 | 0.00 / 0.00 | 0.000 |
| K1V3_r1_m600 | 579 | 27.05 / 32.97 | 5.68 / 6.97 | 13.9 / 18.0 | 0.00 / 0.00 | 0.000 |
| K1V3_r1_m1000 | 580 | 26.30 / 30.35 | 5.51 / 6.26 | 17.0 / 19.5 | 0.00 / 0.00 | 0.000 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| K1V2_r4_m1000 | 1.90 | 0.524 | 0.56 | 21.6 | 170 | 0.43 |
| K1V3_r1_m300 | 1.91 | 0.515 | 0.54 | 23.3 | 160 | 0.57 |
| K1V3_r1_m600 | 1.90 | 0.514 | 0.52 | 24.2 | 134 | 0.67 |
| K1V3_r1_m1000 | 1.91 | 0.506 | 0.50 | 19.8 | 92 | 0.68 |
