"""
LeetCode 1939. Net Salary

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| emp_id      | int   |
| salary      | int   |
| tax         | int   |
+-------------+-------+
emp_id is the primary key for this table.

Write an SQL query to find the net salary for each employee.

Example:
Employees table:
| emp_id | salary | tax |
|--------|--------|-----|
| 1      | 1000   | 100 |
| 2      | 2000   | 200 |

Output:
| emp_id | net_salary |
|--------|------------|
| 1      | 900        |
| 2      | 1800       |
"""

-- SQL Solution
SELECT emp_id, salary - tax AS net_salary
FROM Employees;
