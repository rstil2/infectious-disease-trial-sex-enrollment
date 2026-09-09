# Female enrollment versus target-population sex composition in pivotal infectious disease trials: a reconstructed Bayesian analysis of phase III/IV randomised trials

**Running title:** Target-population comparators for trial sex composition

**Article type:** Research

**Corresponding author:**  
R. Craig Stillwell, Ph.D.  
Independent Researcher  
Email: craig.stillwell@gmail.com  
Phone: 270-491-0493

---

## Abstract

**Background:** Apparent female underrepresentation in infectious disease trials is often judged against an unconditional 50% benchmark. That benchmark is inappropriate when eligibility, indication, or target-population epidemiology imply a different expected sex mix.

**Methods:** We reconstructed the analysis set from a previously submitted 15-study list. Eligibility required a phase III or II/III randomised trial in humans, with sex-stratified counts in the primary report. Phase I/II studies, observational cohorts, and nonhuman experiments were excluded. Sex-restricted trials were analysed separately. For mixed-sex trials, the estimand was the ratio of observed female enrollment to a trial-specific expected share given indication and eligibility. A Bayesian random-effects model summarised log-odds deviations from that expected share and partitioned remaining between-trial variance into disease-level and residual components. Time was omitted from the primary model because disease is aliased with calendar era.

**Results:** Five of 15 originally named studies did not meet the stated eligibility criteria (two phase 1 Ebola studies, one nonhuman-primate experiment, one observational HIV cohort, and one phase 2 trial). Three HIV prevention trials were sex-restricted by design (VOICE and FEM-PrEP, 100% female; iPrEx, cisgender women ineligible). Ten mixed-sex pivotal trials formed the primary set (COVID-19 n=5; Ebola n=2; HIV n=3; N=150,907). Median enrollment ratio versus the trial-specific expected share was 0.98 (range 0.75–1.11). The largest shortfall was rVSV-ZEBOV ring vaccination (32% female among immediately vaccinated versus 43% among enumerated contacts), consistent with pregnancy and breastfeeding exclusion. PALM enrolled 55.6% female patients and included pregnant women. The Bayesian mean log-odds deviation from expected was −0.11 (95% credible interval −0.34 to 0.17). Disease-level versus residual variance could not be identified (disease proportion 95% CrI 0.0004–0.89). The previously reported 72%/28% split and 2068–2074 parity projections are withdrawn.

**Conclusions:** In this reconstructed set, mixed-sex pivotal trials largely tracked their target populations. An unconditional 50% comparator misclassifies sex-specific indications and occupationally skewed samples. Pregnancy exclusion remains a measurable constraint in some prevention protocols. Variance decomposition into “systemic” versus “disease-specific” barriers is not identified with ten heterogeneous trials.

**Keywords:** clinical trials; sex; enrollment; eligibility criteria; infectious diseases; Bayesian random-effects; pregnancy exclusion

---

## Background

Sex-stratified enrollment is a basic requirement for judging whether a trial can support inference in women and men [1,2]. Underrepresentation of women has been documented across therapeutic areas and has consequences for adverse-event detection and dosing [2,3]. Those observations do not imply that every trial should be compared with a 50% female share. Expected composition depends on the intended use population, eligibility rules, and—when the trial enrolls a defined occupational or exposure group—the sex mix of that group.

This revision reconstructs a previously submitted analysis that treated 15 named studies as phase III/IV randomised human trials and compared female enrollment with 50% throughout. Peer review identified ineligible designs in that list, misapplication of the 50% benchmark to sex-restricted HIV prevention trials, unidentified residual variance in the hierarchical model, inconsistent time scaling, and unavailable extraction files. We rebuilt the eligible set, extracted counts from primary publications, replaced the 50% benchmark with trial-specific expected shares, and fitted a model in which residual between-trial variance is reported.

## Methods

### Reconstruction of the eligible set

The original submission listed 15 studies. We re-applied the stated criteria: (1) phase III or pivotal phase II/III randomised trial; (2) human participants; (3) sex-stratified enrollment extractable from the primary publication or ClinicalTrials.gov results tables; (4) COVID-19, Ebola, or HIV indication. We excluded phase I/II immunogenicity studies, observational cohorts, and nonhuman experiments. Sex-restricted trials (women-only or MSM/transgender-women indications) were eligible for a secondary analysis but not for the mixed-sex primary estimand.

