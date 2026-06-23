PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_logo TEXT,
    company_name TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
);

CREATE TABLE IF NOT EXISTS profitandloss (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    opm_percentage REAL,
    other_income REAL,
    interest REAL,
    depreciation REAL,
    profit_before_tax REAL,
    tax_percentage REAL,
    net_profit REAL,
    eps REAL,
    dividend_payout REAL,

    FOREIGN KEY(company_id)
    REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS balancesheet (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,

    FOREIGN KEY(company_id)
    REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS cashflow (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,

    FOREIGN KEY(company_id)
    REFERENCES companies(id)
);