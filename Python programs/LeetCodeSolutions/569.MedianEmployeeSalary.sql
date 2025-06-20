"""
569. Median Employee Salary (SQL)
Difficulty: Hard

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| salary      | int  |
+-------------+------+
id is the primary key for this table.
Each row of this table contains information about the salary of an employee.

Write an SQL query to report the median salary of each company. If the median salary is not an integer, report the nearest integer (round up).

Example:
Employee table:
+----+-------+--------+
| id | name  | salary |
+----+-------+--------+
| 1  | Joe   | 70000  |
| 2  | Henry | 80000  |
| 3  | Sam   | 60000  |
| 4  | Max   | 90000  |
+----+-------+--------+

Result table:
+--------+
| median |
+--------+
| 75000  |
+--------+
"""
-- SQL Solution:
SELECT ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) OVER (), 0) AS median
FROM Employee
LIMIT 1;
