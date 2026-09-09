# Scoring sex representativeness against the wrong denominator: target-population analysis of pivotal infectious disease trials

**Running title:** Target-population scoring of trial sex composition

**Article type:** Research

**Corresponding author:**
R. Craig Stillwell, Ph.D.
Independent Researcher
Email: craig.stillwell@gmail.com
Phone: 270-491-0493

---

## Abstract

**Background:** Female enrollment in infectious disease trials is routinely scored against 50%. That denominator treats a women-only pre-exposure prophylaxis (PrEP) trial, a PrEP trial restricted to men who have sex with men (MSM), a trial of people who inject drugs (PWID), and a health-care-worker vaccine trial as if they shared one recruitment failure. The scientifically relevant question is whether enrollment matches the sex mix implied by indication, eligibility, and the people the protocol actually set out to enroll.

**Methods:** We assembled a verified set of pivotal phase II/III or III randomised human trials of COVID-19, Ebola, or HIV with extractable sex-stratified counts. Sex-restricted trials were scored against their design (expected share 0 or 1). Mixed-sex trials were scored with an enrollment ratio: observed female proportion divided by a trial-specific expected share. A Bayesian random-effects model estimated the mean log-odds deviation from that expected share and reported residual and disease-level variance components separately. Calendar time was omitted because disease is aliased with era.

**Results:** Ten mixed-sex pivotal trials (N=150,907) had a median enrollment ratio of 0.98 (range 0.75–1.11). HIV couple and PWID trials sat on their epidemiologic comparators (ratios 0.99–1.01). Adult COVID-19 vaccine trials were 45.0–49.4% female versus 50% expected. The two Ebola trials diverged by protocol, not by pathogen: PALM enrolled 55.6% women and included pregnant patients, whereas rVSV-ZEBOV ring vaccination enrolled 32% women among vaccinees against 43% among enumerated contacts after excluding pregnancy and breastfeeding. Posterior mean log-odds deviation from the target-population expected share was −0.11 (95% credible interval [CrI] −0.34 to 0.17). Forcing every mixed-sex trial onto a 50% benchmark produced a more negative mean and recreated the appearance of a shared deficit. Disease-level and residual variance could not be separately identified (disease proportion of variance, 95% CrI 0.0004–0.89).

**Conclusions:** In this set, sex composition is mostly a design feature. The 50% score mislabels successful indication-matched enrollment as underrepresentation and hides the protocol choice that still moves the ratio: default exclusion of pregnancy in prevention trials. PALM shows that inclusion of pregnant patients is feasible in an outbreak therapeutic trial. Trial reports should publish enrollment against a stated target population, not against a universal 50% line.

**Keywords:** clinical trials; sex; enrollment; eligibility criteria; infectious diseases; Bayesian random-effects; pregnancy exclusion

---

## Background

Whether a trial can support inference in women depends on who was enrolled, not on a single percentage [1–3]. Large registry analyses already show that a fairer comparator is the sex mix of the intended-use population, not an unconditional 50% line [4]. Infectious disease prevention trials make the same point sharper: a woman-only PrEP trial, a PrEP trial restricted to MSM, a trial of PWID, and a health-care-worker vaccine trial have each already specified a target sex mix by design. Scoring them against 50% converts that design into apparent bias.

The same scoring error also hides an eligibility rule that still changes mixed-sex enrollment: default exclusion of pregnant and breastfeeding people, which remains the norm in US drug trials [5–7]. Two Ebola virus disease (EVD) protocols in the same outbreak lineage supply a natural contrast. PALM (Pamoja Tulinde Maisha, Swahili for "together save lives") enrolled unselected inpatients with EVD, including pregnant women [8]. The rVSV-ZEBOV ring-vaccination trial, built on a recombinant vesicular stomatitis virus–based Ebola vaccine, excluded pregnancy and breastfeeding from eligibility [9]. The draft ICH E21 guideline, now in public consultation, asks sponsors to stop treating that exclusion as the automatic default [10]. If a target-population score is the right estimand, that eligibility choice is the protocol lever it should detect.

The practical question for trial methodologists is therefore not "how far is this trial from 50%?" but "did this trial enroll the sex mix its indication and eligibility implied?" We answer that question for a reconstructed set of pivotal infectious disease randomised trials.

## Methods

### Reconstruction of the eligible set

