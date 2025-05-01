--Find the latest(most recent) order placed by each customer

WITH recent_orders AS(
    SELECT * , ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM orders
)

SELECT * 
FROM recent_orders
WHERE rn=1;