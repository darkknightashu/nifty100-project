"""
Reusable Excel Loader
"""

import pandas as pd
from pathlib import Path


def load_excel(file_path):
    df = pd.read_excel(file_path, header=1)

    print(f"\nLoaded: {Path(file_path).name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


if __name__ == "__main__":

    files = [
        "companies.xlsx",
        "profitandloss.xlsx",
        "balancesheet.xlsx",
        "cashflow.xlsx",
        "analysis.xlsx",
        "documents.xlsx",
        "prosandcons.xlsx",
        "financial_ratios.xlsx",
        "market_cap.xlsx",
        "peer_groups.xlsx",
        "sectors.xlsx",
        "stock_prices.xlsx"
    ]

    for file in files:
        load_excel(f"data/raw/{file}")
with open("../src/etl/loader.py", "r", encoding="utf-8") as f:
    print(f.read())