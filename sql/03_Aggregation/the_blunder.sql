/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), and round it up to the next integer.

Note: Salary is per month.

-employees
    id : integer
    name : string
    salary : integer

Sample Input
id      name        salary
1       Kristeen    1420    => 142
2       Ashley      2006    => 26
3       Julia       2210    => 221
4       Maria       3000    => 3

Sample Output
2061

Explanation
Samantha computes an average salary of 98. The actual average salary is 2159.
2159.00 - 98.00 = 2061.00
*/

SELECT CEIL(AVG(salary)-AVG(REPLACE(salary, '0','')))
FROM employees;