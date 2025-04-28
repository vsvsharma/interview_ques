--Problem Link: https://leetcode.com/problems/confirmation-rate/description/
SELECT s.user_id CASE WHEN COUNT(c.time_stamp)=0
THEN 0.00
ELSE ROUND(SUM(CASE WHEN c.action='confirmed' THEN 1 ELSE 0 END )*1.0/COUNT(*),2)
END confirmation_rate
FROM Signup s
LEFT JOIN Confirmation 
ON s.user_id=c.user_id
GROUP BY s.user_id