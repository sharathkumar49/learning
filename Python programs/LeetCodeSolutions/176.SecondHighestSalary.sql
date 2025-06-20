"""
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

SQL Schema:
Employee table: id, salary

Write a SQL query to get the second highest salary from the Employee table. If there is no second highest salary, the query should return null.

Example:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""
-- SQL Solution
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
