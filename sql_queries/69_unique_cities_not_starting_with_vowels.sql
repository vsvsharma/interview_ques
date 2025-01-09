--Problems URL(https://www.hackerrank.com/challenges/weather-observation-station-9/problem)

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(FROM 1 FOR 1)) NOT IN ('a','e','i','o','u');