"""
Sprint 2 - Day 13

Ratio Edge Case Logger
"""

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


def generate_edge_case_log(df):
    """
    Generate edge case log for unusual financial ratios.
    """

    edge_cases = []

    for _, row in df.iterrows():

        # Negative Equity
        equity = row["equity_capital"] + row["reserves"]

        if equity <= 0:
            edge_cases.append({
                "company_id": row["company_id"],
                "year": row["year"],
                "issue": "Negative Equity",
                "category": "Formula Edge Case"
            })

        # Zero Sales
        if row["sales"] == 0:
            edge_cases.append({
                "company_id": row["company_id"],
                "year": row["year"],
                "issue": "Zero Sales",
                "category": "Formula Edge Case"
            })

        # Zero Interest
        if row["interest"] == 0:
            edge_cases.append({
                "company_id": row["company_id"],
                "year": row["year"],
                "issue": "Debt Free",
                "category": "Business Case"
            })

    edge_df = pd.DataFrame(edge_cases)

    log_file = OUTPUT_DIR / "ratio_edge_cases.csv"

    edge_df.to_csv(
        log_file,
        index=False,
    )

    print(f"\nEdge Case Log saved to:\n{log_file}")

    return edge_df