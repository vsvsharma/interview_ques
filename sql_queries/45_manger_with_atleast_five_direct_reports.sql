--Problems URL(https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/)
SELECT M.name
FROM Employee M
JOIN Employee R
ON M.id=R.managerId
GROUP BY M.id,M.name
HAVING COUNT(R.id)>=5