We started from a named list of 15 frequently cited COVID-19, Ebola, and HIV studies and re-applied explicit eligibility: (1) pivotal phase II/III or phase III randomised trial; (2) human participants; (3) sex-stratified enrollment extractable from the primary publication or ClinicalTrials.gov results tables; (4) COVID-19, Ebola, or HIV indication. We excluded phase I/II immunogenicity studies, observational cohorts, and nonhuman-primate experiments. Sex-restricted trials (women-only or MSM/transgender-women indications) were eligible for a secondary analysis but not for the mixed-sex primary estimand.

We added three pivotal mixed-sex phase III trials that met the same rules and had extractable Table 1 sex counts: Ad26.COV2.S ENSEMBLE [11], NVX-CoV2373 United Kingdom [12], and Partners PrEP [13]. Supplementary Table S1 is the trial-level reconstruction log with registry identifiers, and Supplementary Figure S1 records inclusion and exclusion in a PRISMA-style flow [14]. This is a protocol-specified sample of pivotal trials, not a multi-registry census; we do not claim a 2,847-record search.

### Data extraction

For each included trial we recorded registry identifier, phase, design, analysis population as labelled in the source table, n, female n, pregnancy-related eligibility, and citation. Counts were taken from the table that the paper used for baseline characteristics (safety population, per-protocol efficacy population, or randomised set, as reported). A single extractor (R.C.S.) recorded values; each count in Supplementary Table S2 is tied to a page-level source note and a public registry number.

### Expected female share

The comparator was defined before modelling, trial by trial:

- General adult COVID-19 vaccine trials: 0.50.
- ChAdOx1 nCoV-19: 0.70, because enrollment targeted health-care workers and women comprise approximately 70% of the global health and care workforce [15].
- rVSV-ZEBOV ring vaccination: 0.43, the female share among enumerated contacts [9].
- PALM: 0.50 (unselected EVD inpatients).
- HPTN 052 index partners: 0.50 (either sex eligible).
- Partners PrEP HIV-uninfected partners: 0.38, matching the documented 62% male share among HIV-negative partners in that heterosexual serodiscordant-couple design [13].
- Bangkok Tenofovir Study: 0.20, matching the approximately 80% male composition of the enrolled PWID population [16].
- VOICE and FEM-PrEP: 1.00 (women-only).
- iPrEx: 0 for cisgender women (male sex at birth required) [17].

Enrollment ratio = observed female proportion / expected share. A ratio of 1.0 means the trial matched its target-population comparator.

### Statistical analysis

Wilson 95% confidence intervals were computed for each observed proportion. The primary Bayesian model used trial-level log-odds deviations, θ̂ᵢ = logit(pᵢ) − logit(πᵢ), with known sampling variance sᵢ² = 1 / [nᵢ · pᵢ · (1 − pᵢ)]. The random-effects model was:

θ̂ᵢ ~ Normal(α + δ_d(i), sᵢ² + τ²), with δ_d ~ Normal(0, σδ²),

where *i* indexes trials and *d(i)* is the disease of trial *i*.

Priors: α ~ Normal(0, 1); τ and σδ ~ Half-Normal(0, 0.5). The observational unit is the trial. α is the mean log-odds deviation from the trial-specific expected share, reported as a posterior mean with a 95% credible interval. τ² is residual between-trial variance; σδ² is disease-level variance. Their sum is the between-trial variance of the linear predictor; binomial sampling variance is already contained in sᵢ² and is not part of that sum. Posterior samples used componentwise Metropolis–Hastings sampling (20,000 iterations; 5,000 discarded as burn-in; seed 42). Acceptance rates for the four parameter blocks (α, δ, τ, σδ) ranged from 58% to 93%; full posterior draws are in Additional File 1.

Time (in years or decades) was not included in the primary model. COVID-19 trials are all from 2020, Ebola trials from 2015–2019, and HIV trials from 2008–2011; a global time slope is not separately identified from disease in this sample.

Sensitivity analyses: (i) replace every mixed-sex expected share with 0.50, the conventional audit statistic; (ii) drop the health-care-worker trial; (iii) drop rVSV-ZEBOV. We do not extrapolate enrollment to future calendar years, because disease and era are aliased and a global time slope is not identified.

Analyses used Python 3.9+ (NumPy, SciPy, pandas). Code, extraction tables, and posterior draws are at https://github.com/rstil2/infectious-disease-trial-sex-enrollment and in Additional File 1.

