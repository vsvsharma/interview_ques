/*
Problem: Show Students whose grades are above average in their department
Tables: students, grades, departments
I am using inner join because i want to include students who have grades and that are linked to valid
department
*/
SELECT s.student_name, g.grade, d.department_name, 
    AVG(g.grade) OVER(PARTITION BY d.department_id) AS dept_avg, 
    CASE WHEN g.grade > AVG(g.grade) OVER(PARTITION BY d.department_id) THEN 
    'Above Avg' ELSE 'Below Avg' END AS performance
FROM students s
JOIN grades g ON s.student_id=g.student_id
JOIN department d ON s.department_id= d.department_id;

