/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT DISTINCT city
FROM station 
WHERE city RLIKE '[aeiou]$';

-- OR

SELECT DISTINCT city
FROM station 
WHERE city REGEXP '[aeiou]$';



