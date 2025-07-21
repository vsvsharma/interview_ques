--Count no. of orders per customer
SELECT customers_id, COUNT(*) AS no_of_orders
FROM orders
GROUP BY customers_id