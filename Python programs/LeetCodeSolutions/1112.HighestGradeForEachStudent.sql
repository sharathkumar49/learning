"""
1112. Highest Grade For Each Student (SQL)

Table: Enrollments
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| course_id   | int     |
| grade       | int     |
+-------------+---------+
(student_id, course_id) is the primary key.

Write an SQL query to find the highest grade for each student. Return the result table ordered by student_id.

"""
SELECT student_id, MAX(grade) AS highest_grade
FROM Enrollments
GROUP BY student_id
ORDER BY student_id;
