--Problems's URL(https://leetcode.com/problems/sales-analysis-iii/description/)
SELECT Product.product_id, Product.product_name
FROM Product
LEFT JOIN Sales
ON Product.product_id=Sales.product_id
GROUP BY Product.product_id
HAVING (Sales.sale_date)>0 AND 
COUNT(*)= COUNT(*) FILTER(WHERE Sales.sale_date BETWEEN '2019-01-01' AND '2019-03-31')