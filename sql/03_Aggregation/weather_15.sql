/*
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

-- returns first matching row
SELECT ROUND(long_w,4)
FROM station 
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1;

-- OR
-- returns all matching rows
SELECT ROUND(long_w,4)
FROM station 
WHERE lat_n = (
    SELECT MAX(lat_n)
    FROM station
    WHERE lat_n < 137.2345
)
ORDER BY 1;
