"""
Javelin.AI - Signal Analysis
============================
Run this BEFORE deciding on a modeling approach.
This checks if DQ features actually correlate with SAE.

Usage:
    python src/check_signal.py
"""

import pandas as pd
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path("outputs")

def analyze_signal():
    print("=" * 70)
    print("JAVELIN.AI - SIGNAL ANALYSIS")
    print("Do Data Quality issues correlate with SAE?")
    print("=" * 70)

    # Load data
    df = pd.read_csv(OUTPUT_DIR / "master_subject.csv")
    print(f"\nLoaded {len(df):,} subjects")

    # Create target
    df['has_sae'] = (df['sae_total_count'] > 0).astype(int)

    features = [
        'missing_visit_count', 'max_days_outstanding', 'lab_issues_count',
        'missing_pages_count', 'max_days_page_missing', 'uncoded_meddra_count',
        'uncoded_whodd_count', 'inactivated_forms_count', 'edrr_open_issues'
    ]

    baseline_sae_rate = df['has_sae'].mean()
    print(f"\nBaseline SAE rate: {baseline_sae_rate:.1%}")

    print("\n" + "-" * 70)
    print("SAE RATE BY FEATURE")
    print("(Does having issue X increase probability of SAE?)")
    print("-" * 70)

    results = []
    for feat in features:
        if feat not in df.columns:
            continue

        has_issue = df[feat] > 0
        n_with_issue = has_issue.sum()

        if n_with_issue == 0:
            continue

        sae_rate_with = df[has_issue]['has_sae'].mean()
        sae_rate_without = df[~has_issue]['has_sae'].mean()

        lift = sae_rate_with / baseline_sae_rate if baseline_sae_rate > 0 else 0

        results.append({
            'feature': feat,
            'n_with_issue': n_with_issue,
            'sae_rate_with': sae_rate_with,
            'sae_rate_without': sae_rate_without,
            'lift': lift
        })

        if lift > 1.5:
            signal = "*** STRONG ***"
        elif lift > 1.2:
            signal = "** MODERATE **"
        elif lift > 1.0:
            signal = "* WEAK *"
        else:
            signal = "(negative)"

        print(f"\n{feat}:")
        print(f"  Subjects with issue: {n_with_issue:,} ({n_with_issue/len(df):.1%})")
        print(f"  SAE rate WITH issue:    {sae_rate_with:.1%}")
        print(f"  SAE rate WITHOUT issue: {sae_rate_without:.1%}")
        print(f"  Lift vs baseline: {lift:.2f}x  {signal}")

    print("\n" + "-" * 70)
    print("OVERLAP ANALYSIS")
    print("-" * 70)

    # How many subjects have BOTH SAE and any DQ issue?
    available_features = [f for f in features if f in df.columns]
    df['any_dq_issue'] = (df[available_features].sum(axis=1) > 0).astype(int)

    sae_subjects = df['has_sae'].sum()
    dq_subjects = df['any_dq_issue'].sum()
    both = ((df['has_sae'] == 1) & (df['any_dq_issue'] == 1)).sum()

    print(f"\nSubjects with SAE: {sae_subjects:,}")
    print(f"Subjects with any DQ issue: {dq_subjects:,}")
    print(f"Subjects with BOTH: {both:,}")
    print(f"\nOf SAE subjects, {both/sae_subjects:.1%} have DQ issues")
    print(f"Of DQ subjects, {both/dq_subjects:.1%} have SAE")

    print("\n" + "-" * 70)
    print("COMPOSITE FEATURES")
    print("-" * 70)

    # Count of issue types per subject
    df['n_issue_types'] = (df[available_features] > 0).sum(axis=1)

    print("\nSAE rate by number of issue types:")
    for n in range(0, min(6, df['n_issue_types'].max() + 1)):
        subset = df[df['n_issue_types'] == n]
        if len(subset) > 100:  # Only show if enough samples
            print(f"  {n} issue types: {len(subset):,} subjects, SAE rate: {subset['has_sae'].mean():.1%}")

    print("\n" + "-" * 70)
    print("CORRELATION MATRIX")
    print("-" * 70)

    corr_cols = available_features + ['has_sae']
    corr_matrix = df[corr_cols].corr()

    print("\nCorrelation with has_sae:")
    sae_corr = corr_matrix['has_sae'].drop('has_sae').sort_values(ascending=False)
    for feat, corr in sae_corr.items():
        strength = "GOOD" if abs(corr) > 0.1 else "WEAK" if abs(corr) > 0.05 else "NONE"
        print(f"  {feat}: {corr:+.3f} [{strength}]")

    print("\n" + "=" * 70)
    print("RECOMMENDATION")
    print("=" * 70)

    avg_lift = np.mean([r['lift'] for r in results if r['lift'] > 0])
    max_corr = sae_corr.abs().max()

    print(f"\nAverage lift: {avg_lift:.2f}x")
    print(f"Max correlation: {max_corr:.3f}")

    if avg_lift > 1.5 or max_corr > 0.15:
        print("\n>>> STRONG SIGNAL: Better modeling will help!")
        print("    Recommendation: XGBoost with class balancing + feature engineering")
    elif avg_lift > 1.2 or max_corr > 0.08:
        print("\n>>> MODERATE SIGNAL: Some predictive power exists")
        print("    Recommendation: Try ensemble methods, add composite features")
    elif avg_lift > 1.0 or max_corr > 0.03:
        print("\n>>> WEAK SIGNAL: Limited predictive power")
        print("    Recommendation: Focus on feature engineering, consider different target")
    else:
        print("\n>>> MINIMAL SIGNAL: DQ metrics don't predict SAE well")
        print("    Recommendation: Use domain-knowledge heuristic weights instead")
        print("    This is still valid - it means DQ issues are independent of SAE")

    # Save results
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('lift', ascending=False)
    results_df.to_csv(OUTPUT_DIR / "signal_analysis.csv", index=False)
    print(f"\nSaved: outputs/signal_analysis.csv")


if __name__ == "__main__":
    analyze_signal()