"""
LeetCode 1873. Calculate Special Bonus

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| employee_id | int   |
| name        | varchar|
| salary      | int   |
+-------------+-------+
employee_id is the primary key for this table.

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if their employee_id is an odd number and their name does not start with 'M', otherwise the bonus is 0.

Example:
Employees table:
| employee_id | name    | salary |
|-------------|---------|--------|
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |

Output:
| employee_id | bonus |
|-------------|-------|
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
"""

-- SQL Solution
SELECT employee_id, 
       CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM Employees;
