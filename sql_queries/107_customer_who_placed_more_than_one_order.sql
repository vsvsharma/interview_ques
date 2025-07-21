-- Using CTE find the customer who placed more than one order 

WITH OrderCounts AS(
    SELECT customer_id, COUNT(*) AS total_orders
    FROM Orders 
    GROUP BY customer_id
)
SELECT customer_id, total_orders
FROM OrderCounts
WHERE total_orders > 1; 