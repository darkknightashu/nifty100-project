from src.etl.loader import load_excel

from src.etl.validator import (
    dq01_pk_uniqueness,
    dq02_composite_pk,
    dq03_fk_integrity,
    save_validation_failure
)

companies = load_excel("data/raw/companies.xlsx")
dq01_pk_uniqueness(companies, "id")

profitandloss = load_excel("data/raw/profitandloss.xlsx")
dq02_composite_pk(
    profitandloss,
    ["company_id", "year"]
)

dq03_fk_integrity(
    profitandloss,
    companies,
    "company_id",
    "id"
)

save_validation_failure(
    "DQ-03",
    "CRITICAL",
    "Foreign key mismatch between profitandloss and companies",
    [
        "ULTRACEMCO",
        "UNIONBANK",
        "UNITDSPR",
        "VBL",
        "VEDL",
        "WIPRO",
        "ZOMATO",
        "ZYDUSLIFE"
    ]
)