### Terminology and reporting

Trial reports recorded sex as female or male; we use *sex* for these categories throughout. This observational analysis of published trial reports follows STROBE guidance [18] (Supplementary File S3).

## Results

### Reconstruction

Of 15 originally named studies, five were ineligible: Tapia et al. (ChAd3-EBO-Z) and Milligan et al. (Ad26/MVA) are phase 1 [19,20]; Qiu et al. is a nonhuman-primate ZMapp experiment [21]; PARTNER is observational [22]; Peterson et al. is labelled phase 2 in the source paper [23]. Three trials were sex-restricted: VOICE, 5,029 women [24]; FEM-PrEP, 2,120 women [25]; iPrEx, 2,499 MSM and transgender women, of whom 29 participants (1.2%) identified as women [17]. Seven original mixed-sex trials were retained after count correction, and three mixed-sex phase III trials were added. The primary set is 10 trials (N=150,907). Supplementary Figure S1 shows the reconstruction flow, and corrected source counts are in Table 1 and Supplementary Table S2.

### Mixed-sex enrollment versus expected share

Table 1 and Figure 1 show observed versus expected shares. Median enrollment ratio was 0.98 (range 0.75–1.11). Once each trial is scored against its own target, the set does not describe a shared recruitment failure.

The HIV mixed-sex trials illustrate the point. Bangkok Tenofovir enrolled 20.2% women, which looks like a large deficit against 50% but matches the approximately 80% male PWID population the protocol enrolled (ratio 1.01) [16]. Partners PrEP enrolled 37.6% HIV-negative female partners versus 38% expected (ratio 0.99) [13]. HPTN 052 enrolled 49.5% female index partners versus 50% (ratio 0.99) [26]. A 50% audit line would have classified two of these three trials as underrepresentation.

COVID-19 general-adult vaccine trials ranged from 45.0% (Ad26.COV2.S) to 49.4% (BNT162b2) against 50% expected, modest shortfalls of 0.6 to 5.0 percentage points [11,12,27,28]. ChAdOx1 nCoV-19 enrolled 60.5% women in a health-care-worker-enriched sample, below a 70% workforce comparator but far above 50% [15,29].

The two Ebola trials diverged by protocol, not by pathogen. PALM enrolled 55.6% women (ratio 1.11) and reported that 6.1% of female participants were pregnant at EVD diagnosis [8]. rVSV-ZEBOV immediately vaccinated contacts were 32% women versus 43% among enumerated contacts (ratio 0.75) [9]; eligibility excluded pregnant and breastfeeding individuals. That 11-percentage-point gap relative to the ring is the largest shortfall in the primary set.

### Bayesian summary and the 50% sensitivity

The posterior mean of α was −0.11 (95% CrI −0.34 to 0.17), compatible with no mean deviation from the trial-specific expected share. Posterior mean residual SD τ was 0.23 (95% CrI 0.13–0.40), and posterior mean disease-level SD σδ was 0.15 (95% CrI 0.005–0.61). The residual share of between-trial variance had 95% CrI 0.11–1.00, so a 72%/28% systemic-versus-disease split is not identified in this sample. Inverse-variance pooling, which is dominated by the largest COVID-19 trials, gave a mean log-odds deviation of −0.12 (SE 0.044). After dropping rVSV-ZEBOV, \(\alpha\) was −0.01 (95% CrI −0.26 to 0.29).

Replacing every mixed-sex expected share with 0.50 produced a more negative mean (α −0.33, 95% CrI −1.09 to 0.22). That sensitivity analysis is itself a methods result: the conventional 50% statistic, not a shared recruitment process, generates the appearance of large "systemic" underrepresentation.

### Sex-restricted trials

VOICE and FEM-PrEP enrolled only women, as designed [24,25]. iPrEx excluded cisgender women by eligibility [17]. Comparing these trials with 50% is not a valid estimand; against their design, they match.

### Protocol features

Pregnancy exclusion at entry was present in the COVID-19 vaccine trials and in rVSV-ZEBOV, and women in Partners PrEP were not pregnant at enrollment [13]. PALM did not exclude pregnancy [8]. These features are descriptive; they were not entered as covariates in the hierarchical model.

## Discussion

