"""
LeetCode 1965. Employees With Missing Information

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| employee_id | int   |
| name        | varchar|
+-------------+-------+
employee_id is the primary key for this table.

Table: Salaries
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| employee_id | int   |
| salary      | int   |
+-------------+-------+
employee_id is the primary key for this table.

Write an SQL query to report the IDs of employees missing information.

Example:
Employees table:
| employee_id | name    |
|-------------|---------|
| 2           | Crew    |
| 4           | Haven   |
| 5           | Kristian|

Salaries table:
| employee_id | salary |
|-------------|--------|
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |

Output:
| employee_id |
|-------------|
| 1           |
| 2           |
| 5           |
"""

-- SQL Solution
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
