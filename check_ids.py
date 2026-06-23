from src.etl.loader import load_excel

companies = load_excel("data/raw/companies.xlsx")
profitandloss = load_excel("data/raw/profitandloss.xlsx")

company_ids = set(companies["id"].astype(str).str.strip().str.upper())

for ticker in [
    "ULTRACEMCO",
    "UNIONBANK",
    "UNITDSPR",
    "VBL",
    "VEDL",
    "WIPRO",
    "ZOMATO",
    "ZYDUSLIFE"
]:
    print(
        ticker,
        ticker in company_ids
    )
print("\nLast 30 company IDs:")
print(companies["id"].sort_values().tail(30).to_list())
print("\nCompany IDs containing 'W'")
print(
    companies[
        companies["id"].str.contains("W", case=False, na=False)
    ]["id"].to_list()
)