-- Porblem's URL(https://leetcode.com/problems/customers-who-never-order/)
SELECT Customers.name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id=Orders.customerId
WHERE Orders.customerId IS NULL