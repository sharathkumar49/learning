"""
LeetCode 1934. Confirmation Rate

Table: Signups
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| user_id     | int   |
+-------------+-------+
user_id is the primary key for this table.

Table: Confirmations
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| user_id     | int   |
| time_stamp  | int   |
| action      | ENUM('confirmed', 'timeout') |
+-------------+-------+
(user_id, time_stamp) is the primary key for this table.

Write an SQL query to find the confirmation rate for each user.

Example:
Signups table:
| user_id |
|---------|
| 3       |
| 7       |
| 2       |
| 6       |

Confirmations table:
| user_id | time_stamp | action     |
|---------|------------|------------|
| 3       | 100        | confirmed  |
| 3       | 200        | confirmed  |
| 3       | 300        | timeout    |
| 7       | 400        | timeout    |
| 7       | 500        | confirmed  |
| 2       | 600        | confirmed  |
| 2       | 700        | confirmed  |

Output:
| user_id | confirmation_rate |
|---------|------------------|
| 2       | 1.00             |
| 3       | 0.67             |
| 7       | 0.50             |
| 6       | 0.00             |
"""

-- SQL Solution
SELECT s.user_id, 
       ROUND(COALESCE(SUM(c.action = 'confirmed') / COUNT(c.action), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
