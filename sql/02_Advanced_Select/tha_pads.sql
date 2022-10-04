/*
Generate the following two result sets:

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).

Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
There are a total of [occupation_count] [occupation]s.

- occupations
    name : String
    occupation : String

Sample Output
Ashely(P)
Christeen(P)
Jane(A)
Jenny(D)
Julia(A)
Ketty(P)
Maria(A)
Meera(S)
Priya(S)
Samantha(D)
There are a total of 2 doctors.
There are a total of 2 singers.
There are a total of 3 actors.
There are a total of 3 professors.

*/

SELECT CONCAT(name,'(', UPPER(LEFT(occupation, 1)), ')')
FROM occupations
ORDER BY name;

SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation),'s.')
FROM occupations
GROUP BY occupation
ORDER by Count(occupation);
