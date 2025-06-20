"""
597. Friend Requests I: Overall Acceptance Rate (SQL)
Difficulty: Easy

Table: FriendRequest
+-------------+------+
| Column Name | Type |
+-------------+------+
| sender_id   | int  |
| send_to_id  | int  |
+-------------+------+
(sender_id, send_to_id) is the primary key for this table.

Table: RequestAccepted
+-------------+------+
| Column Name | Type |
+-------------+------+
| sender_id   | int  |
| send_to_id  | int  |
+-------------+------+
(sender_id, send_to_id) is the primary key for this table.

Write an SQL query to find the overall acceptance rate of friend requests. The acceptance rate is the number of accepted requests divided by the total number of requests. Round the result to 2 decimal places.

Example:
FriendRequest table:
+-----------+------------+
| sender_id | send_to_id |
+-----------+------------+
| 1         | 2          |
| 1         | 3          |
| 1         | 4          |
| 2         | 3          |
| 3         | 4          |
+-----------+------------+

RequestAccepted table:
+-----------+------------+
| sender_id | send_to_id |
+-----------+------------+
| 1         | 2          |
| 1         | 3          |
| 1         | 4          |
| 2         | 3          |
+-----------+------------+

Result table:
+-------------------+
| accept_rate       |
+-------------------+
| 0.80              |
+-------------------+

SQL Solution:
SELECT ROUND(
    (SELECT COUNT(*) FROM RequestAccepted) * 1.0 /
    (SELECT COUNT(*) FROM FriendRequest), 2
) AS accept_rate;
