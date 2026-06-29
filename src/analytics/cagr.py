"""
Financial Ratio Engine
Sprint 2 - Day 10

CAGR Engine
"""

from math import pow


def calculate_cagr(start_value, end_value, years):
    """
    Calculate CAGR (Compound Annual Growth Rate)

    Formula:
    CAGR = ((End / Start) ** (1 / Years) - 1) * 100

    Returns:
        (value, flag)

    Flags:
        None
        ZERO_BASE
        DECLINE_TO_LOSS
        TURNAROUND
        BOTH_NEGATIVE
        INSUFFICIENT
    """

    # Not enough history
    if years <= 0:
        return None, "INSUFFICIENT"

    # Zero base
    if start_value == 0:
        return None, "ZERO_BASE"

    # Positive → Negative
    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    # Negative → Positive
    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    # Negative → Negative
    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    try:
        cagr = (pow(end_value / start_value, 1 / years) - 1) * 100
        return round(cagr, 2), None

    except Exception:
        return None, "CALCULATION_ERROR"


def revenue_cagr(start_revenue, end_revenue, years):
    """
    Revenue CAGR
    """
    return calculate_cagr(start_revenue, end_revenue, years)


def pat_cagr(start_pat, end_pat, years):
    """
    PAT CAGR
    """
    return calculate_cagr(start_pat, end_pat, years)


def eps_cagr(start_eps, end_eps, years):
    """
    EPS CAGR
    """
    return calculate_cagr(start_eps, end_eps, years)

