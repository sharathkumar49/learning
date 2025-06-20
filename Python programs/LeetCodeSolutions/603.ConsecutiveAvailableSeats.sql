"""
603. Consecutive Available Seats (SQL)
Difficulty: Easy

Table: Cinema
+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is the primary key for this table.

Write an SQL query to output all seat_ids with consecutive available seats (i.e., free = 1) in ascending order.

Example:
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+

Result table:
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+

SQL Solution:
SELECT DISTINCT c1.seat_id
FROM Cinema c1
JOIN Cinema c2 ON ABS(c1.seat_id - c2.seat_id) = 1 AND c2.free = 1
WHERE c1.free = 1
ORDER BY c1.seat_id;
