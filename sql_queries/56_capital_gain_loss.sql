--Problems URL(https://leetcode.com/problems/capital-gainloss/description/)
-- Write your PostgreSQL query statement below
WITH StockData AS (
  SELECT
    stock_name,
    operation,
    operation_day,
    price,
    LAG(price) OVER (PARTITION BY stock_name ORDER BY operation_day) AS prev_price
  FROM
    Stocks
)
SELECT
  stock_name,
  SUM(CASE
        WHEN operation = 'Sell' THEN price - prev_price
        ELSE 0
      END) AS capital_gain_loss
FROM
  StockData
GROUP BY
  stock_name
HAVING
  SUM(CASE WHEN operation = 'Buy' THEN 1 ELSE 0 END) > 0; 
