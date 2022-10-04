/*
We define an employee's total earnings to be their monthly salary*months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. 
Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

-employee
    employee_id : integer
    name : string
    months : integer
    salary : integer

Sample Output
69952 1

Explanation
print the maximum earnings value (69952) and a count of the number of employees who have earned(which is 1) as two space-separated values.
*/

SELECT salary*months, COUNT(*)
FROM employee
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;