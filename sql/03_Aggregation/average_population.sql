/*
Query the average population for all cities in CITY, rounded down to the nearest integer.
Note

-city
    id : number
    name : string
    countrycode : string
    district : string
    population : string
*/

-- CEIL()  : rounds UP 
-- FLOOR() : rounds DOWN

SELECT FLOOR(AVG(population))
FROM city;
