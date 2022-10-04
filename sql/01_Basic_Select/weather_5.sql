/* 
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
The STATION table is described as follows: 

-station
    id : NUMBER
    city : VARCHAR2 (21)
    state : VARCHAR2 (2)
    lat_n : NUMBER
    long_w : NUMBER

Note
You can write two separate queries to get the desired output. It need not be a single query.
*/

(   
    SELECT city, LENGTH(city)
    FROM station 
    ORDER BY LENGTH(city) ASC, city ASC 
    LIMIT 1
) UNION (
    SELECT city, LENGTH(city)
    FROM station 
    ORDER BY LENGTH(city) DESC, city ASC 
    LIMIT 1
);