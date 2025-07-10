"""
LeetCode 1729. Find Followers Count

Table: Followers
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key.

Write an SQL query to find the number of followers for each user.

Example:
Followers table:
| user_id | follower_id |
|---------|-------------|
| 1       | 2           |
| 1       | 3           |
| 2       | 1           |

Output:
| user_id | followers_count |
|---------|-----------------|
| 1       | 2               |
| 2       | 1               |

"""
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id;
