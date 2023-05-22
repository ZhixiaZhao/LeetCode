# Write your MySQL query statement below
SELECT max(salary) AS SecondHighestSalary
FROM (SELECT salary, DENSE_RANK () over (ORDER BY salary desc) AS rd
     FROM Employee) e
where rd = 2

