-- select the maxium salary for male and female in the department

SELECT dept_id,
    MAX(CASE WHEN gender='M' THEN salary) AS male_salary
    MAX(CASE WHEN gender='F' THEN salary) AS female_salary
FROM employees
GROUP BY dept_id