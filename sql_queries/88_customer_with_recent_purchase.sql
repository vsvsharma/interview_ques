--Problem: You work in e-commerce. The product team want to see each customer's most recent order
WITH ranked_orders AS(
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id, ORDER BY order_date DESC) AS rn
    FROM orders
)
SELECT * 
FROM ranked_orders
WHERE rn=1;