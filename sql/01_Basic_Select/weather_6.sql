/*
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT DISTINCT city
FROM station 
WHERE city RLIKE '^[aeiou]';

-- OR

SELECT DISTINCT city
FROM station 
WHERE city REGEXP '^[aeiou]';

-- OR

SELECT DISTINCT city
FROM station 
WHERE SUBSTR(city, 1, 1) IN ('a', 'e', 'i', 'o', 'u');