We added three pivotal mixed-sex phase III trials that met the same rules and had extractable Table 1 sex counts: Ad26.COV2.S ENSEMBLE [4], NVX-CoV2373 United Kingdom [5], and Partners PrEP [6]. The reconstruction log is Supplementary Table S1. This is a reconstructed, protocol-specified sample of pivotal trials, not a new multi-registry search of 2,847 records. The previous 2,847 / 67-trial funnel is withdrawn because a trial-level screening log with verifiable registry identifiers was not available.

### Data extraction

For each included trial we recorded registry identifier, phase, design, analysis population as labelled in the source table, n, female n, pregnancy-related eligibility, and the citation. Counts were taken from the table that the paper used for baseline characteristics (safety population, per-protocol efficacy population, or randomised set, as reported). A single extractor (R.C.S.) recorded values; each count in Supplementary Table S2 is tied to a page-level source note. No fabricated sequential NCT identifiers were used.

### Expected female share

The comparator was defined before modelling, trial by trial:

- General adult COVID-19 vaccine trials: 0.50.
- ChAdOx1 nCoV-19: 0.70, because enrollment targeted health-care workers and women comprise approximately 70% of the global health and care workforce [7].
- rVSV-ZEBOV ring vaccination: 0.43, the female share among enumerated contacts [8].
- PALM: 0.50 (unselected EVD inpatients).
- HPTN 052 index partners: 0.50 (either sex eligible).
- Partners PrEP HIV-uninfected partners: 0.38, matching the documented 62% male share among HIV-negative partners in that heterosexual serodiscordant-couple design [6].
- Bangkok Tenofovir Study: 0.20, matching the ~80% male composition of the enrolled PWID population [9].
- VOICE and FEM-PrEP: 1.00 (women-only).
- iPrEx: 0 for cisgender women (male sex at birth required) [10].

Enrollment ratio = observed female proportion / expected share. Ratio 1.0 means the trial matched its target-population comparator.

### Statistical analysis

Wilson 95% confidence intervals were computed for each observed proportion. The primary Bayesian model used trial-level log-odds deviations \(\hat\theta_i=\mathrm{logit}(p_i)-\mathrm{logit}(\pi_i)\) with known sampling variances \(s_i^2=1/[n_i p_i(1-p_i)]\):

\[\hat\theta_i \sim \mathrm{Normal}(\alpha + \delta_{d[i]},\; s_i^2 + \tau^2),\quad \delta_d\sim\mathrm{Normal}(0,\sigma_\delta^2).\]

Priors: \(\alpha\sim\mathrm{Normal}(0,1)\); \(\tau,\sigma_\delta\sim\mathrm{HalfNormal}(0.5)\). The observational unit is the trial. \(\alpha\) is the mean log-odds deviation from the trial-specific expected share. \(\tau^2\) is residual between-trial variance; \(\sigma_\delta^2\) is disease-level variance. Their sum is the between-trial variance of the linear predictor; binomial sampling variance is already in \(s_i^2\). Posterior samples used componentwise Metropolis–Hastings (20,000 iterations; 5,000 discarded; seed 42).

Time (years or decades) was not included in the primary model. COVID-19 trials are all 2020, Ebola 2015–2019, and HIV 2008–2011; a global slope is not separately identified from disease.

Sensitivity analyses: (i) replace every mixed-sex expected share with 0.50; (ii) drop the health-care-worker trial; (iii) drop rVSV-ZEBOV. Long-range parity projections to 2068–2074 are not reported.

Analyses used Python 3.9+ (NumPy, SciPy, pandas). Code, extraction tables, and posterior draws are at https://github.com/rstil2/infectious-disease-trial-sex-enrollment and in Additional File 1.

### Terminology and reporting

Trial reports record sex as female/male. We use *sex* for those categories. This observational analysis of published trial reports follows STROBE (Supplementary File S3).

## Results

### Reconstruction

Of 15 originally named studies, five were ineligible: Tapia et al. (ChAd3-EBO-Z) and Milligan et al. (Ad26/MVA) are phase 1 [11,12]; Qiu et al. is a nonhuman-primate ZMapp experiment [13]; PARTNER is observational [14]; Peterson et al. is labelled phase 2 in the source paper [15]. Three trials were sex-restricted: VOICE, 5,029 women [16]; FEM-PrEP, 2,120 women [17]; iPrEx, 2,499 MSM and transgender women, with 29 participants (1.2%) identifying as women [10]. Seven original mixed-sex trials were retained after count correction. Three mixed-sex phase III trials were added. The primary set is 10 trials (N=150,907). Supplementary Figure S1 shows the reconstruction flow.

