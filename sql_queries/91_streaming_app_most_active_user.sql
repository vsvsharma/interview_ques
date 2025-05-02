/*
Problem: Find the top 3 users per week by watch hours
There is only one table that is watch_logs
*/
SELECT * 
FROM (SELECT user_id, watch_week, hours_watched, RANK() OVER(PARTITION BY watch_week ORDER BY hours_watched)
    AS rnk FROM watch_logs) AS ranked
WHERE rnk<=3;