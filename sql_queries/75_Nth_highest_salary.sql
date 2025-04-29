--Problem Link: https://leetcode.com/problems/nth-highest-salary/description/
WITH cte AS
    (SELECT *, DENSE_RANK() OVER (ORDER BY Salary DESC ) AS RNK
    FROM Employee)

    SELECT DISTINCT IFNULL(Salary,null)
    FROM cte
    WHERE RNK=N