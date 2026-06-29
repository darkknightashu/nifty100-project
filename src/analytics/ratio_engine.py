"""
Financial Ratio Engine
Sprint 2

Main Ratio Engine
"""

import sqlite3
import pandas as pd
import re
from pathlib import Path

from ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
    net_debt,
)

from capital_allocation import capital_allocation_pattern

from edge_case_logger import generate_edge_case_log

from cagr import (
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)

from cashflow_kpis import (
    free_cash_flow,
    capex_intensity,
    cfo_quality_score,
    fcf_conversion_rate,
)

BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE = BASE_DIR / "db" / "nifty100.db"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


def get_connection():
    """Create SQLite connection."""
    return sqlite3.connect(DATABASE)


def load_data():
    """Load tables from SQLite."""

    conn = get_connection()

    profit = pd.read_sql("SELECT * FROM profitandloss", conn)
    balance = pd.read_sql("SELECT * FROM balancesheet", conn)
    cashflow = pd.read_sql("SELECT * FROM cashflow", conn)

    conn.close()

    return profit, balance, cashflow


def normalize_year(year_value):
    """
    Convert values like:

    Mar 2023
    Dec 2022
    Mar 2016 9m

    into

    2023
    2022
    2016
    """

    if pd.isna(year_value):
        return None

    match = re.search(r"(19|20)\d{2}", str(year_value))

    if match:
        return int(match.group())

    return None


def merge_data(profit, balance, cashflow):
    """Merge all tables."""

    profit = profit.drop_duplicates(
        subset=["company_id", "year"],
        keep="first",
    )

    balance = balance.drop_duplicates(
        subset=["company_id", "year"],
        keep="first",
    )

    cashflow = cashflow.drop_duplicates(
        subset=["company_id", "year"],
        keep="first",
    )

    df = profit.merge(
        balance,
        on=["company_id", "year"],
        how="left",
    )

    df = df.merge(
        cashflow,
        on=["company_id", "year"],
        how="left",
    )

    df["financial_year"] = df["year"].apply(normalize_year)

    df = df.sort_values(
        ["company_id", "financial_year"]
    ).reset_index(drop=True)

    return df
def calculate_ratios(df):
    """
    Calculate financial ratios for each company-year.
    """

    result = pd.DataFrame()

    # Basic Information
    result["company_id"] = df["company_id"]
    result["year"] = df["year"]

    # Profitability Ratios
    result["net_profit_margin_pct"] = df.apply(
        lambda x: net_profit_margin(
            x["net_profit"],
            x["sales"],
        ),
        axis=1,
    )

    result["operating_profit_margin_pct"] = df.apply(
        lambda x: operating_profit_margin(
            x["operating_profit"],
            x["sales"],
        ),
        axis=1,
    )

    result["return_on_equity_pct"] = df.apply(
        lambda x: return_on_equity(
            x["net_profit"],
            x["equity_capital"],
            x["reserves"],
        ),
        axis=1,
    )

    result["return_on_assets_pct"] = df.apply(
        lambda x: return_on_assets(
            x["net_profit"],
            x["total_assets"],
        ),
        axis=1,
    )

    # Leverage Ratios
    result["debt_to_equity"] = df.apply(
        lambda x: debt_to_equity(
            x["borrowings"],
            x["equity_capital"],
            x["reserves"],
        ),
        axis=1,
    )

    result["interest_coverage"] = df.apply(
        lambda x: interest_coverage_ratio(
            x["operating_profit"],
            x["other_income"],
            x["interest"],
        ),
        axis=1,
    )

    result["asset_turnover"] = df.apply(
        lambda x: asset_turnover(
            x["sales"],
            x["total_assets"],
        ),
        axis=1,
    )

    # Cash Flow KPIs
    result["free_cash_flow_cr"] = df.apply(
        lambda x: free_cash_flow(
            x["operating_activity"],
            x["investing_activity"],
        ),
        axis=1,
    )

    result["total_debt_cr"] = df["borrowings"]

    result["cash_from_operations_cr"] = df["operating_activity"]

    result["earnings_per_share"] = df["eps"]

    result["book_value_per_share"] = (
        (df["equity_capital"] + df["reserves"]) /
        df["equity_capital"].replace(0, pd.NA)
    )

    result["dividend_payout_ratio_pct"] = df["dividend_payout"]


    return result


def save_ratios_to_database(ratio_df):
    """
    Save calculated ratios to SQLite.
    """

    conn = get_connection()

    ratio_df.to_sql(
        "financial_ratios",
        conn,
        if_exists="replace",
        index=False,
    )

    conn.close()

    print("\nfinancial_ratios table updated successfully.")


def generate_capital_allocation(df):
    """
    Generate capital allocation CSV.
    """

    output = pd.DataFrame()

    output["company_id"] = df["company_id"]
    output["year"] = df["year"]

    output["cfo_sign"] = df["operating_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    output["cfi_sign"] = df["investing_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    output["cff_sign"] = df["financing_activity"].apply(
        lambda x: "+" if x >= 0 else "-"
    )

    output["pattern_label"] = df.apply(
        lambda x: capital_allocation_pattern(
            x["operating_activity"],
            x["investing_activity"],
            x["financing_activity"],
        )[1],
        axis=1,
    )

    csv_path = OUTPUT_DIR / "capital_allocation.csv"

    output.to_csv(
        csv_path,
        index=False,
    )

    print(f"\nCapital allocation file saved to:\n{csv_path}")

def main():

    print("=" * 60)
    print("Financial Ratio Engine")
    print("=" * 60)

    profit, balance, cashflow = load_data()

    print("Profit & Loss :", len(profit))
    print("Balance Sheet :", len(balance))
    print("Cash Flow     :", len(cashflow))

    print("\nDuplicate Check")
    print("-" * 30)

    print(
        "Profit duplicates :",
        profit.duplicated(subset=["company_id", "year"]).sum()
    )

    print(
        "Balance duplicates:",
        balance.duplicated(subset=["company_id", "year"]).sum()
    )

    print(
        "Cashflow duplicates:",
        cashflow.duplicated(subset=["company_id", "year"]).sum()
    )

    # 👇 THIS IS THE BLOCK YOU WERE ASKING ABOUT
    df = merge_data(
        profit,
        balance,
        cashflow,
    )

    print("\nMerged Records :", len(df))

    ratio_df = calculate_ratios(df)

    print("\nCalculated Ratios")
    print("-" * 40)
    print(ratio_df.head())

    save_ratios_to_database(ratio_df)

    generate_capital_allocation(df)

    generate_edge_case_log(df)


    conn = get_connection()
    

    count = pd.read_sql(
    "SELECT COUNT(*) AS total FROM financial_ratios",
    conn,
)

    print("\nRows in financial_ratios:")
    print(count)

    conn.close()
    print(
        "Unique company-year rows :",
        len(df)
    )

    print(
        "Unique Companies :",
        df["company_id"].nunique()
    )

    years = [int(y) for y in sorted(df["financial_year"].dropna().unique())]

    print("Financial Years :", years)

    print("\nSample Company IDs:")
    print(sorted(df["company_id"].dropna().unique())[:20])

    print("\nSample Years:")
    print(sorted(df["year"].dropna().astype(str).unique())[:30])


if __name__ == "__main__":
    main()