For pivotal infectious disease trials, the result that matters is not a new global percentage. It is that the usual 50% audit statistic is the wrong instrument for indication- and eligibility-restricted protocols. Scored against the sex mix their protocols implied, the mixed-sex pivotal trials in this set have a median enrollment ratio of 0.98. Scored against 50%, Bangkok Tenofovir, Partners PrEP, and ChAdOx1 look like failures when they are indication-matched, occupationally skewed, or both. That is a methods error with a practical cost: it manufactures the appearance of a uniform enrollment crisis and hides the eligibility rule that still moves the ratio.

The remaining, interpretable contrast is protocol, not pathogen. PALM enrolled a female majority and included pregnant patients with EVD [8]. rVSV-ZEBOV excluded pregnancy and breastfeeding and enrolled 32% women among vaccinees against 43% among enumerated contacts [9]. Those two designs sit in the same outbreak lineage and on opposite sides of the pregnancy-exclusion default that still dominates US drug trials [5–7]. *Trials* has already argued that fair inclusion of pregnant women is a scientific and ethical design problem, not an afterthought [5]. The draft ICH E21 guideline now asks sponsors to treat inclusion as the starting point rather than the exception [10]. PALM shows that inclusion is feasible in an outbreak therapeutic trial; rVSV-ZEBOV illustrates the enrollment gap associated with the default exclusion in a prevention protocol. We do not claim that pregnancy exclusion is the sole cause of the rVSV-ZEBOV gap — ring composition, consent, and operational constraints also differ between the two trials — but it is the eligibility feature that distinguishes the two protocols and that trialists can change.

Adult COVID-19 vaccine trials still sit 0.6 to 5.0 percentage points below 50%. That modest gap is real and should not be papered over. It is not evidence of a disease-specific Ebola or HIV recruitment failure, and it is much smaller than the deficit a 50% score invents for PWID, couple, and health-care-worker protocols.

A hierarchical split of "systemic" versus "disease-specific" barriers is not identified with ten mixed-sex trials and three diseases aliased with calendar era. We report that uncertainty rather than a point estimate, and we do not extrapolate parity years.

### Limitations

The sample is a reconstructed pivotal-trial set, not a comprehensive registry census. Expected shares depend on documented design features; the 0.70 health-care-worker comparator is a published workforce average, not the exact occupational mix at ChAdOx1 sites. Extraction was performed by one reviewer (R.C.S.). PALM is phase II/III rather than phase III. Geographic site-level sex mix was rarely published and is unmodelled. The Bayesian variance split has wide credible intervals and should not be used for policy ranking of "systemic" versus "disease-specific" causes.

## Conclusions

In ten mixed-sex pivotal infectious disease trials, female enrollment generally matched the sex mix implied by indication and eligibility. The 50% score mislabels that match as underrepresentation. The protocol contrast that remains is pregnancy exclusion versus inclusion: rVSV-ZEBOV versus PALM. Trial reports should publish an enrollment ratio against a stated target population. Sponsors writing protocols now can treat the draft ICH E21 inclusion standard as the design choice that this estimand is built to detect.

## Declarations

**Ethics approval and consent to participate:** Not applicable. This study used published aggregate trial reports. No individual participant data were accessed.

**Consent for publication:** Not applicable.

**Availability of data and materials:** Extraction tables, screening log, analysis code, and posterior draws are at https://github.com/rstil2/infectious-disease-trial-sex-enrollment (MIT license) and in Additional File 1. All source counts are from the cited publications and ClinicalTrials.gov.

**Competing interests:** The author declares no competing interests.

**Funding:** None.

**Authors' contributions:** R.C.S. designed the reconstruction, extracted data, wrote the code, fitted the models, and wrote the manuscript.

**Acknowledgements:** The author thanks the original trial participants and investigators who reported sex-stratified enrollment.

---

## References

1. Clayton JA, Tannenbaum C. Reporting sex, gender, or both in clinical research? JAMA. 2016;316:1863–1864. doi:10.1001/jama.2016.16405.

2. Feldman S, Ammar W, Lo K, Trepman E, van Zuylen L, Etzioni O. Quantifying sex bias in clinical studies at scale with automated data extraction. JAMA Netw Open. 2019;2:e196700. doi:10.1001/jamanetworkopen.2019.6700.

3. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32. doi:10.1186/s13293-020-00308-5.

