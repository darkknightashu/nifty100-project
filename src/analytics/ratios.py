"""
Financial Ratio Engine
Sprint 2
Profitability, Leverage & Efficiency Ratios
"""


def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin (%)
    Formula: (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin (%)
    Formula: (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity_capital, reserves):
    """
    Return on Equity (%)

    ROE = Net Profit / (Equity + Reserves) * 100
    """
    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return (net_profit / equity) * 100


def return_on_capital_employed(
    operating_profit,
    other_income,
    equity_capital,
    reserves,
    borrowings,
):
    """
    Return on Capital Employed (ROCE)

    EBIT = Operating Profit + Other Income
    Capital Employed = Equity + Reserves + Borrowings
    """
    capital = equity_capital + reserves + borrowings

    if capital <= 0:
        return None

    ebit = operating_profit + other_income

    return (ebit / capital) * 100


def return_on_assets(net_profit, total_assets):
    """
    Return on Assets (%)
    """
    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt to Equity Ratio
    """
    if borrowings == 0:
        return 0

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return borrowings / equity


def high_leverage_flag(de_ratio, sector):
    """
    Flag companies with high leverage.
    Financial companies are excluded.
    """
    if de_ratio is None:
        return False

    if sector and sector.lower() == "financials":
        return False

    return de_ratio > 5


def interest_coverage_ratio(
    operating_profit,
    other_income,
    interest,
):
    """
    Interest Coverage Ratio (ICR)
    """
    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def icr_label(icr):
    """
    Display label for debt-free companies.
    """
    if icr is None:
        return "Debt Free"

    return ""


def interest_warning_flag(icr):
    """
    Warn when interest coverage is weak.
    """
    if icr is None:
        return False

    return icr < 1.5


def net_debt(borrowings, investments):
    """
    Net Debt
    """
    return borrowings - investments


def asset_turnover(sales, total_assets):
    """
    Asset Turnover Ratio
    """
    if total_assets == 0:
        return None

    return sales / total_assets