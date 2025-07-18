"""
1075. Project Employees I (SQL)

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

Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 decimal places.

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
+-------------+--------------------+
| project_id  | average_years      |
+-------------+--------------------+
| 1           | 2.00               |
| 2           | 2.50               |
+-------------+--------------------+
"""
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN ProjectEmployee pe ON p.project_id = pe.project_id
JOIN Employee e ON pe.employee_id = e.employee_id
GROUP BY p.project_id;
