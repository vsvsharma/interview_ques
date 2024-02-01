--Problems URL(https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/)
SELECT
    person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn ASC) AS total_weight
    FROM
        Queue
) AS subquery
WHERE
    total_weight <= 1000
ORDER BY
    total_weight DESC
LIMIT 1;