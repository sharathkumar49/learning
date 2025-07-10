"""
LeetCode 1454. Active Users

Table: Logins
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| time_stamp  | int  |
+-------------+------+
(user_id, time_stamp) is the primary key for this table.

Write an SQL query to find the number of users that were active in the past 30 days (i.e., have logged in at least once in the past 30 days).

Example:
Input:
Logins table:
| user_id | time_stamp |
|---------|------------|
| 1       | 5          |
| 2       | 20         |
| 3       | 35         |
| 1       | 40         |
Output:
| active_users |
|--------------|
| 3            |
"""

-- SQL Query:
SELECT COUNT(DISTINCT user_id) AS active_users
FROM Logins
WHERE time_stamp >= (SELECT MAX(time_stamp) FROM Logins) - 29;
