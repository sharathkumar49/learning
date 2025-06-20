"""
626. Exchange Seats (SQL)
Difficulty: Medium

Table: Seat
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| student     | varchar |
+-------------+------+
id is the primary key for this table.

Write an SQL query to swap the seat id of every two consecutive students. If the number of students is odd, the last student keeps their seat.

Example:
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Elvis   |
+----+---------+

Result table:
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Elvis   |
+----+---------+

SQL Solution:
SELECT CASE
    WHEN id % 2 = 1 AND id + 1 <= (SELECT COUNT(*) FROM Seat) THEN id + 1
    WHEN id % 2 = 0 THEN id - 1
    ELSE id
  END AS id, student
FROM Seat
ORDER BY id;
