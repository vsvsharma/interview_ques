/*
For each department, show how each employee's salary compares to the previous hire in terms of difference.
*/
SELECT emp_id, department_id, emp_name, salary, hire_date, LAG(salary) OVER (PARTITON BY department_id
    ORDER BY hire_date) AS prev_salary, salary - LAG(salary) OVER (PARTITION BY department_id 
    ORDER BY hire_date) AS salary_difference
FROM employee_salaries
ORDER BY department_id, hire_date;
