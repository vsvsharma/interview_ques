--Problems URL(https://leetcode.com/problems/find-followers-count/submissions/1143531982/)
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id 
ORDER BY user_id ASC