--Problem's URL(https://leetcode.com/problems/not-boring-movies/description/)
SELECT id, movie, description,rating
FROM Cinema
WHERE id %2 <> 0 AND description <> 'boring'
ORDER BY rating desc