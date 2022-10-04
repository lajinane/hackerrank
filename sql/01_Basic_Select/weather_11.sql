/*
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT DISTINCT city
FROM station
WHERE city NOT RLIKE '^[aeiou].*[aeiou]$';

-- OR

SELECT DISTINCT city
FROM station 
WHERE city NOT REGEXP '^[aeiou].*[aeiou]$';