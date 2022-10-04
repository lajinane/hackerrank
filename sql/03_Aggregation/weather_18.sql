/*
Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.

- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).

Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.

https://xlinux.nist.gov/dads/HTML/manhattanDistance.html

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

WITH t AS (
    SELECT MIN(lat_n) a, MIN(long_w) b, MAX(lat_n) c, MAX(long_w) d
    FROM station
)
SELECT ROUND(ABS(c-a)+ABS(d-b), 4) manhattan_distance
FROM t;

--OR

SELECT ROUND(ABS(MAX(lat_n)-MIN(lat_n))+ABS(MAX(long_w)-MIN(long_w)), 4) manhattan_distance
FROM station;

