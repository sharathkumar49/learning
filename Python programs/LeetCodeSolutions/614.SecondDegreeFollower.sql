"""
614. Second Degree Follower (SQL)
Difficulty: Medium

Table: Follow
+-------------+------+
| Column Name | Type |
+-------------+------+
| followee    | int  |
| follower    | int  |
+-------------+------+
(followee, follower) is the primary key for this table.

Write an SQL query to report the follower who is a second degree follower of a user. A second degree follower is a follower's follower who is not a direct follower.

Example:
Follow table:
+----------+----------+
| followee | follower |
+----------+----------+
| 1        | 2        |
| 2        | 3        |
| 1        | 3        |
+----------+----------+

Result table:
+----------+----------+
| followee | follower |
+----------+----------+
| 1        | 3        |
+----------+----------+
"""

-- SQL Solution:
SELECT DISTINCT f1.followee, f2.follower
FROM Follow f1
JOIN Follow f2 ON f1.follower = f2.followee
WHERE f1.followee != f2.follower
  AND NOT EXISTS (
    SELECT 1 FROM Follow f3 WHERE f3.followee = f1.followee AND f3.follower = f2.follower
  );
