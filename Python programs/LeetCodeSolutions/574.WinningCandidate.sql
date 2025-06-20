"""
574. Winning Candidate (SQL)
Difficulty: Medium

Table: Candidate
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
+-------------+------+
id is the primary key for this table.

Table: Vote
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| candidateId | int  |
+-------------+------+
id is the primary key for this table.
candidateId is a foreign key to Candidate.id.

Write an SQL query to find the name of the winning candidate. The test cases are generated so that exactly one candidate wins.

Example:
Candidate table:
+----+------+
| id | name |
+----+------+
| 1  | A    |
| 2  | B    |
| 3  | C    |
| 4  | D    |
+----+------+

Vote table:
+----+-------------+
| id | candidateId |
+----+-------------+
| 1  | 2           |
| 2  | 4           |
| 3  | 3           |
| 4  | 2           |
+----+-------------+

Result table:
+------+
| name |
+------+
| B    |
+------+

SQL Solution:
SELECT name
FROM Candidate
WHERE id = (
    SELECT candidateId
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
