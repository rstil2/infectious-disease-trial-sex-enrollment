#!/usr/bin/env python3
"""Reconstructed analysis for Trials R1.

Primary estimand: female enrollment relative to a trial-specific expected
share given indication, eligibility, and target-population epidemiology.

Bayesian model (mixed-sex primary trials):
    y_i ~ Binomial(n_i, p_i)
    logit(p_i) = logit(pi_i) + alpha + delta[disease_i] + eps_i
    delta ~ Normal(0, sigma_d)
    eps   ~ Normal(0, sigma_e)

Priors are weakly informative. Time is omitted from the primary model
because disease is aliased with calendar era (COVID 2020; Ebola 2015-2019;
HIV 2008-2011).

Variance components are the disease and residual SDs on the logit-deviation
scale. Their squares sum to the between-trial variance of the linear
predictor; sampling (binomial) variance is separate.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import expit, logit
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "verified_trials.csv"
OUT = ROOT / "results"
FIG = ROOT / "figures"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)

RNG = np.random.default_rng(42)


def wilson_ci(k, n, z=1.96):
    if n == 0:
        return (np.nan, np.nan)
    p = k / n
    den = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / den
    half = z * np.sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / den
    return centre - half, centre + half


def trial_level(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for r in df.itertuples(index=False):
        p = r.n_female / r.n_analysis
        lo, hi = wilson_ci(r.n_female, r.n_analysis)
        pi = r.expected_female
        # Guard 0/1 expected for secondary set
        pi_clip = min(max(pi, 1e-6), 1 - 1e-6)
        p_clip = min(max(p, 1e-6), 1 - 1e-6)
        lor = logit(p_clip) - logit(pi_clip)
        se = np.sqrt(1 / (r.n_analysis * p_clip * (1 - p_clip)))
        ratio = p / pi if pi > 0 else np.nan
        rows.append(
            {
                "trial_id": r.trial_id,
                "short_name": r.short_name,
                "disease": r.disease,
                "year_mid": r.year_mid,
                "n": int(r.n_analysis),
                "n_female": int(r.n_female),
                "p": p,
                "p_lo": lo,
                "p_hi": hi,
                "pi": pi,
                "ratio": ratio,
                "lor": lor,
                "lor_se": se,
                "analysis_set": r.analysis_set,
            }
        )
    return pd.DataFrame(rows)


def bayes_re(lor, se, disease, n_iter=20000, n_burn=5000, thin=5):
    """Bayesian random-effects meta-analysis of log-odds deviations.

    hat_theta_i ~ N(alpha + delta[d_i], se_i^2)
    delta_d ~ N(0, sigma_d^2)
    extra residual: hat_theta_i ~ N(alpha + delta[d_i], se_i^2 + tau^2)

    With large n_i, binomial sampling error is tiny; tau captures remaining
    between-trial heterogeneity. Componentwise Metropolis updates.
    """
    lor = np.asarray(lor, dtype=float)
    se = np.asarray(se, dtype=float)
    dcode, uniques = pd.factorize(np.asarray(disease))
    n_d = len(uniques)
    k = len(lor)

    alpha = 0.0
    delta = np.zeros(n_d)
    log_tau = np.log(0.2)
    log_sd = np.log(0.2)

    def log_post(alpha, delta, log_tau, log_sd):
        tau = np.exp(log_tau)
        sd = np.exp(log_sd)
        mu = alpha + delta[dcode]
        var = se**2 + tau**2
        lp = -0.5 * np.sum(np.log(2 * np.pi * var) + (lor - mu) ** 2 / var)
        lp += -0.5 * alpha**2
        lp += -0.5 * np.sum(delta**2) / sd**2 - n_d * np.log(sd)
        lp += -0.5 * (tau / 0.5) ** 2 + log_tau
        lp += -0.5 * (sd / 0.5) ** 2 + log_sd
        return lp

    lp = log_post(alpha, delta, log_tau, log_sd)
    draws = []
    accept = {"alpha": 0, "delta": 0, "tau": 0, "sd": 0}
    n_scan = 0
    for t in range(n_iter):
        n_scan += 1
        a2 = alpha + 0.03 * RNG.normal()
        lp2 = log_post(a2, delta, log_tau, log_sd)
        if np.log(RNG.random()) < lp2 - lp:
            alpha, lp = a2, lp2
            accept["alpha"] += 1
        d2 = delta + 0.04 * RNG.normal(size=n_d)
        lp2 = log_post(alpha, d2, log_tau, log_sd)
        if np.log(RNG.random()) < lp2 - lp:
            delta, lp = d2, lp2
            accept["delta"] += 1
        lt2 = log_tau + 0.12 * RNG.normal()
        lp2 = log_post(alpha, delta, lt2, log_sd)
        if np.log(RNG.random()) < lp2 - lp:
            log_tau, lp = lt2, lp2
            accept["tau"] += 1
        ls2 = log_sd + 0.12 * RNG.normal()
        lp2 = log_post(alpha, delta, log_tau, ls2)
        if np.log(RNG.random()) < lp2 - lp:
            log_sd, lp = ls2, lp2
            accept["sd"] += 1
        if t >= n_burn and (t - n_burn) % thin == 0:
            tau = float(np.exp(log_tau))
            sd = float(np.exp(log_sd))
            tot = sd**2 + tau**2
            draws.append(
                {
                    "alpha": float(alpha),
                    "sigma_d": sd,
                    "sigma_e": tau,
                    "var_disease": sd**2,
                    "var_residual": tau**2,
                    "prop_disease": sd**2 / tot if tot > 0 else np.nan,
                    "prop_residual": tau**2 / tot if tot > 0 else np.nan,
                    **{f"delta_{u}": float(delta[i]) for i, u in enumerate(uniques)},
                }
            )
    post = pd.DataFrame(draws)
    acc = {k: v / n_scan for k, v in accept.items()}
    return post, acc, list(uniques)


def posterior_summary(x):
    x = np.asarray(x, dtype=float)
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "q025": float(np.quantile(x, 0.025)),
        "q975": float(np.quantile(x, 0.975)),
    }


def ds_laird(lor, se):
    """DerSimonian-Laird random-effects mean of log-odds ratios."""
    w = 1 / se**2
    mu_fe = np.sum(w * lor) / np.sum(w)
    q = np.sum(w * (lor - mu_fe) ** 2)
    k = len(lor)
    c = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0.0, (q - (k - 1)) / c)
    w_re = 1 / (se**2 + tau2)
    mu = np.sum(w_re * lor) / np.sum(w_re)
    se_mu = np.sqrt(1 / np.sum(w_re))
    return mu, se_mu, tau2


def make_forest(tl, path):
    sub = tl[tl.analysis_set == "primary"].copy().reset_index(drop=True)
    sub = sub.sort_values(["disease", "year_mid"])
    fig, ax = plt.subplots(figsize=(9.5, 7.2))
    y = np.arange(len(sub))
    ax.hlines(y, sub.p_lo, sub.p_hi, color="#444444", lw=1.4)
    ax.plot(sub.p, y, "o", color="#1f4e79", ms=6, label="Observed female share")
    ax.plot(sub.pi, y, "D", color="#c45c26", ms=5, label="Expected share")
    ax.set_yticks(y)
    ax.set_yticklabels(sub.short_name, fontsize=8)
    ax.set_xlabel("Female enrollment proportion")
    ax.set_xlim(0, 0.85)
    ax.axvline(0.5, color="#888888", ls="--", lw=0.8, label="Unconditional 50%")
    ax.legend(loc="lower right", fontsize=8, frameon=False)
    ax.set_title("Observed female enrollment vs trial-specific expected share")
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)


def make_ratio_forest(tl, path):
    sub = tl[tl.analysis_set == "primary"].copy().reset_index(drop=True)
    sub = sub.sort_values(["disease", "year_mid"])
    fig, ax = plt.subplots(figsize=(9.5, 7.2))
    y = np.arange(len(sub))
    ax.plot(sub.ratio, y, "o", color="#1f4e79", ms=6)
    ax.axvline(1.0, color="#888888", ls="--", lw=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels(sub.short_name, fontsize=8)
    ax.set_xlabel("Enrollment ratio (observed / expected)")
    ax.set_title("Enrollment ratio relative to target-population expected share")
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)


def make_prisma(path):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    def box(x, y, w, h, text):
        rec = plt.Rectangle((x, y), w, h, fill=True, facecolor="#f4f4f4", edgecolor="#222")
        ax.add_patch(rec)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8, wrap=True)

    box(3, 8.4, 4, 1.2, "Original submitted set\n15 named studies")
    box(3, 6.6, 4, 1.2, "Eligibility re-applied\nphase III/IV human RCT\nsex-stratified counts")
    box(0.4, 4.6, 3.4, 1.6, "Excluded (n=5)\nTapia 2016 phase 1\nMilligan 2016 phase 1\nQiu 2014 NHP\nPARTNER observational\nPeterson 2007 phase 2")
    box(6.2, 4.6, 3.4, 1.6, "Moved to secondary (n=3)\nVOICE women-only\nFEM-PrEP women-only\niPrEx MSM/TGW")
    box(3, 2.8, 4, 1.2, "Retained after count correction (n=7)\n+ added pivotal RCTs (n=3)")
    box(3, 1.0, 4, 1.3, "Primary mixed-sex analysis n=10\nCOVID-19 5; Ebola 2; HIV 3\nSecondary sex-specific n=3")
    ax.annotate("", xy=(5, 7.8), xytext=(5, 8.4), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(5, 4.0), xytext=(5, 6.6), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(5, 2.2), xytext=(5, 2.8), arrowprops=dict(arrowstyle="->"))
    fig.tight_layout()
    fig.savefig(path, dpi=300)
    plt.close(fig)


def main():
    df = pd.read_csv(DATA)
    tl = trial_level(df)
    tl.to_csv(OUT / "trial_level_estimates.csv", index=False)

    primary = tl[tl.analysis_set == "primary"].reset_index(drop=True)
    disease = primary.disease.to_numpy()

    post, acc, diseases = bayes_re(primary.lor.to_numpy(), primary.lor_se.to_numpy(), disease)
    post.to_csv(OUT / "posterior_draws.csv", index=False)

    mu, se_mu, tau2 = ds_laird(primary.lor.to_numpy(), primary.lor_se.to_numpy())

    summary = {
        "n_primary": int(len(primary)),
        "n_secondary": int((tl.analysis_set == "secondary_sex_specific").sum()),
        "mh_acceptance": acc,
        "alpha": posterior_summary(post.alpha),
        "sigma_d": posterior_summary(post.sigma_d),
        "sigma_e": posterior_summary(post.sigma_e),
        "prop_disease": posterior_summary(post.prop_disease),
        "prop_residual": posterior_summary(post.prop_residual),
        "dsl_lor_mean": float(mu),
        "dsl_lor_se": float(se_mu),
        "dsl_tau2": float(tau2),
        "alpha_or": {
            "mean": float(np.exp(post.alpha).mean()),
            "q025": float(np.exp(post.alpha).quantile(0.025)),
            "q975": float(np.exp(post.alpha).quantile(0.975)),
        },
        "trial_ratios": primary[["short_name", "disease", "p", "pi", "ratio"]].to_dict("records"),
        "mean_ratio": float(primary.ratio.mean()),
        "median_ratio": float(primary.ratio.median()),
    }
    # disease-specific deltas
    for d in diseases:
        col = f"delta_{d}"
        if col in post.columns:
            summary[col] = posterior_summary(post[col])

    # Sensitivity: unconditional 50% expected share
    p = primary.p.to_numpy()
    lor50 = logit(np.clip(p, 1e-6, 1 - 1e-6)) - logit(0.5)
    post50, _, _ = bayes_re(lor50, primary.lor_se.to_numpy(), disease)
    summary["sensitivity_50pct_alpha"] = posterior_summary(post50.alpha)
    summary["sensitivity_50pct_prop_residual"] = posterior_summary(post50.prop_residual)

    # Sensitivity: drop healthcare-worker trial
    mask = primary.trial_id.to_numpy() != "AZD1222"
    post_nohcw, _, _ = bayes_re(
        primary.lor.to_numpy()[mask],
        primary.lor_se.to_numpy()[mask],
        disease[mask],
    )
    summary["sensitivity_no_hcw_alpha"] = posterior_summary(post_nohcw.alpha)

    # Sensitivity: drop rVSV (pregnancy-exclusion outlier)
    mask2 = primary.trial_id.to_numpy() != "rVSV"
    post_noring, _, _ = bayes_re(
        primary.lor.to_numpy()[mask2],
        primary.lor_se.to_numpy()[mask2],
        disease[mask2],
    )
    summary["sensitivity_no_rvsv_alpha"] = posterior_summary(post_noring.alpha)

    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))

    make_forest(tl, FIG / "figure1_observed_vs_expected.png")
    make_ratio_forest(tl, FIG / "figure2_enrollment_ratio.png")
    make_prisma(FIG / "figure_s1_reconstruction_flow.png")
    print(json.dumps({k: summary[k] for k in ["n_primary", "alpha", "sigma_d", "sigma_e", "prop_residual", "prop_disease", "mh_acceptance", "mean_ratio"]}, indent=2))


if __name__ == "__main__":
    main()
