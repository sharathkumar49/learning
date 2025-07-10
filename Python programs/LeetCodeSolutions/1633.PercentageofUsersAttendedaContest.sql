"""
LeetCode 1633. Percentage of Users Attended a Contest

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
+-------------+------+
user_id is the primary key for this table.

Table: Register
+-------------+------+
| Column Name | Type |
+-------------+------+
| contest_id  | int  |
| user_id     | int  |
+-------------+------+
(contest_id, user_id) is the primary key for this table.

Write an SQL query to report the percentage of users registered for each contest rounded to two decimals.

Example:
Input:
Users table:
| user_id |
|---------|
| 6       |
| 2       |
| 3       |
Register table:
| contest_id | user_id |
|------------|---------|
| 215        | 6       |
| 209        | 2       |
| 208        | 2       |
| 210        | 6       |
| 208        | 6       |
| 209        | 6       |
| 209        | 3       |
Output:
| contest_id | percentage |
|------------|------------|
| 208        | 66.67      |
| 209        | 100.00     |
| 210        | 33.33      |
| 215        | 33.33      |
"""

-- SQL Query:
SELECT contest_id, ROUND(COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id;
