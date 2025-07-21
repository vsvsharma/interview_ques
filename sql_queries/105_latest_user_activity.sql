-- Your user_activity_log table contains multiple rows per user. 
-- You need to keep only the latest activity per user based on activity_timestamp.

SELECT user_id, activity_type, activity_timestamp
FROM (
    SELECT * , ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_timestamp DESC) as rnk
    FROM user_activity_log
) as sub
WHERE rnk=1;