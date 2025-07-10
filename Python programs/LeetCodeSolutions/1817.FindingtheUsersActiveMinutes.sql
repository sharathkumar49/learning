"""
LeetCode 1817. Finding the Users Active Minutes

Table: UserActivity
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| time_stamp  | int  |
+-------------+------+
(user_id, time_stamp) is the primary key.

Write an SQL query to find the number of users with a given UAM (user active minutes).

Example:
UserActivity table:
| user_id | time_stamp |
|---------|------------|
| 1       | 5          |
| 1       | 2          |
| 2       | 2          |
| 2       | 3          |
| 2       | 5          |

Output:
| uam | count |
|-----|-------|
| 1   | 1     |
| 2   | 1     |
| 3   | 1     |

"""
SELECT uam, COUNT(*) AS count
FROM (
    SELECT user_id, COUNT(DISTINCT time_stamp) AS uam
    FROM UserActivity
    GROUP BY user_id
) t
GROUP BY uam;
