/*
Query the difference between the maximum and minimum populations in CITY.

-city
    id : number
    name : string
    countrycode : string
    district : string
    population : string
*/

SELECT MAX(population)-MIN(population)
FROM city;