"""
1141. User Activity for the Past 30 Days I (SQL)

Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| session_id   | int     |
| activity_date| date    |
| activity_type| enum    |
+--------------+---------+
(activity_type: 'open_session', 'end_session', 'scroll_down', 'send_message')

Write an SQL query to find the number of active users for each day in the past 30 days (including today). An active user is a user who has done at least one activity per day.

Return result table ordered by date ascending.

"""
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 29 DAY) AND CURDATE()
GROUP BY activity_date
ORDER BY activity_date;
