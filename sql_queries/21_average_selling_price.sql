--Porblem's URL(https://leetcode.com/problems/average-selling-price/description/)
WITH ProductSales AS (
  SELECT
    p.product_id,
    SUM(u.units * p.price) AS total_price,
    SUM(u.units) AS total_units
  FROM Prices p
  LEFT JOIN UnitsSold u ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
  GROUP BY p.product_id
)

SELECT
  product_id,
  CASE
    WHEN total_units > 0 THEN ROUND(CAST(total_price AS DECIMAL(10, 2)) / total_units, 2)
    ELSE 0
  END AS average_price
FROM ProductSales;
