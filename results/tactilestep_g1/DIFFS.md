# TactileStep re-implementation: what differs from the paper (arXiv 2609.28959)

Built on the Hiking-in-the-Wild G1 parkour task; Hiking rewards/terrain/AMP unchanged. New code:
`mdp/tactile.py`, `config/g1/tactilestep_cfg.py`, `scripts/instinct_rl/train_tactile.py`, `scripts/play_tactile.py`.

Same as paper: 60 taxels/foot (12x5 grid on the shoe sole), raycast along the sole normal, eq. 3 weights with
tau=(gmax-gmin)/ln50, force from the foot's contact force projected on the sole normal, kNN diffusion, F/A/CoP features,
CoP normalised by the foot outline extents and zeroed below 0.05 BW, 2-frame actor history (16 dims), critic adds foot vz
+ phase one-hot, Algorithm 1 phases, all Table 5/6 tactile weights and thresholds (incl. 40000 N/s, 0.038 m, 0.01 m),
tactile noise of Table 10 (±10 % per taxel, episode XY offset 1.5 mm clip 5 mm, 8 % one-frame delay), dual critic with
advantage mixing [1.1, 0.9] (instinct_rl multi-reward), AMP coef 0.25, foot slide -0.4.

Differs:
- Warm start from the released Hiking ONNX actor (plain MLP 512-256-128) instead of from scratch with MoE 256-128-64;
  tactile input columns zero-initialised; 100-iteration critic warm-up with the actor frozen; lr 3e-4; init std 0.3;
  tactile warm-up ramp 200 iterations (paper 5000). Paper: 50 000 iterations; here a few hundred to ~1000.
- Reward grouping: all existing Hiking terms stay in critic 1 (dense) + new dense tactile terms; only the new
  pre-landing and landing-event terms go to critic 2 (paper also moves dont_wait, air time, slide, limits... to sparse).
- Terrain normal per taxel from the hit-point grid (finite differences); Isaac's ray caster gives no normals.
- Not given in the paper, chosen: eta_n 0.5, beta 2, alpha 0.3, k 4, eps_f 1 N, contact F>0.05 BW or A>0.15,
  h_pre 0.08 m, landing window 5 steps (0.1 s); "concentrated load" = share of force on the most loaded taxel.
- CoP margin uses the shoe-sole rectangle (x -0.054..0.132, y ±0.036 m), so max margin is 36 mm.
