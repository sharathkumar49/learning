"""
1142. User Activity for the Past 30 Days II (SQL)

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

Write an SQL query to find the average number of active users for each day in the past 30 days (including today). An active user is a user who has done at least one activity per day.

Return the result as a single row with the column average_active_users, rounded to 2 decimal places.

"""
SELECT ROUND(AVG(daily_users), 2) AS average_active_users
FROM (
    SELECT activity_date, COUNT(DISTINCT user_id) AS daily_users
    FROM Activity
    WHERE activity_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 29 DAY) AND CURDATE()
    GROUP BY activity_date
) t;
