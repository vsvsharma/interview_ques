--Problems URL(https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/)
SELECT teacher_id, COUNT(DISTINCT subject_id)
FROM Teacher
ORDER BY teacher_id