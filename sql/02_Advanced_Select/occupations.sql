/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.

- occupations
    name : String
    occupation : String

Sample Output
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria

Explanation
The first column is an alphabetically ordered list of Doctor names.

Pivot table : Rotate rows to columns
*/

WITH tb AS (
    SELECT 
        CASE WHEN occupation = 'Doctor' THEN @rD := @rD +1
             WHEN occupation = 'Professor' THEN @rP := @rP + 1
             WHEN occupation = 'Singer' THEN @rS := @rS + 1 
             WHEN occupation = 'Actor' THEN @rA := @rA + 1 
             END row_idx,
        CASE WHEN occupation = 'Doctor' THEN name END Doctor,
        CASE WHEN occupation = 'Professor' THEN name END Professor,
        CASE WHEN occupation = 'Singer' THEN name END Singer,
        CASE WHEN occupation = 'Actor' THEN name END Actor
    FROM occupations,
        (SELECT @rD:=0, @rP:=0, @rS:=0, @rA:=0) r
    ORDER BY name)
SELECT MAX(Doctor), MAX(Professor), MAX(Singer), MAX(Actor)
FROM tb
GROUP BY row_idx;

-- OR 

SET @rD:=0, @rP:=0, @rS:=0, @rA:=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM (
    SELECT 
        CASE WHEN occupation = 'Doctor' THEN @rD := @rD +1
             WHEN occupation = 'Professor' THEN @rP := @rP + 1
             WHEN occupation = 'Singer' THEN @rS := @rS + 1 
             WHEN occupation = 'Actor' THEN @rA := @rA + 1 
             END row_idx,
        CASE WHEN occupation = 'Doctor' THEN name END Doctor,
        CASE WHEN occupation = 'Professor' THEN name END Professor,
        CASE WHEN occupation = 'Singer' THEN name END Singer,
        CASE WHEN occupation = 'Actor' THEN name END Actor
    FROM occupations
    ORDER BY name
) tb
GROUP BY row_idx;