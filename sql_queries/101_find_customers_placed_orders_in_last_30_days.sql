--Find customers who placed order in last 30 days
SELECT DISTINCT customers_id, customer_name
FROM Orders
WHERE order_date >= CURRENT_DATE - INTERVAL 30 DAYS;