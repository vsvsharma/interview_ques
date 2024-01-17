--Problems URL(https://leetcode.com/problems/employees-whose-manager-left-the-company/description/)
WITH cte AS(
    SELECT employee_id
    FROM Employees
    WHERE salary < 30000
)
SELECT employee_id
FROM cte
WHERE manger_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id