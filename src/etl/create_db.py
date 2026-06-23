import sqlite3
import pandas as pd

# Connect to database

conn = sqlite3.connect("db/nifty100.db")

# Load companies data

companies = pd.read_excel(
"data/raw/companies.xlsx",
header=1
)

# Load into SQLite

companies.to_sql(
"companies",
conn,
if_exists="append",
index=False
)

print(f"✅ Loaded {len(companies)} companies")

conn.close()
companies = pd.read_excel("data/raw/companies.xlsx", header=1)

companies.to_sql(
    "companies",
    conn,
    if_exists="append",
    index=False
)