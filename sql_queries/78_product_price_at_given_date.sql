--Problem Link: https://leetcode.com/problems/product-price-at-a-given-date/description/
WITH cte AS
(SELECT *, RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS r
FROM Products
WHERE change_date <= '2019-08-16')

SELECT product_id, new_price AS price
FROM cte
WHERE r=1

UNION 

SELECT product_id, 10 AS price
FROM Products NOT IN (SELECT product_id FROM cte)