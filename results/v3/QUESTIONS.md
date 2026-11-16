# QUESTIONS

Things Kyrylo (or the consultant chat) should answer. None of them blocked the run; the default taken is written next to each.

## Q1. Should the gate be re-stated before real data is collected?
G1 came out 0 of 3 (REPORT.md section 1). Two of the three criteria turned out to have little room in this setup: proprioception alone already separates grip from slip at 0.948 F1, and the surface-change criterion cannot resolve less than one step (every run's median is exactly 2 steps). I kept the criteria and thresholds as written. **Default taken:** verdict reported as it is. **Question:** for the real-sole phase, do you want the gate re-stated around partial-support detection, slip onset, and transfer to an unseen gait (REPORT.md section 10)? That is a judgment call for you and the consultant, not for me after seeing the result.

## Q2. Which controller will run on the real K1 during data collection?
Models trained on two gaits and tested on a third lose 30 points of terrain F1 or collapse completely (SONIC: 0.07–0.11). The real training set must contain the controller that will actually be deployed. **Default taken:** all three sim gaits are in v1 training. **Question:** which controller(s), and can you record with more than one?

## Q3. Is G113 m2200 the right "deployed" velocity policy?
Worker B found it as the latest policy in `adder:/data/kkolesni/K1/k1_deploy/policies/B_G113_m2200_soft.pt`, with G80 m4200 as a fallback, and SONIC-K1 `release_onnx_it50000` on viper. **Default taken:** those three. Tell me if a newer one should replace them.

## Q4. Friction between 0.36 and 0.7 was not sampled
The brief defines hard-slip and hard-grip as classes, and the terrain suite left a gap between them. In that range the foot slides less often and shear might matter more, or nothing might be observable at all. **Default taken:** not added after seeing the result (it would be changing the test). **Question:** add it as a pre-registered v2?

## Q5. Is a compliant-sole simulation worth building?
In a rigid-body solver the split of force between zones is a numerical artifact and there is no partial slip in the contact patch, which is what a real shear sensor picks up. My judgment is that further rigid-body sim cannot answer the shear question either way. **Default taken:** none; this is a scope decision (days of work, not hours).

## Q6. Real PX-FOOTRIX details for `fla_terrain/real/convert.py`
The converter is a stub: grid size, taxel pitch, axis signs, left/right mirroring, units and noise level are placeholders. Please send the actual sole geometry and a sample recording when you have one. The sim sensor noise (0.15 N shear, 0.25 N normal) is also a placeholder.

## Q7. Housekeeping on the servers
- A deputy-manager watchdog is running on viper (`/data/kkolesni/fla-terrain/agents/watchdog.sh`, PID in `agents/watchdog.pid`). It only acts if the Mac goes silent for 45 minutes. The manager stops it when the run is closed; if you see it still running, `touch /data/kkolesni/fla-terrain/agents/STOP_DEPUTY`.
- Two conda envs were created on viper: `env_fla` (used by everything) and `env_fla_walk` (created by the first Worker B, unused; safe to delete). Nothing in `env_isaaclab` or the IsaacLab checkout was touched.
- adder was only read from (K1 policies and assets were copied to `viper:/data/kkolesni/fla-terrain/b_ext/`). No jobs were run there.

# Questions from run v2

## Q8. Rectangular point mask instead of the foot-shaped one
The brief asks for a foot-shaped mask of about 100 points. The simulated foot is a rigid box and touches the ground at its corners, where a foot-shaped mask has no points, so the centre of pressure cannot be reproduced there. **Default taken:** 19 x 8 points at 10 mm on the box (152 per foot); the foot shape from your screenshot is a variant in the sensitivity test and its outline is drawn in the renders. **Question:** is that acceptable, or do you want the contact geometry itself changed to the real foot outline (which means the walking policies see a different foot)?

## Q9. The middle of the K1 foot
You described three parts with a middle that does not touch. The foot mesh in the assets shows a 16 mm long groove (4-15 mm deep) just in front of the heel rather than a middle third. **Default taken:** thirds, as in the brief, with per-episode randomization of the boundaries that also covers the mesh value. Which is closer to the real sole?

## Q10. `hard-mid` (friction 0.36-0.7) is test-only
The brief calls it an extra set evaluated for friction regression and class assignment. **Default taken:** it is not in training or validation at all, so it measures how the friction estimate behaves in a range the models never saw. Say so if you wanted it in training.

## Q11. Per-point shear cannot be tested in this simulator
The rigid solver's split of force between contact blocks is not trustworthy while walking (D13), so the map is rebuilt from the foot's total force, centre of pressure and twist. Per-point shear is then that total shear shared out by pressure, with no independent content. The comparison "per-point shear versus block shear" (question 3) will be run and labelled, but it cannot say what the real sensor's per-point shear is worth. Only real recordings or a simulator with a deformable sole can.


## Q12. Per-point force range of the real sole
The simulated foot is a rigid box, so at heel strike and toe-off two to four corner points carry most of the load, far above the 60 N per point (30 N shear) limit the sensor model uses as a placeholder. About a third of the loaded walking samples are clipped and the recorded foot force is then well below the true one (D19). **Default taken:** keep 60 N, and add a "no saturation" arm to the sensitivity test so the report says whether any conclusion depends on it. **Question:** what is the per-point range of the PaXini sole, and does the real map show single points pinned at their maximum during walking?

# Questions from run v3

## Q13. Is SONIC really the heel-to-toe gait on the K1?
Q3 asks whether shear helps more on a heel-to-toe gait (SONIC) than on flat-footed velocity policies. In our simulation (rigid box foot, K1), SONIC touches down flatter than the velocity policies (foot pitch at touchdown 9.6 degrees vs 14-17), with a third of their impact, and spends the same share of stance with its centre of pressure in the back third (0.28 vs 0.27-0.30). The most heel-first gait here is the v2 policy run4 m1000 (21.7 degrees, 0.43). **Default taken:** Q3 is run as pre-registered (SONIC against G113 and G80), the per-gait result is also shown for run4 m1000, and the report states what distinguishes the gaits in simulation (D29). **Question:** on the real robot, does SONIC roll heel-to-toe? If you have a video or foot-pitch log of it, that would settle whether the simulated SONIC gait is representative.
