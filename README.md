# Scoring sex representativeness against the wrong denominator

Reproducibility package for the *Trials* revision of:

**Stillwell, R.C.** Scoring sex representativeness against the wrong denominator: target-population analysis of pivotal infectious disease trials.

**Repository:** https://github.com/rstil2/infectious-disease-trial-sex-enrollment

## Contents

| Path | Description |
|------|-------------|
| `data/verified_trials.csv` | Extracted n, female n, expected share, DOI, source note |
| `data/screening_log.csv` | Decision for each originally named study |
| `data/STROBE_checklist.csv` | STROBE item locations |
| `src/analysis.py` | Descriptives, Bayesian random-effects model, figures (seed 42) |
| `src/build_docx.py` | Builds Word files from the markdown sources |
| `results/` | Trial-level estimates, posterior draws, `summary.json` |
| `figures/` | Figures 1–2 and reconstruction flowchart |

## Reproduce

```bash
python3 -m pip install -r requirements.txt
python3 src/analysis.py
```

## License

MIT (code and compiled tables). Source counts remain copyright of the cited publications.
