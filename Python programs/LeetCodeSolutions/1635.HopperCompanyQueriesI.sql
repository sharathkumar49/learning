"""
LeetCode 1635. Hopper Company Queries I

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| salary      | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to report the names of employees with a salary greater than 50000.

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
WHERE salary > 50000;
