"""
LeetCode 1311. Get Watched Videos by Your Friends

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
+-------------+------+
id is the primary key.

Table: Friendship
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| friend_id   | int  |
+-------------+------+
(user_id, friend_id) is the primary key.

Table: VideosWatched
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| video_name  | varchar |
+-------------+------+
(user_id, video_name) is the primary key.

Write an SQL query to get the list of videos watched by friends of a given user at a given level, ordered by frequency and then by name.

Example:
(See LeetCode for full details.)

"""
-- This problem requires recursive queries and parameters for user_id and level.
-- See LeetCode for full schema and requirements.
