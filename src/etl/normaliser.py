"""
Data normalization functions for Nifty100 ETL pipeline.
"""

import re


def normalize_year(year_value):
    """
    Convert year formats to a standard integer year.
    """

    if year_value is None:
        return None

    year_str = str(year_value).strip()

    match = re.search(r"(\d{2})$", year_str)

    if match:
        yy = int(match.group(1))
        return 2000 + yy

    if year_str.isdigit():
        return int(year_str)

    return None


def normalize_ticker(ticker):
    """
    Standardize ticker/company IDs.
    """

    if ticker is None:
        return None

    return str(ticker).strip().upper()