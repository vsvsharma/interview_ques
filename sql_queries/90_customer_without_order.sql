/*Problem: Find the users who signed up but never placed an order
There are 2 tables: customers, orders. So I'm using left join because i want customers who didn't
appeared in the orders table
*/
SELECT c.customer_id, c.name
FROM customers c 
LEFT JOIN order o
ON c.customer_id=o.customer_id
WHERE o.customer_id IS NULL;