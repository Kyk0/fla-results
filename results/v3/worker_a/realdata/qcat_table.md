# QCAT temporal models (B3)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

TerrainNet (fla_terrain.models.nets, unchanged body), 6-class head; AdamW lr 0.01, max 60 epochs, cosine, batch 64, early stop on inner-val accuracy (patience 15). Five seeds (0-4).
Per seed: mean over folds; table: mean ± std over the 5 seeds. Commits: ['9a7d478c1affa235505ce948aedf404963e36d23 clean', 'eef85d4acad4a579e6b2c9389abd43dacac99a73 clean']

Published (Ahmadi et al. 2021, 10-fold step-level CV): force 96.6 %, IMU 96.63 %, force + IMU 97.64 %.


## Accuracy (%)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

| input | step10 | trial10 | loso | lofo |
|---|---|---|---|---|
| normal | 92.1 ± 0.3 (n=5) | 88.6 ± 0.3 (n=5) | 83.4 ± 0.6 (n=5) | 71.6 ± 1.3 (n=5) |
| force3 | 94.3 ± 0.4 (n=5) | 92.7 ± 0.4 (n=5) | 89.0 ± 0.4 (n=5) | 79.8 ± 1.6 (n=5) |
| imu | 97.7 ± 0.2 (n=5) | 92.5 ± 1.1 (n=5) | 78.1 ± 0.9 (n=5) | 73.9 ± 0.8 (n=5) |
| force3+imu | 98.2 ± 0.2 (n=5) | 96.3 ± 0.4 (n=5) | 88.8 ± 0.5 (n=5) | 83.8 ± 1.4 (n=5) |
| force3_noFL | 94.0 ± 0.2 (n=5) | 92.9 ± 0.2 (n=5) | 88.7 ± 0.1 (n=5) | 76.1 ± 2.4 (n=5) |
| normal_noFL | 92.2 ± 0.5 (n=5) | 88.4 ± 0.6 (n=5) | 83.8 ± 0.4 (n=5) | 71.1 ± 1.7 (n=5) |

## Terrain macro-F1 (x100)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

| input | step10 | trial10 | loso | lofo |
|---|---|---|---|---|
| normal | 92.1 ± 0.3 (n=5) | 88.6 ± 0.4 (n=5) | 83.3 ± 0.6 (n=5) | 71.0 ± 1.3 (n=5) |
| force3 | 94.3 ± 0.4 (n=5) | 92.7 ± 0.4 (n=5) | 88.9 ± 0.4 (n=5) | 79.4 ± 1.8 (n=5) |
| imu | 97.7 ± 0.2 (n=5) | 92.4 ± 1.1 (n=5) | 77.2 ± 1.0 (n=5) | 72.5 ± 1.0 (n=5) |
| force3+imu | 98.2 ± 0.2 (n=5) | 96.3 ± 0.4 (n=5) | 88.0 ± 0.5 (n=5) | 83.1 ± 1.7 (n=5) |
| force3_noFL | 94.0 ± 0.2 (n=5) | 92.8 ± 0.2 (n=5) | 88.5 ± 0.1 (n=5) | 75.9 ± 2.5 (n=5) |
| normal_noFL | 92.1 ± 0.5 (n=5) | 88.4 ± 0.6 (n=5) | 83.7 ± 0.4 (n=5) | 70.1 ± 1.7 (n=5) |

## Leave-one-speed-out: accuracy per held-out speed (%, mean ± std over seeds)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

| input | speed 1 (0.125 Hz, 80 mm) | speed 2 (0.125 Hz, 120 mm) | speed 3 (0.1875 Hz, 80 mm) | speed 4 (0.1875 Hz, 120 mm) | speed 5 (0.25 Hz, 80 mm) | speed 6 (0.25 Hz, 120 mm) |
|---|---|---|---|---|---|---|
| normal | 68.7 ± 1.4 | 77.0 ± 2.1 | 84.4 ± 1.3 | 90.0 ± 0.9 | 91.8 ± 0.9 | 88.5 ± 2.4 |
| force3 | 75.9 ± 0.8 | 83.6 ± 1.5 | 90.3 ± 2.0 | 93.8 ± 1.4 | 95.8 ± 1.3 | 94.7 ± 0.9 |
| imu | 46.5 ± 1.5 | 64.5 ± 5.5 | 83.2 ± 1.2 | 93.3 ± 2.1 | 88.4 ± 2.7 | 92.4 ± 1.7 |
| force3+imu | 58.8 ± 2.9 | 89.7 ± 1.1 | 93.3 ± 1.2 | 98.0 ± 0.7 | 96.6 ± 1.0 | 96.6 ± 1.7 |
| force3_noFL | 74.6 ± 2.3 | 83.5 ± 1.9 | 88.4 ± 1.4 | 95.0 ± 1.4 | 94.8 ± 0.9 | 95.8 ± 0.9 |
| normal_noFL | 68.4 ± 1.0 | 75.8 ± 1.9 | 84.8 ± 0.9 | 89.3 ± 1.5 | 90.6 ± 2.8 | 94.0 ± 0.8 |

## Leave-one-step-frequency-out: accuracy per held-out frequency (%)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

