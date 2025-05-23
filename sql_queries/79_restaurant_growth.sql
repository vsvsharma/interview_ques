-- Problem Link: https://leetcode.com/problems/restaurant-growth/description/

WITH cte AS
(SELECT visited_on, SUM(amount) AS total_amount  
FROM Customer
GROUP BY visited_on),

cte2 AS
(SELECT visited_on, SUM(total_amount) OVER (ORDER BY visited_on ROWS 
BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
ROUND (AVG(total_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING 
AND CURRENT ROW),2 ) AS average_amount
FROM cte)

SELECT * 
FROM cte2
WHERE visited_on >= (SELECT visited_on FROM cte2 
ORDER BY visited_on LIMIT 1) + 6
ORDER BY visited_on