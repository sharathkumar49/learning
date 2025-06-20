"""
602. Friend Requests II: Who Has the Most Friends (SQL)
Difficulty: Medium

Table: RequestAccepted
+-------------+------+
| Column Name | Type |
+-------------+------+
| requester_id| int  |
| accepter_id | int  |
| accept_date | date |
+-------------+------+
(requester_id, accepter_id) is the primary key for this table.

Write an SQL query to find the id of the person who has the most friends. The result should have columns id and num.

Example:
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016-06-03  |
| 1            | 3           | 2016-06-08  |
| 2            | 3           | 2016-06-08  |
| 3            | 4           | 2016-06-09  |
+--------------+-------------+-------------+

Result table:
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
"""

-- SQL Solution:
SELECT id, COUNT(*) AS num
FROM (
  SELECT requester_id AS id FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id FROM RequestAccepted
) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;
