--Problems URl(https://leetcode.com/problems/patients-with-a-condition/description/)
SELECT *
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'