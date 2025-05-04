/*
Problem: Rank the top 3 courses by number of students per category
Tables: courses, enrollments
I am using inner join here because i want to include courses with enrollments...left join would include
courses with no enrollments also
*/
SELECT * 
FROM (
        SELECT c.course_name,c.category, COUNT(e.student_id) AS enrollments,
        RANK() OVER(PARTITION BY c.category ORDER BY COUNT(e.student_id) DESC) AS rnk
        FROM courses c
        JOIN enrollments e ON c.course_id=e.course_id
        GROUP BY c.course_name, c.category
) AS ranked
WHERE rnk<=3;