--Find the revenue per region per month
SELECT region, FORMAT_DATE('%Y-%m', order_date) AS month, 
    AVG(revenue) AS monthly_revenue
FROM order
GROUP BY region, month