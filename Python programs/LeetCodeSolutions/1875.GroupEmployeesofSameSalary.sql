"""
LeetCode 1875. Group Employees of Same Salary

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| employee_id | int   |
| name        | varchar|
| salary      | int   |
+-------------+-------+
employee_id is the primary key for this table.

Write an SQL query to group employees with the same salary.

Example:
Employees table:
| employee_id | name    | salary |
|-------------|---------|--------|
| 1           | Alice   | 1000   |
| 2           | Bob     | 1000   |
| 3           | Charlie | 2000   |

Output:
| salary | employees      |
|--------|---------------|
| 1000   | Alice,Bob     |
| 2000   | Charlie       |
"""

-- SQL Solution
SELECT salary, GROUP_CONCAT(name ORDER BY name) AS employees
FROM Employees
GROUP BY salary;
