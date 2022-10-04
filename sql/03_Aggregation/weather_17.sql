/*
Query the Western Longitude (LONG_W) where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER
*/

-- returns first matching row
SELECT ROUND(LONG_W,4)
FROM STATION 
WHERE LAT_N > 38.7780
ORDER BY LAT_N ASC
LIMIT 1

-- OR
-- returns all matching rows
SELECT ROUND(LONG_W,4)
FROM STATION 
WHERE LAT_N = (
    SELECT MIN(LAT_N)
    FROM STATION
    WHERE LAT_N > 38.7780
)
ORDER BY 1