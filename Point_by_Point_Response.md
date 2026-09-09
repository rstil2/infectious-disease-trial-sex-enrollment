Submission ID: 10975380-4561-4e88-b54d-6692abdfe004
Journal: Trials
Manuscript: Female enrollment versus target-population sex composition in pivotal infectious disease trials: a reconstructed Bayesian analysis of phase III/IV randomised trials

Dear Dr Watson and Reviewer,

Thank you for the review. We treated the comments as a requirement to rebuild trial selection, extraction, the estimand, and the model. The previous 15-study table, the 72% (68–76%) systemic-variance claim, the 2068–2074 parity projections, and the 2,847-record funnel are withdrawn. The revised manuscript uses counts taken from primary publications, a trial-specific expected-share comparator, and a hierarchical model that reports residual variance.

A reproducibility package (extraction table, screening log, code, posterior draws, figures) is Additional File 1.

---

Editor

Comment: Please ensure the results are accurately reported, any overstated conclusions are rewritten and the limitations of the work fully explained.

Response: We agree. Female percentages now match the cited tables (e.g. BNT162b2 49.4% not 34%; VOICE 100% not 35%). Conclusions no longer attribute 72% of variance to systemic barriers or forecast parity in 2068–2074. Limitations state that disease-versus-residual variance is not identified and that the sample is a reconstructed pivotal-trial set, not a registry census.

---

Reviewer

Major comment 1. The Methods specify phase III/IV randomized human trials, but the Ebola sample includes phase I studies and the Qiu et al. ZMapp nonhuman-primate experiment. The HIV sample includes the observational PARTNER study and a phase II trial. These studies do not meet the stated criteria. A reproducible search strategy, screening flowchart, reasons for exclusion, and verified study-characteristics table are required.

Response: We agree. We re-applied the stated criteria to the original 15 named studies.

Excluded as ineligible:
- Tapia et al., Lancet Infect Dis 2016 — phase 1 ChAd3-EBO-Z [manuscript ref 11]
- Milligan et al., JAMA 2016 — phase 1 Ad26/MVA [12]
- Qiu et al., Nature 2014 — nonhuman-primate ZMapp experiment [13]
- Rodger et al., JAMA 2016 (PARTNER) — observational cohort [14]
- Peterson et al., PLoS Clin Trials 2007 — phase 2 [15]

Human ZMapp/therapeutic data are taken from PALM (Mulangu et al., NEJM 2019; phase II/III; n=673; 55.6% female), not from Qiu et al.

We added three pivotal mixed-sex phase III trials with extractable Table 1 sex counts: ENSEMBLE, NVX-CoV2373 UK, and Partners PrEP.

Supplementary Table S1 is the study-by-study decision log. Supplementary Figure S1 is the reconstruction flowchart. Table 1 and Supplementary Table S2 give verified characteristics, n, female n, source table, NCT/registry ID, and DOI.

We do not reuse the previous 2,847 / 67-trial funnel. That funnel cannot be reproduced from a trial-level log with real registry identifiers. The Methods now state that this is a reconstructed pivotal-trial sample.

---

Major comment 2. VOICE and FEM-PrEP enrolled women, whereas iPrEx enrolled men and transgender women who have sex with men. Their enrollment composition largely reflects the intended study population rather than a common recruitment bias. Applying an unconditional 50% benchmark across these studies is therefore not appropriate. The comparator should reflect each trial’s target population, disease epidemiology, intervention indication, and eligibility criteria.

Response: We agree. VOICE (5,029 women) and FEM-PrEP (2,120 women) are women-only by design. iPrEx required male sex at birth. They are a secondary, sex-restricted set. The primary estimand is observed female share divided by a trial-specific expected share (general adult COVID-19 vaccines 0.50; ChAdOx1 health-care workers 0.70; rVSV-ZEBOV enumerated contacts 0.43; Partners PrEP HIV-negative partners 0.38; Bangkok PWID 0.20; and so on). Results are enrollment ratios, not distance from 50%.

---

Major comment 3. The model is highly parameterized for only 15 heterogeneous trial-level observations, and disease is strongly confounded with calendar time. The Methods define time per decade, whereas the Results interpret the coefficient per year. In addition, the reported global and disease variances sum exactly to total variance, leaving no residual variance despite inclusion of a trial-level random effect. The authors should clarify the observational unit, identifiability constraints, coefficient units, and calculation of every variance component.

Response: We agree. The observational unit is the trial. The primary model has no time term, because COVID-19, Ebola, and HIV occupy disjoint eras. Coefficient α is a log-odds deviation from the trial-specific expected share, not a per-year or per-decade slope. Between-trial variance is split into disease-level σδ² and residual τ²; both are reported with 95% credible intervals. Residual variance is no longer omitted. With 10 mixed-sex trials and three diseases, the disease proportion of variance has 95% CrI 0.0004–0.89 and is not identified. We do not report a 72%/28% split.

---

Major comment 4. The repository is still listed as “[URL to be added],” and the trial-level dataset, extraction forms, model code and sensitivity analyses are unavailable. These materials are necessary during peer review, particularly because several reported values cannot be reconciled with the cited sources.

Response: We agree. Additional File 1 contains:
- data/verified_trials.csv (n, female n, expected share, DOI, extraction note)
- data/screening_log.csv
- src/analysis.py (seed 42)
- results/trial_level_estimates.csv and posterior_draws.csv
- figures

Every primary-set percentage in the revised paper can be recomputed from those files and the cited tables. Examples of previous irreconcilable values and the corrected sources are in the response to comment 1.

---

We hope this reconstruction addresses every point. We are grateful for a review that made the ineligible studies and the wrong estimand explicit.
