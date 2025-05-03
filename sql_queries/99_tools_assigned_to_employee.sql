/*
Problem: Show all tools available, even if no employee is assigned to them
Tables: employee, tools
I am using right join here because main dataset is on right and i want all rows either it is 
assigned to employee or not.
*/
SELECT t.tool_name, e.employee_name
FROM employees e
RIGHT JOIN tools t 
ON e.tool_id=t.tool_id; 