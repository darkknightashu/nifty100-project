"""
Financial Ratio Engine
Sprint 2 - Day 11

Cash Flow KPI Engine
"""


def free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow (FCF)

    Formula:
    Operating Cash Flow + Investing Cash Flow
    """
    return operating_activity + investing_activity


def cfo_quality_score(cfo_values, pat_values):
    """
    Average CFO/PAT ratio over available years.

    Returns:
        (average_ratio, label)
    """

    ratios = []

    for cfo, pat in zip(cfo_values, pat_values):
        if pat == 0:
            continue
        ratios.append(cfo / pat)

    if not ratios:
        return None, None

    avg = sum(ratios) / len(ratios)

    if avg > 1:
        label = "High Quality"
    elif avg >= 0.5:
        label = "Moderate"
    else:
        label = "Accrual Risk"

    return round(avg, 2), label


def capex_intensity(investing_activity, sales):
    """
    CapEx Intensity (%)
    """

    if sales == 0:
        return None, None

    value = abs(investing_activity) / sales * 100

    if value < 3:
        label = "Asset Light"
    elif value <= 8:
        label = "Moderate"
    else:
        label = "Capital Intensive"

    return round(value, 2), label


def fcf_conversion_rate(fcf, operating_profit):
    """
    FCF Conversion Rate (%)
    """

    if operating_profit == 0:
        return None

    return round((fcf / operating_profit) * 100, 2)


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Capital Allocation Pattern
    """

    signs = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    patterns = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed"
    }

    return signs, patterns.get(signs, "Other")


