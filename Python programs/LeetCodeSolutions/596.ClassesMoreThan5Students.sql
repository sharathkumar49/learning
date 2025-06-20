"""
596. Classes More Than 5 Students (SQL)
Difficulty: Easy

Table: Courses
+-------------+------+
| Column Name | Type |
+-------------+------+
| student     | varchar |
| class       | varchar |
+-------------+------+
(student, class) is the primary key for this table.

Write an SQL query to report all the classes that have more than or equal to 5 students.

Example:
Courses table:
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
+---------+------------+

Result table:
+---------+
| class   |
+---------+
| Math    |
+---------+

SQL Solution:
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
