--Problems URL(https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/)
SELECT e1.employee_id, e1.name, COUNT(e2.reports_to) AS reports_count, ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2
ON e1.employee_id=e2.reports_to
GROUP BY e1.employee_id,e1.name
ORDER BY e1.employee_id