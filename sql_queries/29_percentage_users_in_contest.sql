--Problems URL(https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/)
SELECT
    contest_id,
    ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM Register) , 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;
