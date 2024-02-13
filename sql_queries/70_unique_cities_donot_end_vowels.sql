--Problems URL(https://www.hackerrank.com/challenges/weather-observation-station-10/problem)

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(SUBSTRING(CITY FROM LENGTH(CITY) FOR 1)) NOT IN ('a','e','i','o','u');