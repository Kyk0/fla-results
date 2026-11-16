# V3 summary for outside review
Completion: the owner-reduced quick check finished; the original full experiment did not (DECISIONS.md D36, D40; STATUS.md v3).
Archive: adder manager checkout commit b8f0b07154ef5cbed566337eace56c5863ef0afb; REPORT_V3.md does not exist in any inspected checkout.
Question definitions below are DECISIONS.md D26, not the unrelated historical Q1–Q5 in QUESTIONS.md.
Notation: terrain macro-F1; ± population standard deviation over seeds; quick-check seeds 0–2 (D36); real-data accuracy uses five seeds (q5_table.md).
Sources: R = qc/robust_table.md (row, column); J = worker_a/sweep/{condition}/{layout}_s{0,1,2}.json, test.M1.
Derived values and exact layout rows: REVIEW_TABLE.csv and SHEAR_BENEFIT.csv; build_review.py documents averaging and pairing.

Q1: No universal pressure count is established: without shear, seen-gait F1 rises from 0.782 ± 0.003 at four points to 0.856 ± 0.001 at full resolution (R Npool4/Nreal, in-distribution).
Unseen SONIC also improves: 0.223 ± 0.017 → 0.418 ± 0.024 (J logo_walk_sonic, Npool4/Nreal; REVIEW_TABLE.csv).
Changed sensor reverses that ranking: foot mask 0.727 ± 0.007 → 0.084 ± 0.018 (R Npool4/Nreal, g1); therefore the pressure-count conclusion does not hold across sensor models.

Q2: Four block shear vectors help the tested layouts, but the minimum shear count is unknown because one/two-vector comparisons were cut (D36; R).
At four pooled points, seen-gait F1 is 0.782 ± 0.003 without vs 0.821 ± 0.006 with shear (R Npool4/Npool4+Sblk, in-distribution).
Four-point shear benefit holds on unseen SONIC (0.116 ± 0.034), G113 (0.142 ± 0.030), and the changed-sensor mean (0.049 ± 0.005); individual arm significance is not established (SHEAR_BENEFIT.csv Npool4; R).

Q3: Greater shear benefit on SONIC is not supported by the tested held-out results; the complete original gait comparison remains untested (D26 Q3, D40).
Full-map held-out benefits: 0.108 ± 0.021 SONIC vs 0.065 ± 0.048 G113 (SHEAR_BENEFIT.csv Nreal; J logo_* Nreal[+Sblk]).
The second benefit fails the stated real-difference rule (D40); no gait-specific changed-sensor comparison or held-out G80 is available, so neither setting establishes the original hypothesis.

Q4: No layout earns a robust recommendation under the original rule; four-point layouts are insufficient and finer layouts fragile under the explicitly stated reduced-scope eight-arm average (REVIEW_TABLE.csv, D26 Q4).
Four points + shear: seen 0.821 ± 0.006, two-gait mean 0.471 ± 0.019, changed sensor 0.742 ± 0.003 (REVIEW_TABLE.csv Npool4+Sblk).
Full map + shear: seen 0.881 ± 0.002, two-gait mean 0.622 ± 0.023, changed sensor 0.530 ± 0.007 (REVIEW_TABLE.csv Nreal+Sblk).
Unseen-gait and sensor objectives favour different layouts; course metrics and original full recommendation grid were not completed (D26, D36).

Q5: The real-data shear analogue holds on QCAT but not PUTany; neither dataset validates a humanoid pressure layout (q5_table.md, real-data sections).
QCAT unseen speed: three-axis 89.0 ± 0.4% vs normal-only 83.4 ± 0.6%; PUTany: 64.9 ± 2.7% vs 65.8 ± 1.0% (q5_table.md force3/normal rows).
Changed hardware sensor model was not tested; unseen robot gait was not tested (unseen speed is the QCAT proxy); matching simulation comparisons remain pending (q5_table.md).

V2 observation: confirmed for the tested pooled layouts on both unseen gaits, and for the full map on unseen SONIC; full-map unseen G113 is inconclusive (D40; SHEAR_BENEFIT.csv).
Four-point paired benefit: SONIC 0.116 ± 0.034, G113 0.142 ± 0.030 (SHEAR_BENEFIT.csv Npool4).
The original H2 confirmation is NOT established: v2-block replication and the complete held-out-gait mean were cut; D40 calls the pooled result confirmed, whereas D26 explicitly excludes pooled four-point results from the strict H2 verdict.

Missing/wrong: no REPORT_V3.md or existing v3 HTML page; old/pending sections remain in STATUS.md and q5_table.md, alongside completed quick-check results.
STATUS.md final table rounds SONIC four-point no-shear to 0.22 ± 0.02; use recomputed REVIEW_TABLE.csv/J for exact values.
STATUS.md draft robustness mixes nominal sensor results with in-distribution results: four-point no-shear 0.80 vs 0.782 ± 0.003; R separates nominal 0.799 ± 0.002 from in-distribution 0.782 ± 0.003.
No report/table reconciliation is possible for REPORT_V3.md because it is missing; original tables and STATUS.md are retained.
Sensor checks: maximum centre-of-pressure difference 1.57 mm failed the 1 mm limit; small footprints overcount edge load and foot masks omit box-foot edge loads (DECISIONS.md D33; reallike_checks.json).
Viper was used for contact-policy training; both attempts failed the contact-improvement rule (D33, D36; contact_evaluation/ and NOTES_C.md).
Weights remain on the servers; WEIGHTS.txt and WEIGHTS_VIPER.txt list their paths and sizes; this collection contains results and a weight inventory, not checkpoint binaries.
