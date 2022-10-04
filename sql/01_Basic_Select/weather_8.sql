/*
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT DISTINCT city
FROM station 
WHERE city RLIKE '^[aeiou].*[aeiou]$';

-- OR

SELECT DISTINCT city
FROM station 
WHERE city REGEXP '^[aeiou].*[aeiou]$';




