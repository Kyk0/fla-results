# Robustness of the in-distribution models on the sensitivity sets (B8, D36)

*Simulation: K1 humanoid, sole-only models (pooled pressure per foot, + 4 block shear vectors for +Sblk), trained on data/v2 (randomized sensor), scored without retraining on the sensitivity sets.*

Terrain macro-F1 M1 (walk test windows of the three v2 sources), mean ± std over seeds 0-2. In-distribution = the model's own data/v2 test M1 (main sweep json).
Commits: ['1dc5b56e29d7ba7299eb73433f1a5326f1147b5c clean', 'a029f744ec7a1273943173ea5fe6b09913ad6f50 clean']

| layout | in-distribution | nominal | shifted | pads | g1 | nosat | reallike30 | reallike60 | reallike100 | reallike60_g1 |
|---|---|---|---|---|---|---|---|---|---|---|
| Npool4 | 0.782 ± 0.003 | 0.799 ± 0.002 | 0.782 ± 0.002 | 0.560 ± 0.009 | 0.727 ± 0.007 | 0.696 ± 0.004 | 0.571 ± 0.008 | 0.718 ± 0.004 | 0.791 ± 0.001 | 0.698 ± 0.009 |
| Npool4+Sblk | 0.821 ± 0.006 | 0.829 ± 0.006 | 0.822 ± 0.006 | 0.630 ± 0.025 | 0.745 ± 0.002 | 0.764 ± 0.005 | 0.631 ± 0.008 | 0.789 ± 0.004 | 0.822 ± 0.006 | 0.732 ± 0.011 |
| Npool8 | 0.817 ± 0.001 | 0.838 ± 0.004 | 0.817 ± 0.006 | 0.338 ± 0.014 | 0.399 ± 0.004 | 0.750 ± 0.005 | 0.582 ± 0.020 | 0.748 ± 0.008 | 0.828 ± 0.003 | 0.471 ± 0.005 |
| Npool8+Sblk | 0.851 ± 0.003 | 0.862 ± 0.003 | 0.855 ± 0.001 | 0.484 ± 0.013 | 0.466 ± 0.009 | 0.825 ± 0.004 | 0.638 ± 0.019 | 0.816 ± 0.003 | 0.856 ± 0.004 | 0.551 ± 0.008 |
| Npool18 | 0.839 ± 0.003 | 0.851 ± 0.004 | 0.838 ± 0.003 | 0.303 ± 0.005 | 0.321 ± 0.006 | 0.813 ± 0.010 | 0.520 ± 0.020 | 0.692 ± 0.025 | 0.814 ± 0.012 | 0.304 ± 0.004 |
| Npool18+Sblk | 0.866 ± 0.001 | 0.878 ± 0.005 | 0.870 ± 0.004 | 0.417 ± 0.024 | 0.347 ± 0.030 | 0.854 ± 0.001 | 0.591 ± 0.038 | 0.781 ± 0.027 | 0.857 ± 0.004 | 0.338 ± 0.025 |
| Nreal | 0.856 ± 0.001 | 0.868 ± 0.003 | 0.843 ± 0.003 | 0.189 ± 0.021 | 0.084 ± 0.018 | 0.753 ± 0.015 | 0.504 ± 0.028 | 0.624 ± 0.030 | 0.746 ± 0.009 | 0.087 ± 0.015 |
| Nreal+Sblk | 0.881 ± 0.002 | 0.889 ± 0.004 | 0.870 ± 0.001 | 0.231 ± 0.021 | 0.098 ± 0.013 | 0.815 ± 0.018 | 0.579 ± 0.015 | 0.738 ± 0.012 | 0.811 ± 0.012 | 0.101 ± 0.013 |

M2 (support macro-F1) and M2_partial per model and arm: robust.jsonl.

Pending arms (no cache yet): none
