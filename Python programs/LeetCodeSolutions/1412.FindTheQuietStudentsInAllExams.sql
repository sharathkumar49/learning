"""
LeetCode 1412. Find the Quiet Students in All Exams

Table: Exam
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| exam_id     | int   |
| student_id  | int   |
| score       | int   |
+-------------+-------+
(exam_id, student_id) is the primary key for this table.

Write an SQL query to report the students who got the lowest score in each exam. Do not return students who got the lowest score in only one exam. Return the result table ordered by student_id in ascending order.

Example:
Input:
Exam table:
| exam_id | student_id | score |
|---------|------------|-------|
| 10      | 1          | 70    |
| 10      | 2          | 80    |
| 10      | 3          | 70    |
| 20      | 1          | 80    |
| 20      | 2          | 90    |
| 20      | 3          | 80    |
| 30      | 1          | 80    |
| 30      | 2          | 90    |
| 30      | 3          | 80    |
Output:
| student_id |
|------------|
| 1          |
| 3          |
"""

--SQL Query:
SELECT student_id
FROM (
    SELECT student_id, COUNT(*) AS cnt
    FROM (
        SELECT e.exam_id, e.student_id
        FROM Exam e
        JOIN (
            SELECT exam_id, MIN(score) AS min_score
            FROM Exam
            GROUP BY exam_id
        ) m ON e.exam_id = m.exam_id AND e.score = m.min_score
    ) t
    GROUP BY student_id
    HAVING cnt > 1
) x
ORDER BY student_id;
