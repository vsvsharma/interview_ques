-- Find the employee who is earning more than the average salary of the company
SELECT emp_id, name, salary
FROM employees
WHERE salary > (
    SELECT avg(salary)
    FROM employees
) 