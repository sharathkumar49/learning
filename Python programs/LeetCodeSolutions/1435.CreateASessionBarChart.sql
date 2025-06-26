"""
LeetCode 1435. Create a Session Bar Chart

Table: Activity
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| session_id     | int     |
| user_id        | int     |
| activity_date  | date    |
| activity_type  | enum    |
+----------------+---------+
session_id is the primary key for this table.
activity_type is an ENUM of type ('open_session', 'end_session', 'scroll_down', 'send_message').

Write an SQL query to report the number of sessions started on each day. Return the result table ordered by activity_date.

Example:
Input:
Activity table:
| session_id | user_id | activity_date | activity_type |
|------------|---------|---------------|---------------|
| 1          | 1       | 2020-07-20    | open_session  |
| 2          | 1       | 2020-07-20    | scroll_down   |
| 3          | 1       | 2020-07-20    | end_session   |
| 4          | 4       | 2020-07-21    | open_session  |
| 5          | 4       | 2020-07-21    | send_message  |
| 6          | 4       | 2020-07-21    | end_session   |
| 7          | 5       | 2020-07-21    | open_session  |
| 8          | 5       | 2020-07-21    | scroll_down   |
| 9          | 5       | 2020-07-21    | end_session   |
Output:
| activity_date | sessions_count |
|--------------|----------------|
| 2020-07-20   | 1              |
| 2020-07-21   | 2              |
"""

--SQL Query:
SELECT activity_date, COUNT(*) AS sessions_count
FROM Activity
WHERE activity_type = 'open_session'
GROUP BY activity_date
ORDER BY activity_date;
