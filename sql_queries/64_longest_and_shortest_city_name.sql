--Problems URL(https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

--For shortest city
SELECT CITY, LENGTH(CITY) AS Name_difference
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1;

--For longest city
SELECT CITY, LENGTH(CITY) AS Name_difference
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1;