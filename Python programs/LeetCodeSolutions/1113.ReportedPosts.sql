"""
1113. Reported Posts (SQL)

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

Write an SQL query to find the number of unique posts reported each day.

"""
SELECT action_date, COUNT(DISTINCT post_id) AS unique_reports
FROM Actions
WHERE action = 'report'
GROUP BY action_date;
