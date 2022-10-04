/*
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
The STATION table is described as follows:

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT DISTINCT city
FROM station
WHERE MOD(id,2) = 0;

-- OR

SELECT DISTINCT city
FROM station
WHERE id % 2 = 0;


