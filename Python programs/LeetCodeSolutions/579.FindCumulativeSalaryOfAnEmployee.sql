"""
579. Find Cumulative Salary of an Employee (SQL)
Difficulty: Hard

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| month       | int  |
| salary      | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to report the cumulative salary of an employee over each month. The result should have columns id, month, and cumulative_salary.

Example:
Employee table:
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 1  | 1     | 1000   |
| 1  | 2     | 2000   |
| 2  | 1     | 700    |
| 2  | 2     | 600    |
+----+-------+--------+

Result table:
+----+-------+------------------+
| id | month | cumulative_salary|
+----+-------+------------------+
| 1  | 1     | 1000             |
| 1  | 2     | 3000             |
| 2  | 1     | 700              |
| 2  | 2     | 1300             |
+----+-------+------------------+

SQL Solution:
SELECT id, month, SUM(salary) OVER (PARTITION BY id ORDER BY month) AS cumulative_salary
FROM Employee;
