--Problems URL(https://www.hackerrank.com/challenges/weather-observation-station-6/problem)

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY,1)) IN ('a','e','i','o','u')

--another approach
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]';

--another approach. In this substring is used to extract the first letter of the word.
SELECT CITY
FROM STATION
WHERE  LOWER(SUBSTRING(CITY, 1, 1)) IN ('a', 'e', 'i', 'o', 'u');
--CITY: This is the column from which you want to extract characters.
--1: This is the starting position from which the substring extraction begins. 
--In this case, it's the first character of the city name.
--1: This is the length of the substring to be extracted.
--Here, it's 1, so it only extracts one character.
