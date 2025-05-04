/*
Problem: Show all customers(even they haven't ordered), and the date of their latest order
Tables: customers,orders
I am using left join here because i want to include customers with no orders also
*/
SELECT c.customer_name, MAX(o.order_date) AS lastest_order
FROM customers 
LEFT JOIN orders o 
ON c.customer_id=o.customer_id
GROUP BY c.customer_name;