4. Steinberg JR, Turner BE, Weeks BT, Magnani CJ, Wong BO, Rodriguez F, et al. Analysis of female enrollment and participant sex by burden of disease in US clinical trials between 2000 and 2020. JAMA Netw Open. 2021;4:e2113749. doi:10.1001/jamanetworkopen.2021.13749.

5. van der Graaf R, van der Zande ISE, den Ruijter HM, Oudijk MA, van Delden JJM, Oude Rengerink K, et al. Fair inclusion of pregnant women in clinical trials: an integrated scientific and ethical approach. Trials. 2018;19:78. doi:10.1186/s13063-017-2402-9.

6. Sewell CA, Sheehan SM, Gill MS, Henry LM, Bucci-Rechtweg C, Gyamfi-Bannerman C, et al. Scientific, ethical, and legal considerations for the inclusion of pregnant people in clinical trials. Am J Obstet Gynecol. 2022;227:805–811. doi:10.1016/j.ajog.2022.07.037.

7. Bilinski A, Emanuel N. Fewer than 1% of United States clinical drug trials enroll pregnant participants. Am J Obstet Gynecol. 2025;232:e136–e139. doi:10.1016/j.ajog.2024.12.028.

8. Mulangu S, Dodd LE, Davey RT Jr, Tshiani Mbaya O, Proschan M, Mukadi D, et al. A randomized, controlled trial of Ebola virus disease therapeutics. N Engl J Med. 2019;381:2293–2303. doi:10.1056/NEJMoa1910993.

9. Henao-Restrepo AM, Camacho A, Longini IM, Watson CH, Edmunds WJ, Egger M, et al. Efficacy and effectiveness of an rVSV-vectored vaccine in preventing Ebola virus disease: final results from the Guinea ring vaccination, open-label, cluster-randomised trial (Ebola Ça Suffit!). Lancet. 2017;389:505–518. doi:10.1016/S0140-6736(16)32621-6.

10. International Council for Harmonisation of Technical Requirements for Pharmaceuticals for Human Use. ICH E21 guideline: inclusion of pregnant and breastfeeding individuals in clinical trials. Draft version, Step 2b, endorsed 14 May 2025. https://www.ema.europa.eu/en/documents/other/ich-e21-guideline-inclusion-pregnant-breastfeeding-individuals-clinical-trials_en.pdf. US Food and Drug Administration. E21 Inclusion of Pregnant and Breastfeeding Women in Clinical Trials; International Council for Harmonisation; Draft Guidance for Industry; Availability. 90 FR 34279 (21 July 2025).

11. Sadoff J, Gray G, Vandebosch A, Cárdenas V, Shukarev G, Grinsztejn B, et al. Safety and efficacy of single-dose Ad26.COV2.S vaccine against Covid-19. N Engl J Med. 2021;384:2187–2201. doi:10.1056/NEJMoa2101544.

12. Heath PT, Galiza EP, Baxter DN, Boffito M, Browne D, Burns F, et al. Safety and efficacy of NVX-CoV2373 Covid-19 vaccine. N Engl J Med. 2021;385:1172–1183. doi:10.1056/NEJMoa2107659.

13. Baeten JM, Donnell D, Ndase P, Mugo NR, Campbell JD, Wangisi J, et al. Antiretroviral prophylaxis for HIV prevention in heterosexual men and women. N Engl J Med. 2012;367:399–410. doi:10.1056/NEJMoa1108524.

14. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.

15. World Health Organization. Closing the leadership gap: gender equity and leadership in the global health and care workforce. Geneva: WHO; 2021. https://www.who.int/publications/i/item/9789240025905.

16. Choopanya K, Martin M, Suntharasamai P, Sangkum U, Mock PA, Leethochawalit M, et al. Antiretroviral prophylaxis for HIV infection in injecting drug users in Bangkok, Thailand (the Bangkok Tenofovir Study): a randomised, double-blind, placebo-controlled phase 3 trial. Lancet. 2013;381:2083–2090. doi:10.1016/S0140-6736(13)61127-7.

17. Grant RM, Lama JR, Anderson PL, McMahan V, Liu AY, Vargas L, et al. Preexposure chemoprophylaxis for HIV prevention in men who have sex with men. N Engl J Med. 2010;363:2587–2599. doi:10.1056/NEJMoa1011205.

18. von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Ann Intern Med. 2007;147:573–577. doi:10.7326/0003-4819-147-8-200710160-00010.