| input | 0.125 Hz | 0.1875 Hz | 0.25 Hz |
|---|---|---|---|
| normal | 51.6 ± 1.0 | 85.3 ± 1.1 | 78.0 ± 4.1 |
| force3 | 58.3 ± 5.1 | 91.3 ± 0.7 | 89.8 ± 3.4 |
| imu | 57.5 ± 2.0 | 84.0 ± 1.1 | 80.3 ± 2.0 |
| force3+imu | 65.2 ± 2.9 | 95.8 ± 0.9 | 90.3 ± 4.5 |
| force3_noFL | 50.1 ± 6.7 | 91.1 ± 0.7 | 87.2 ± 3.3 |
| normal_noFL | 52.4 ± 2.0 | 84.8 ± 2.0 | 76.1 ± 2.7 |

## Every seed (fold-mean accuracy %, macro-F1 x100)

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

| input | split | seed 0 | seed 1 | seed 2 | seed 3 | seed 4 |
|---|---|---|---|---|---|---|
| normal | step10 | 92.6 / 92.6 | 92.2 / 92.2 | 92.0 / 91.9 | 92.0 / 92.0 | 91.7 / 91.7 |
| force3 | step10 | 94.8 / 94.8 | 93.8 / 93.8 | 94.1 / 94.1 | 94.0 / 94.0 | 94.9 / 94.9 |
| imu | step10 | 97.6 / 97.6 | 97.3 / 97.3 | 97.6 / 97.6 | 97.7 / 97.7 | 98.0 / 98.0 |
| force3+imu | step10 | 98.1 / 98.1 | 98.3 / 98.3 | 98.0 / 98.0 | 98.4 / 98.4 | 98.1 / 98.1 |
| force3_noFL | step10 | 94.3 / 94.3 | 93.8 / 93.8 | 93.8 / 93.8 | 94.3 / 94.3 | 93.9 / 93.8 |
| normal_noFL | step10 | 92.6 / 92.6 | 92.0 / 91.9 | 92.0 / 92.0 | 92.8 / 92.7 | 91.5 / 91.5 |
| normal | trial10 | 88.5 / 88.6 | 88.4 / 88.3 | 89.1 / 89.1 | 88.2 / 88.2 | 89.0 / 88.9 |
| force3 | trial10 | 92.2 / 92.1 | 92.4 / 92.3 | 93.0 / 93.0 | 93.2 / 93.1 | 93.0 / 92.9 |
| imu | trial10 | 93.1 / 93.0 | 90.6 / 90.6 | 92.7 / 92.6 | 92.0 / 92.0 | 93.9 / 93.9 |
| force3+imu | trial10 | 96.0 / 96.0 | 96.7 / 96.6 | 96.6 / 96.5 | 96.8 / 96.8 | 95.7 / 95.6 |
| force3_noFL | trial10 | 92.9 / 92.8 | 92.4 / 92.4 | 93.1 / 93.0 | 93.0 / 93.0 | 92.9 / 92.8 |
| normal_noFL | trial10 | 87.9 / 87.9 | 87.7 / 87.7 | 89.3 / 89.2 | 88.3 / 88.3 | 88.9 / 88.8 |
| normal | loso | 83.2 / 83.1 | 82.4 / 82.2 | 84.0 / 83.9 | 83.5 / 83.5 | 83.9 / 83.6 |
| force3 | loso | 88.5 / 88.5 | 89.7 / 89.5 | 88.6 / 88.5 | 89.0 / 88.9 | 89.2 / 89.1 |
| imu | loso | 79.8 / 79.1 | 77.4 / 76.4 | 77.5 / 76.4 | 77.6 / 76.8 | 78.0 / 77.2 |
| force3+imu | loso | 88.8 / 88.1 | 89.0 / 88.0 | 88.0 / 87.1 | 89.5 / 88.8 | 88.9 / 87.8 |
| force3_noFL | loso | 88.9 / 88.7 | 88.8 / 88.7 | 88.5 / 88.5 | 88.6 / 88.4 | 88.6 / 88.4 |
| normal_noFL | loso | 83.5 / 83.5 | 84.2 / 84.2 | 84.3 / 84.2 | 83.7 / 83.5 | 83.3 / 83.1 |
| normal | lofo | 70.5 / 69.7 | 71.6 / 71.4 | 69.8 / 69.2 | 72.9 / 71.6 | 73.3 / 72.8 |
| force3 | lofo | 79.1 / 78.5 | 80.4 / 80.5 | 81.4 / 80.9 | 81.1 / 81.0 | 76.9 / 76.3 |
| imu | lofo | 73.1 / 71.8 | 73.6 / 72.0 | 73.8 / 72.2 | 73.6 / 72.0 | 75.6 / 74.5 |
| force3+imu | lofo | 84.2 / 83.5 | 84.9 / 84.4 | 81.2 / 79.8 | 83.5 / 83.4 | 84.9 / 84.4 |
| force3_noFL | lofo | 80.3 / 80.1 | 76.8 / 77.0 | 74.0 / 74.2 | 75.7 / 75.3 | 73.8 / 72.8 |
| normal_noFL | lofo | 68.0 / 67.0 | 71.7 / 70.0 | 70.8 / 70.4 | 72.2 / 71.4 | 72.8 / 71.7 |

## Shuffled-label control

*QCAT: quadruped, one 3-axis force vector per foot, real hardware; not a humanoid pressure map.*

trial10, force3, seed 0, training and validation labels permuted, test labels true: accuracy 16.2 % over 10 folds (fold range 9.0-23.3; chance 16.7 %).

Leakage check: for trial10, loso and lofo every fold asserted no (surface, speed, eval_id) trial in both train/val and test (assert_no_leak, run before every fold).

Confusion matrices per fold and seed: qcat_runs.jsonl (`cm`, rows true, cols predicted; classes concrete, grass, gravel, mulch, dirt, sand).
