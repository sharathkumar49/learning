"""
1076. Project Employees II (SQL)

Table: Project
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
+-------------+---------+
project_id is the primary key for this table.

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| experience_years | int |
+-------------+---------+
employee_id is the primary key for this table.

Table: ProjectEmployee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key for this table.

Write an SQL query that reports the employees who are working on all the projects.

Example:
Input:
Project table:
+-------------+
| project_id  |
+-------------+
| 1           |
| 2           |
+-------------+
Employee table:
+-------------+---------+------------------+
| employee_id | name    | experience_years |
+-------------+---------+------------------+
| 1           | Khaled  | 3                |
| 2           | Ali     | 2                |
| 3           | John    | 1                |
+-------------+---------+------------------+
ProjectEmployee table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 2           |
+-------------+-------------+
Output:
+-------------+
| employee_id |
+-------------+
| 1           |
+-------------+
"""
SELECT employee_id
FROM ProjectEmployee
GROUP BY employee_id
HAVING COUNT(DISTINCT project_id) = (SELECT COUNT(*) FROM Project);