Corrected counts differ substantially from the submitted table. Examples: BNT162b2 49.4% female (18,631/37,706), not 34.3% [18]; mRNA-1273 47.3% (14,366/30,351) [19]; HPTN 052 49.5% female index partners (873/1,763), not 32.8% of n=5,876 [20]; Bangkok Tenofovir 20.2% female (487/2,413), not 38.9% of n=6,184 [9]; PALM 55.6% female (374/673), not 36.8% of n=5,686 [21]. VOICE and FEM-PrEP are 100% female, not ~35–37%.

### Mixed-sex enrollment versus expected share

Table 1 and Figure 1 show observed versus expected shares. Median ratio was 0.98. COVID-19 general-adult vaccine trials ranged from 45.0% (Ad26.COV2.S) to 49.4% (BNT162b2) against 50% expected. ChAdOx1 nCoV-19 enrolled 60.5% women in a health-care-worker-enriched sample, below a 70% workforce comparator but far above 50% [7,22]. HIV mixed-sex trials tracked their comparators: HPTN 052 49.5% versus 50%; Partners PrEP 37.6% versus 38%; Bangkok 20.2% versus 20%. PALM enrolled 55.6% women and reported that 6.1% of female participants were pregnant at EVD diagnosis [21]. rVSV-ZEBOV immediately vaccinated contacts were 32% women versus 43% among enumerated contacts [8]; eligibility excluded pregnant and breastfeeding individuals.

### Bayesian summary and variance components

The posterior mean of \(\alpha\) was −0.11 (95% CrI −0.34 to 0.17), compatible with no mean deviation from the trial-specific expected share. Residual SD \(\tau\) was 0.22 (0.13–0.40). Disease-level SD \(\sigma_\delta\) was 0.15 (0.005–0.61). The residual share of between-trial variance had 95% CrI 0.11–1.00. A 72%/28% systemic-versus-disease split is not supported. Inverse-variance pooling, which is dominated by the largest COVID-19 trials, gave a mean log-odds deviation of −0.12 (SE 0.044). After dropping rVSV-ZEBOV, \(\alpha\) was −0.01 (−0.26 to 0.29). Replacing all expected shares with 0.50 produced a more negative mean (α −0.33, CrI −1.09 to 0.22), illustrating that the unconditional 50% benchmark, not a shared recruitment process, generates the appearance of large “systemic” underrepresentation.

### Sex-restricted trials

VOICE and FEM-PrEP enrolled only women, as designed [16,17]. iPrEx excluded cisgender women by eligibility [10]. Comparing these trials with 50% is not a valid estimand.

### Protocol features

Pregnancy exclusion at entry was present in the COVID-19 vaccine trials and in rVSV-ZEBOV, and women in Partners PrEP were not pregnant at enrollment [6]. PALM did not exclude pregnancy [21]. These features are descriptive; they were not entered as covariates in the hierarchical model.

## Discussion

After eligible designs are restored and the comparator is the target population, mixed-sex pivotal trials in this set do not show a uniform 34–36% female share. COVID-19 vaccine trials sit near 45–49%; HIV couple and PWID trials match their epidemiology; the Ebola treatment trial enrolled a female majority and included pregnant patients. The remaining, interpretable shortfall is rVSV-ZEBOV, where pregnancy and breastfeeding exclusions reduced female share relative to enumerated contacts.

The original 72% “systemic barriers” claim treated a global time trend as a variance component, omitted residual trial-level variance, and used ineligible studies. With ten mixed-sex trials and three diseases, disease-level variance is not separately identified from residual heterogeneity. We report that uncertainty rather than a point percentage.

We do not project parity years. A global time slope cannot be separated from disease in this sample, and the previous 2068–2074 figures used incorrect counts and an unidentified model.

### Limitations

