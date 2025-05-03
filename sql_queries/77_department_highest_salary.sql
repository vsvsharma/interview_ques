--Problem Link: https://leetcode.com/problems/department-highest-salary/description/
WITH cte AS
(SELECT e.name AS Employee, e.salary AS d.name AS Department, 
    MAX(e.salary) OVER(PARTITION BY e.departmentId) AS max_salary
FROM Employee e
LEFT JOIN Department d 
ON e.departmentId=d.id)

SELECT Department, Employee, Salary
FROM cte
WHERE Salary=max_salary