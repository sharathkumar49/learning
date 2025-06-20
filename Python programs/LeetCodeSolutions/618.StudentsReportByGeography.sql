"""
618. Students Report By Geography (SQL)
Difficulty: Hard

Table: Student
+-------------+------+
| Column Name | Type |
+-------------+------+
| student_id  | int  |
| name        | varchar |
| continent   | varchar |
+-------------+------+
student_id is the primary key for this table.

Write an SQL query to report the number of students in each continent.

Example:
Student table:
+------------+---------+-----------+
| student_id | name    | continent |
+------------+---------+-----------+
| 1          | Jack    | America   |
| 2          | Pascal  | Europe    |
| 3          | Xi      | Asia      |
| 4          | Jane    | America   |
+------------+---------+-----------+

Result table:
+-----------+----------------+
| continent | student_number |
+-----------+----------------+
| America   | 2              |
| Asia      | 1              |
| Europe    | 1              |
+-----------+----------------+

SQL Solution:
SELECT continent, COUNT(*) AS student_number
FROM Student
GROUP BY continent;
