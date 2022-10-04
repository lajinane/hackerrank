/*
Consider P1(a,c) and P2(b,d) to be two points on a 2D plane 
where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) 
and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points P1 and P2 and format your answer to display  decimal digits.

https://en.wikipedia.org/wiki/Euclidean_distance

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

WITH t AS (
    SELECT MIN(lat_n) a, MAX(lat_n) b, MIN(long_w) c, MAX(long_w) d
    FROM station
)
SELECT ROUND(SQRT(POW(b-a,2)+POW(d-c,2)), 4) euclidean_distance
FROM t;

--OR

SELECT ROUND(SQRT(POW(MAX(lat_n)-MIN(lat_n),2)+POW(MAX(long_w)-MIN(long_w),2)), 4) euclidean_distance
FROM station;
