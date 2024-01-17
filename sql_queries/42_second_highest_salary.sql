--Problems URL(https://leetcode.com/problems/second-highest-salary/description/)
SELECT COALESCE(
    (SELECT DISTINCT salary
    FROM Employees
    ORDER BY salary
    LIMIT 1 OFFSET 1), NULL
) AS SecondHighestSalary