The sample is a reconstructed pivotal-trial set, not a comprehensive registry census. Expected shares depend on documented design features; the 0.70 health-care-worker comparator is a published workforce average, not the exact occupational mix at ChAdOx1 sites. Extraction was performed by one reviewer. PALM is phase II/III. Geographic site-level sex mix was rarely published and is unmodelled. The Bayesian variance split has wide credible intervals and should not be used for policy ranking of “systemic” versus “disease-specific” causes.

## Conclusions

In a reconstructed set of 10 mixed-sex phase III/II–III infectious disease trials, female enrollment generally matched trial-specific expected shares. Sex-restricted HIV prevention trials should not be scored against 50%. Pregnancy exclusion in ring vaccination is a concrete protocol constraint. Hierarchical variance decomposition of “systemic” versus “disease-specific” barriers is not identified here and is not reported as a policy estimand.

## Declarations

**Ethics approval and consent to participate:** Not applicable. This study used published aggregate trial reports. No individual participant data were accessed.

**Consent for publication:** Not applicable.

**Availability of data and materials:** Extraction tables, screening log, analysis code, and posterior draws are at https://github.com/rstil2/infectious-disease-trial-sex-enrollment (MIT license) and in Additional File 1. All source counts are from cited publications and ClinicalTrials.gov.

**Competing interests:** The author declares no competing interests.

**Funding:** None.

**Authors’ contributions:** R.C.S. designed the reconstruction, extracted data, wrote the code, fitted the models, and wrote the manuscript.

**Acknowledgements:** The author thanks the original trial participants and investigators who reported sex-stratified enrollment.

---

## References

1. Clayton JA, Tannenbaum C. Reporting sex, gender, or both in clinical research? JAMA. 2016;316:1863–1864. doi:10.1001/jama.2016.16405.

2. Feldman S, Ammar W, Lo K, Trepman E, van Zuylen L, Etzioni O. Quantifying sex bias in clinical studies at scale with automated data extraction. JAMA Netw Open. 2019;2:e196700. doi:10.1001/jamanetworkopen.2019.6700.

3. Zucker I, Prendergast BJ. Sex differences in pharmacokinetics predict adverse drug reactions in women. Biol Sex Differ. 2020;11:32. doi:10.1186/s13293-020-00308-5.

4. Sadoff J, Gray G, Vandebosch A, Cárdenas V, Shukarev G, Grinsztejn B, et al. Safety and efficacy of single-dose Ad26.COV2.S vaccine against Covid-19. N Engl J Med. 2021;384:2187–2201. doi:10.1056/NEJMoa2101544.

5. Heath PT, Galiza EP, Baxter DN, Boffito M, Browne D, Burns F, et al. Safety and efficacy of NVX-CoV2373 Covid-19 vaccine. N Engl J Med. 2021;385:1172–1183. doi:10.1056/NEJMoa2107659.

6. Baeten JM, Donnell D, Ndase P, Mugo NR, Campbell JD, Wangisi J, et al. Antiretroviral prophylaxis for HIV prevention in heterosexual men and women. N Engl J Med. 2012;367:399–410. doi:10.1056/NEJMoa1108524.

7. World Health Organization. Closing the leadership gap: gender equity and leadership in the global health and care workforce. Geneva: WHO; 2021. https://www.who.int/publications/i/item/9789240025905.

8. Henao-Restrepo AM, Camacho A, Longini IM, Watson CH, Edmunds WJ, Egger M, et al. Efficacy and effectiveness of an rVSV-vectored vaccine in preventing Ebola virus disease: final results from the Guinea ring vaccination, open-label, cluster-randomised trial (Ebola Ça Suffit!). Lancet. 2017;389:505–518. doi:10.1016/S0140-6736(16)32621-6.

9. Choopanya K, Martin M, Suntharasamai P, Sangkum U, Mock PA, Leethochawalit M, et al. Antiretroviral prophylaxis for HIV infection in injecting drug users in Bangkok, Thailand (the Bangkok Tenofovir Study): a randomised, double-blind, placebo-controlled phase 3 trial. Lancet. 2013;381:2083–2090. doi:10.1016/S0140-6736(13)61127-7.

10. Grant RM, Lama JR, Anderson PL, McMahan V, Liu AY, Vargas L, et al. Preexposure chemoprophylaxis for HIV prevention in men who have sex with men. N Engl J Med. 2010;363:2587–2599. doi:10.1056/NEJMoa1011205.

