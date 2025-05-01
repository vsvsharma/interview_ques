/*
Problem: Using window functions, write a SQL query to find the top 2 highest-value orders placed by
each customer. Ensure that if multiple orders have the same amount, they receive the same rank, and the
next rank is skipped accordingly.
*/

WITH ranked_orders AS
    (SELECT customer_id, order_id, Order_date, order_amount, RANK() OVER (PARTITION BY customer_id 
    ORDER BY order_amount DESC) AS order_rank
    FROM orders)
SELECT * 
FROM ranked_orders
WHERE order_rank<=2
ORDER BY customer_id, order_rank
