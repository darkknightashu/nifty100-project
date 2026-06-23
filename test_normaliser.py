from src.etl.normaliser import normalize_year, normalize_ticker

print(normalize_year("FY23"))
print(normalize_year("2022-23"))
print(normalize_ticker(" reliance "))