flat course, v2 foot, plain command 0.35 m/s, auto-T, seeds 0..3; commit a7a9cc1 clean

| policy | crossed | falls | off course | timed out | course speed |
|---|---|---|---|---|---|
| G113_m2200 | 0/4 | 0 | 0 | 4 | 0.356 |
| SONIC | 0/4 | 0 | 0 | 4 | 0.455 |

Per chunk type: entries / falls (incl. off course) / fall rate

| policy | flat | start/end |
|---|---|---|
| G113_m2200 | 4 / 0 / 0.00 | 0 |
| SONIC | 4 / 0 / 0.00 | 0 |

Contact quality per stance (simulator state), median / p90; partial also as mean

| policy | stances | impact, 1 step (x BW) | impact, 10 ms (x BW) | slip in stance (mm) | partial-support fraction | partial mean |
|---|---|---|---|---|---|---|
| G113_m2200 | 144 | 16.67 / 19.39 | 3.43 / 3.88 | 11.0 / 12.1 | 0.00 / 0.00 | 0.000 |
| SONIC | 91 | 4.20 / 6.96 | 1.29 / 2.25 | 13.5 / 15.0 | 0.00 / 0.00 | 0.000 |

Gait descriptors (pooled; pitch, CoP travel, stance duration = medians over stances)

| policy | steps/s | stance fraction | stance (s) | foot pitch at touchdown (deg, heel first > 0) | CoP travel p10-p90 (mm) | stance with CoP in back third |
|---|---|---|---|---|---|---|
| G113_m2200 | 1.89 | 0.573 | 0.60 | 16.9 | 180 | 0.30 |
| SONIC | 1.26 | 0.603 | 0.70 | 9.8 | 180 | 0.28 |
