-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Top 10 ROE companies
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- 3. Top 10 ROCE companies
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- 4. Highest net profit
SELECT company_id, year, net_profit
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 10;

-- 5. Highest sales
SELECT company_id, year, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;

-- 6. Companies by sector
SELECT broad_sector, COUNT(*) AS company_count
FROM sectors
GROUP BY broad_sector
ORDER BY company_count DESC;

-- 7. Market cap leaders
SELECT company_id, market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC
LIMIT 10;

-- 8. Stock price records count
SELECT company_id, COUNT(*) AS price_records
FROM stock_prices
GROUP BY company_id
ORDER BY price_records DESC;

-- 9. Peer group distribution
SELECT peer_group_name, COUNT(*) AS members
FROM peer_groups
GROUP BY peer_group_name
ORDER BY members DESC;

-- 10. Financial ratio coverage
SELECT COUNT(*) AS ratio_records
FROM financial_ratios;
