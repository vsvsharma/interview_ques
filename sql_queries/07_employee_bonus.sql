--Problem's URL(https://leetcode.com/problems/employee-bonus/description/)
SELECT Employee.name, Bonus.bonus 
FROM Employee
LEFT JOIN Bonus
ON Employee.empId=Bonus.empId
WHERE Bonus.bonus<=500 OR Bonus.bonus IS NULL