--Problems URL(https://leetcode.com/problems/exchange-seats/description/)
SELECT
    id,
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN LEAD(student) OVER (ORDER BY id)
        WHEN id % 2 = 0 THEN LAG(student) OVER (ORDER BY id)
        ELSE student
    END AS student
FROM Seat
ORDER BY id;