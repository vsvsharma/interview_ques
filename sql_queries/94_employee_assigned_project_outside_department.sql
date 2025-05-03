/*
Problem: Find the employees who are working on projects not related to their own departmnet
Tables: employees, projects
I'm using inner join here because i only want employees assigned to projects. so inner join filter
whose project_dept not equal to dept_id
*/
SELECT e.emp_name, p.project_name
FROM employees e
INNER JOIN project p
ON e.emp_id=p.emp_id
WHERE e.dept_id != p.project_dept_id