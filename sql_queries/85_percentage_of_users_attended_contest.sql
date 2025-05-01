-- Problem Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/
SELECT contest_id, ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM Users)*100,2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id