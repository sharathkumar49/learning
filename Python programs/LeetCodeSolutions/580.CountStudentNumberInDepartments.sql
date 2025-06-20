"""
580. Count Student Number in Departments (SQL)
Difficulty: Medium

Table: Student
+-------------+------+
| Column Name | Type |
+-------------+------+
| student_id  | int  |
| department  | varchar |
+-------------+------+
student_id is the primary key for this table.

Write an SQL query to report the number of students in each department.

Example:
Student table:
+------------+-------------+
| student_id | department  |
+------------+-------------+
| 1          | Engineering |
| 2          | Science     |
| 3          | Engineering |
+------------+-------------+

Result table:
+-------------+----------------+
| department  | student_number |
+-------------+----------------+
| Engineering | 2              |
| Science     | 1              |
+-------------+----------------+

SQL Solution:
SELECT department, COUNT(*) AS student_number
FROM Student
GROUP BY department;
