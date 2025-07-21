--Count the highest and the lowest salary in the department
SELECT dept_id, MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
FROM employees
GROUP BY dept_id