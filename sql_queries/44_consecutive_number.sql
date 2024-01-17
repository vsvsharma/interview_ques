--Problems URL(https://leetcode.com/problems/consecutive-numbers/description/)
WITH ConsecutiveGroup AS(
    SELECT num,
    LEAD(num) OVER (ORDER BY id) AS next_num,
    LAG(num) OVER (ORDER BY id) AS prev_num
    FROM logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM ConsecutiveGroup
WHERE num=next_num AND num=prev_num