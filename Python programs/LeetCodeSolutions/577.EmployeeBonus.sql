"""
577. Employee Bonus (SQL)
Difficulty: Easy

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| name        | varchar |
| supervisor  | int  |
| salary      | int  |
+-------------+------+
empId is the primary key for this table.
supervisor is the id of the supervisor.

Table: Bonus
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the primary key for this table.

Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.

Example:
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+

Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+

Result table:
+------+-------+
| name | bonus |
+------+-------+
| Dan  | 500   |
+------+-------+

SQL Solution:
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
