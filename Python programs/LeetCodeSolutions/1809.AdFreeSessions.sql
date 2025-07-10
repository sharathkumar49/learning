"""
LeetCode 1809. Ad-Free Sessions

Table: Playback
+-------------+------+
| Column Name | Type |
+-------------+------+
| session_id  | int  |
| customer_id | int  |
| start_time  | int  |
| end_time    | int  |
| ad_id       | int  |
+-------------+------+
(session_id) is the primary key.

Write an SQL query to find the number of ad-free sessions for each customer.

Example:
Playback table:
| session_id | customer_id | start_time | end_time | ad_id |
|------------|-------------|------------|----------|-------|
| 1          | 1           | 10         | 20       | 1     |
| 2          | 1           | 20         | 30       | null  |
| 3          | 2           | 15         | 25       | null  |

Output:
| customer_id | ad_free_sessions |
|-------------|------------------|
| 1           | 1                |
| 2           | 1                |

"""
SELECT customer_id, COUNT(*) AS ad_free_sessions
FROM Playback
WHERE ad_id IS NULL
GROUP BY customer_id;
