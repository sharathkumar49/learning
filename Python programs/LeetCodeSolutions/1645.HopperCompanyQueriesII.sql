"""
LeetCode 1645. Hopper Company Queries II

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| salary      | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to report the names of employees with the highest salary.

Example:
Input:
Employees table:
| id | name  | salary |
|----|-------|--------|
| 1  | Alice | 60000  |
| 2  | Bob   | 40000  |
Output:
| name  |
|-------|
| Alice |
"""

-- SQL Query:
SELECT name
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);
