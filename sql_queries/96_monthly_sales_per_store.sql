/*
Problem: Show total sales per store for a given month, including stores with no sales
Tables:stores,sales
I am using left join here because i want to include all stores which are having zero sales also
*/
SELECT s.store_name, SUM(sales.amount) AS total_sales
FROM stores s
LEFT JOIN sales
ON s.store_id=sales.store_id
AND sales.sale_date BETWEEN '2025-01-01' AND '2025-01-31'
GROUP BY s.store_name;