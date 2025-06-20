"""
1077. Project Employees III (SQL)

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

Write an SQL query that reports the project_id, employee_id, and the number of projects the employee has participated in, for every employee who has participated in at least one project.

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
+-------------+-------------+----------------+
| project_id  | employee_id | projects_count |
+-------------+-------------+----------------+
| 1           | 1           | 2              |
| 1           | 2           | 2              |
| 1           | 3           | 1              |
| 2           | 1           | 2              |
| 2           | 2           | 2              |
+-------------+-------------+----------------+
"""
SELECT pe.project_id, pe.employee_id, (
    SELECT COUNT(DISTINCT project_id)
    FROM ProjectEmployee pe2
    WHERE pe2.employee_id = pe.employee_id
) AS projects_count
FROM ProjectEmployee pe;
