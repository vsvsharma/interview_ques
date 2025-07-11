--Find the second highest salary in the department
SELECT salary
FROM (
    SELECT salary, RANK() OVER (ORDER BY salary DESC) as rnk
    FROM employees
) t
WHERE rnk=2;