--Problem's URL(https://leetcode.com/problems/biggest-single-number/)
SELECT num 
FROM MyNumbers
GROUP BY num
HAVING COUNT(num)=1
ORDER BY MAX(num) DESC
LIMIT 1;