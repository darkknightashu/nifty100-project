import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.etl.normaliser import normalize_year, normalize_ticker

# ------------------------
# normalize_year tests
# ------------------------

def test_year_fy23():
    assert normalize_year("FY23") == 2023

def test_year_24():
    assert normalize_year("24") == 2024

def test_year_2024():
    assert normalize_year("2024") == 2024

def test_year_none():
    assert normalize_year(None) is None

def test_year_string():
    assert normalize_year("FY22") == 2022

def test_year_25():
    assert normalize_year("25") == 2025

def test_year_26():
    assert normalize_year("26") == 2026

def test_year_27():
    assert normalize_year("27") == 2027

def test_year_28():
    assert normalize_year("28") == 2028

def test_year_29():
    assert normalize_year("29") == 2029

def test_year_30():
    assert normalize_year("30") == 2030

def test_year_with_space():
    assert normalize_year(" FY24 ") == 2024

def test_year_int():
    assert normalize_year(2025) == 2025

def test_year_text():
    assert normalize_year("Year24") == 2024

def test_year_fy20():
    assert normalize_year("FY20") == 2020

def test_year_fy21():
    assert normalize_year("FY21") == 2021

def test_year_empty():
    assert normalize_year("") is None

def test_year_invalid():
    assert normalize_year("ABC") is None

def test_year_single_digit():
    assert normalize_year("5") == 5

def test_year_zero():
    assert normalize_year("0") == 0


# ------------------------
# normalize_ticker tests
# ------------------------

def test_ticker_wipro():
    assert normalize_ticker("wipro") == "WIPRO"

def test_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_spaces():
    assert normalize_ticker(" infy ") == "INFY"

def test_ticker_none():
    assert normalize_ticker(None) is None

def test_ticker_hdfc():
    assert normalize_ticker("hdfcbank") == "HDFCBANK"

def test_ticker_reliance():
    assert normalize_ticker("reliance") == "RELIANCE"

def test_ticker_abb():
    assert normalize_ticker("abb") == "ABB"

def test_ticker_upper():
    assert normalize_ticker("WIPRO") == "WIPRO"

def test_ticker_mixed():
    assert normalize_ticker("WiPrO") == "WIPRO"

def test_ticker_empty():
    assert normalize_ticker("") == ""

def test_ticker_adani():
    assert normalize_ticker("adanient") == "ADANIENT"

def test_ticker_zomato():
    assert normalize_ticker("zomato") == "ZOMATO"

def test_ticker_vedl():
    assert normalize_ticker("vedl") == "VEDL"

def test_ticker_ultra():
    assert normalize_ticker("ultracemco") == "ULTRACEMCO"

def test_ticker_union():
    assert normalize_ticker("unionbank") == "UNIONBANK"