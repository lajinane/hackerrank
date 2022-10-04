/*
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

-city
    id : NUMBER
    name : VARCHAR2 (17)
    countrycode VARCHAR2 (3)
    district : VARCHAR2 (20)
    population : NUMBER

-country
    code : VARCHAR2(3)
    name : VARCHAR2 (44)
    continent : VARCHAR2 (13)
    region : VARCHAR2 (25)
    surfacearea : NUMBER
    indepyear : VARCHAR2 (5)
    population : NUMBER
    lifeexpectancy : VARCHAR2 ( 4)
    gnp : NUMBER
    gnpold : VARCHAR2 (9)
    localname : VARCHAR2 (44)
    governmentform : VARCHAR2 ( 44)
    headofstate : VARCHAR2 (32)
    capital : VARCHAR2 (4)
    code2 : VARCHAR2 (2)

Note: city.countrycode and country.code are matching key columns.
*/

SELECT SUM(city.population)
FROM city
JOIN country 
    ON city.countrycode = country.code
WHERE country.continent = 'Asia';