11. Tapia MD, Sow SO, Lyke KE, Haidara FC, Diallo F, Doumbia M, et al. Use of ChAd3-EBO-Z Ebola virus vaccine in Malian and US adults, and boosting of Malian adults with MVA-BN-Filo: a phase 1, randomised, double-blind, dummy-controlled trial. Lancet Infect Dis. 2016;16:31–42. doi:10.1016/S1473-3099(15)00362-X.

12. Milligan ID, Gibani MM, Sewell R, Clutterbuck EA, Campbell D, Plested E, et al. Safety and immunogenicity of novel adenovirus type 26- and modified vaccinia Ankara-vectored Ebola vaccines: a randomized clinical trial. JAMA. 2016;315:1610–1623. doi:10.1001/jama.2016.4218.

13. Qiu X, Wong G, Audet J, Bello A, Fernando L, Alimonti JB, et al. Reversion of advanced Ebola virus disease in nonhuman primates with ZMapp. Nature. 2014;514:47–53. doi:10.1038/nature13777.

14. Rodger AJ, Cambiano V, Bruun T, Vernazza P, Collins S, van Lunzen J, et al. Sexual activity without condoms and risk of HIV transmission in serodifferent couples when the HIV-positive partner is using suppressive antiretroviral therapy: the PARTNER study. JAMA. 2016;316:171–181. doi:10.1001/jama.2016.5148.

15. Peterson L, Taylor D, Roddy R, Belai G, Phillips P, Nanda K, et al. Tenofovir disoproxil fumarate for prevention of HIV infection in women: a phase 2, double-blind, randomized, placebo-controlled trial. PLoS Clin Trials. 2007;2:e27. doi:10.1371/journal.pctr.0020027.

16. Marrazzo JM, Ramjee G, Richardson BA, Gomez K, Mgodi N, Nair G, et al. Tenofovir-based preexposure prophylaxis for HIV infection among African women. N Engl J Med. 2015;372:509–518. doi:10.1056/NEJMoa1402269.

17. Van Damme L, Corneli A, Ahmed K, Agot K, Lombaard J, Kapiga S, et al. Preexposure prophylaxis for HIV infection among African women. N Engl J Med. 2012;367:411–422. doi:10.1056/NEJMoa1202614.

18. Polack FP, Thomas SJ, Kitchin N, Absalon J, Gurtman A, Lockhart S, et al. Safety and efficacy of the BNT162b2 mRNA Covid-19 vaccine. N Engl J Med. 2020;383:2603–2615. doi:10.1056/NEJMoa2034577.

19. Baden LR, El Sahly HM, Essink B, Kotloff K, Frey S, Novak R, et al. Efficacy and safety of the mRNA-1273 SARS-CoV-2 vaccine. N Engl J Med. 2021;384:403–416. doi:10.1056/NEJMoa2035389.

20. Cohen MS, Chen YQ, McCauley M, Gamble T, Hosseinipour MC, Kumarasamy N, et al. Prevention of HIV-1 infection with early antiretroviral therapy. N Engl J Med. 2011;365:493–505. doi:10.1056/NEJMoa1105243.

21. Mulangu S, Dodd LE, Davey RT Jr, Tshiani Mbaya O, Proschan M, Mukadi D, et al. A randomized, controlled trial of Ebola virus disease therapeutics. N Engl J Med. 2019;381:2293–2303. doi:10.1056/NEJMoa1910993.

22. Voysey M, Clemens SAC, Madhi SA, Weckx LY, Folegatti PM, Aley PK, et al. Safety and efficacy of the ChAdOx1 nCoV-19 vaccine (AZD1222) against SARS-CoV-2: an interim analysis of four randomised controlled trials in Brazil, South Africa, and the UK. Lancet. 2021;397:99–111. doi:10.1016/S0140-6736(20)32661-1.

23. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.

---

## Figure legends

**Figure 1.** Observed female enrollment (points, Wilson 95% CI) and trial-specific expected share (diamonds) in 10 mixed-sex pivotal trials. The dashed line is an unconditional 50% benchmark, shown only for reference.

**Figure 2.** Enrollment ratio (observed/expected) for the same 10 trials. Values near 1 indicate match to the target-population comparator.

**Supplementary Figure S1.** Reconstruction of the analysis set from the original 15 named studies.

---

## Table 1. Mixed-sex primary analysis set

See `results/trial_level_estimates.csv` and the Word table generated by `src/build_docx.py`.
