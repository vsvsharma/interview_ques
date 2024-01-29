--Problems URL(https://www.hackerrank.com/challenges/what-type-of-triangle/problem)
SELECT CASE
WHEN A+B<=c OR C+B<=A OR C+A<=B THEN 'Not A Triangle'
WHEN A=B && B=C THEN 'Equilateral'
WHEN A=B OR B=C OR A=C THEN 'Isosceles'
ELSE 'Scalene'
END AS triangle_type
FROM TRIANGLES