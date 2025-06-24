"""
1132. Reported Posts II (SQL)

Table: Actions
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| post_id     | int     |
| action_date | date    |
| action      | enum    |
+-------------+---------+
(user_id, post_id, action_date) is the primary key.

Write an SQL query to find the number of unique users who reported posts each day.

"""
SELECT action_date, COUNT(DISTINCT user_id) AS unique_reporters
FROM Actions
WHERE action = 'report'
GROUP BY action_date;
