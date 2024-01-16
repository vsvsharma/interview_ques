--Problems URL(https://leetcode.com/problems/the-latest-login-in-2020/description/)
SELECT user_id,MAX(time_stamp) AS last_login
FROM logins
WHERE EXTRACT(YEAR FROM time_stamp)=2020
GROUP BY user_id