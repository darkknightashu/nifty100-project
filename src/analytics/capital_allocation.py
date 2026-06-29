"""
Capital Allocation Pattern Engine
Sprint 2 - Day 11
"""

import pandas as pd


def capital_allocation_pattern(cfo, cfi, cff):
    """
    Classify capital allocation pattern.
    """

    cfo_sign = "+" if cfo >= 0 else "-"
    cfi_sign = "+" if cfi >= 0 else "-"
    cff_sign = "+" if cff >= 0 else "-"

    signs = (cfo_sign, cfi_sign, cff_sign)

    patterns = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
        ("+", "-", "+"): "Mixed",
    }

    label = patterns.get(signs, "Unknown")

    return signs, label

if __name__ == "__main__":

    print(
        capital_allocation_pattern(
            100,
            -50,
            -20,
        )
    )