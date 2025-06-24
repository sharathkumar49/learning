"""
1107. New Users Daily Count (SQL)

Table: Traffic
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| activity    | enum    |
| activity_date | date  |
+-------------+---------+
(user_id, activity_date) is the primary key.

Write an SQL query to report the number of users who registered for the first time on each day.

"""
SELECT activity_date AS login_date, COUNT(DISTINCT user_id) AS user_count
FROM Traffic
WHERE (user_id, activity_date) IN (
    SELECT user_id, MIN(activity_date)
    FROM Traffic
    GROUP BY user_id
)
GROUP BY activity_date;