19. Tapia MD, Sow SO, Lyke KE, Haidara FC, Diallo F, Doumbia M, et al. Use of ChAd3-EBO-Z Ebola virus vaccine in Malian and US adults, and boosting of Malian adults with MVA-BN-Filo: a phase 1, randomised, double-blind, dummy-controlled trial. Lancet Infect Dis. 2016;16:31–42. doi:10.1016/S1473-3099(15)00362-X.

20. Milligan ID, Gibani MM, Sewell R, Clutterbuck EA, Campbell D, Plested E, et al. Safety and immunogenicity of novel adenovirus type 26- and modified vaccinia Ankara-vectored Ebola vaccines: a randomized clinical trial. JAMA. 2016;315:1610–1623. doi:10.1001/jama.2016.4218.

21. Qiu X, Wong G, Audet J, Bello A, Fernando L, Alimonti JB, et al. Reversion of advanced Ebola virus disease in nonhuman primates with ZMapp. Nature. 2014;514:47–53. doi:10.1038/nature13777.

22. Rodger AJ, Cambiano V, Bruun T, Vernazza P, Collins S, van Lunzen J, et al. Sexual activity without condoms and risk of HIV transmission in serodifferent couples when the HIV-positive partner is using suppressive antiretroviral therapy: the PARTNER study. JAMA. 2016;316:171–181. doi:10.1001/jama.2016.5148.

23. Peterson L, Taylor D, Roddy R, Belai G, Phillips P, Nanda K, et al. Tenofovir disoproxil fumarate for prevention of HIV infection in women: a phase 2, double-blind, randomized, placebo-controlled trial. PLoS Clin Trials. 2007;2:e27. doi:10.1371/journal.pctr.0020027.

24. Marrazzo JM, Ramjee G, Richardson BA, Gomez K, Mgodi N, Nair G, et al. Tenofovir-based preexposure prophylaxis for HIV infection among African women. N Engl J Med. 2015;372:509–518. doi:10.1056/NEJMoa1402269.

25. Van Damme L, Corneli A, Ahmed K, Agot K, Lombaard J, Kapiga S, et al. Preexposure prophylaxis for HIV infection among African women. N Engl J Med. 2012;367:411–422. doi:10.1056/NEJMoa1202614.

26. Cohen MS, Chen YQ, McCauley M, Gamble T, Hosseinipour MC, Kumarasamy N, et al. Prevention of HIV-1 infection with early antiretroviral therapy. N Engl J Med. 2011;365:493–505. doi:10.1056/NEJMoa1105243.

27. Polack FP, Thomas SJ, Kitchin N, Absalon J, Gurtman A, Lockhart S, et al. Safety and efficacy of the BNT162b2 mRNA Covid-19 vaccine. N Engl J Med. 2020;383:2603–2615. doi:10.1056/NEJMoa2034577.

28. Baden LR, El Sahly HM, Essink B, Kotloff K, Frey S, Novak R, et al. Efficacy and safety of the mRNA-1273 SARS-CoV-2 vaccine. N Engl J Med. 2021;384:403–416. doi:10.1056/NEJMoa2035389.

29. Voysey M, Clemens SAC, Madhi SA, Weckx LY, Folegatti PM, Aley PK, et al. Safety and efficacy of the ChAdOx1 nCoV-19 vaccine (AZD1222) against SARS-CoV-2: an interim analysis of four randomised controlled trials in Brazil, South Africa, and the UK. Lancet. 2021;397:99–111. doi:10.1016/S0140-6736(20)32661-1.

---

## Figure legends

**Figure 1.** Observed female enrollment (points, Wilson 95% CI) and trial-specific expected share (diamonds) in 10 mixed-sex pivotal trials. The dashed line is the conventional 50% audit statistic, shown only as a contrast: it is the wrong comparator for occupationally or epidemiologically skewed protocols.

**Figure 2.** Enrollment ratio (observed/expected) for the same 10 trials. Values near 1 indicate a match to the target-population comparator. rVSV-ZEBOV (0.75) is the largest shortfall; PALM (1.11) is the largest excess.

**Supplementary Figure S1.** Reconstruction of the analysis set from the original 15 named studies.

---

*Table 1 (observed female enrollment versus expected share, all primary trials) is generated from `results/trial_level_estimates.csv` by `src/build_docx.py` and appears after this section in `Manuscript_Trials_R1.docx`.*
