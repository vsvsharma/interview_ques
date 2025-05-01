-- Problem: Find the most recently hired Employee from each department
WITH recent_join AS(
    SELECT *, ROW_NUMBER() OVER(PARTITION BY department_id ORDER  BY hire_date DESC) AS rn
    FROM employee
)
SELECT * 
FROM recent_join
WHERE rn=1;