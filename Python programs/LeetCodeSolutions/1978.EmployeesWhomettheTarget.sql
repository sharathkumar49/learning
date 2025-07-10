"""
LeetCode 1978. Employees Who Met the Target

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| employee_id | int   |
| name        | varchar|
| hours       | int   |
+-------------+-------+
employee_id is the primary key for this table.

Write an SQL query to report the IDs of employees who met the target hours.

Example:
Employees table:
| employee_id | name    | hours |
|-------------|---------|-------|
| 1           | Alice   | 5     |
| 2           | Bob     | 3     |
| 3           | Charlie | 8     |

Output:
| employee_id |
|-------------|
| 1           |
| 3           |
"""

-- SQL Solution
SELECT employee_id
FROM Employees
WHERE hours >= 5;
