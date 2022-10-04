/*
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

SELECT COUNT(city) - COUNT(DISTINCT city) 
FROM station;