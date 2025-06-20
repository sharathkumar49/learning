"""
578. Get Highest Answer Rate Question (SQL)
Difficulty: Medium

Table: SurveyLog
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| action      | varchar |
| question_id | int  |
| answer_id   | int  |
| q_num       | int  |
| timestamp   | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to find the question_id with the highest answer rate. If there is a tie, return the smallest question_id.

Example:
SurveyLog table:
+----+-----------+-------------+-----------+-------+-----------+
| id | action    | question_id | answer_id | q_num | timestamp |
+----+-----------+-------------+-----------+-------+-----------+
| 1  | show      | 285         | null      | 1     | 123       |
| 2  | answer    | 285         | 124124    | 1     | 124       |
| 3  | show      | 369         | null      | 1     | 125       |
| 4  | answer    | 369         | 267768    | 1     | 126       |
| 5  | show      | 285         | null      | 2     | 127       |
+----+-----------+-------------+-----------+-------+-----------+

Result table:
+-------------+
| question_id |
+-------------+
| 285         |
+-------------+

SQL Solution:
SELECT question_id
FROM (
    SELECT question_id, SUM(action = 'answer')/SUM(action = 'show') AS rate
    FROM SurveyLog
    GROUP BY question_id
) t
ORDER BY rate DESC, question_id ASC
LIMIT 1;
