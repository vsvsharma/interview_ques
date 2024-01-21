--Problems URL(https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/)
WITH FriendsCount AS (
    SELECT id, COUNT(*) AS num
    FROM (
        SELECT requester_id AS id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS id FROM RequestAccepted
    ) AS FriendIds
    GROUP BY id
)

SELECT id, num
FROM FriendsCount
WHERE num = (SELECT MAX(num) FROM FriendsCount);