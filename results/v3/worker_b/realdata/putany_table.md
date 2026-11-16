# PUTany temporal models (B6)

*PUTany: ANYmal, one foot force/torque sensor, real hardware; not a humanoid pressure map. No data licence stated: internal analysis only.*

TerrainNet (fla_terrain.models.nets, unchanged body), 8-class head; AdamW lr 0.01, max 60 epochs, cosine, batch 64, early stop on val accuracy (patience 15); lr chosen on val only. Given split: train 3443 / val 1148 / test 1148. Five seeds (0-4).
Commits: ['4734261ce29bc6ed6208e108a46153d84ce334e0 clean']

Published, same hold-out test set (TS-Rep, NeurIPS 2022 SSL workshop, Table 6): HAPTR 91.7 %, HAPTR2 92.7 %, CNN-RNN 93.0 %, TCN 87.5 % (force + torque).


## Test accuracy and macro-F1 (%, mean ± std over 5 seeds)

*PUTany: ANYmal, one foot force/torque sensor, real hardware; not a humanoid pressure map. No data licence stated: internal analysis only.*

| input | channels | accuracy | macro-F1 | seeds (acc) |
|---|---|---|---|---|
| normal | 1 | 65.8 ± 1.0 | 62.0 ± 1.2 | 63.9, 66.1, 66.5, 66.8, 65.6 |
| force3 | 3 | 64.9 ± 2.7 | 62.4 ± 2.6 | 63.1, 64.4, 62.6, 64.6, 70.0 |
| force+torque | 6 | 91.0 ± 0.5 | 88.9 ± 0.7 | 90.9, 91.0, 90.2, 91.6, 91.2 |

Shuffled-label control (force3, seed 0, train and val labels permuted, test labels true): accuracy 21.1 % (chance 12.5 %, majority class 22.6 %).
