"""
LeetCode 2356. Number of Unique Subjects Taught by Each Teacher

Table: Teacher
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| teacher_id  | int   |
| subject_id  | int   |
+-------------+-------+
teacher_id and subject_id together form the primary key.

Write an SQL query to return the number of unique subjects taught by each teacher.

Example:
Teacher table:
| teacher_id | subject_id |
|------------|------------|
| 1          | 2          |
| 1          | 3          |
| 2          | 2          |
| 2          | 4          |

Output:
| teacher_id | cnt |
|------------|-----|
| 1          | 2   |
| 2          | 2   |
"""

-- SQL Solution
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
