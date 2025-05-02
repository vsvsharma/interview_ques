/*
Problem: Identify companies which have more than 5 open roles
Tables: companies, job_posting
I'm using Inner Join because i only want companies with open jobs
*/
SELECT c.company_name, COUNT(j.job_id) AS open_roles
FROM companies c
JOIN job_posting j
ON c.company_id=j.company_id
WHERE j.status='open'
GROUP BY company_name
HAVING COUNT(j.job_id)>5;