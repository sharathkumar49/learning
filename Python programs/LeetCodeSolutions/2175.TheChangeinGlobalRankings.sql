"""
LeetCode 2175. The Change in Global Rankings

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| score       | int  |
+-------------+------+
user_id is the primary key.

Table: Rankings
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| old_rank    | int  |
| new_rank    | int  |
+-------------+------+
user_id is the primary key.

Write an SQL query to report the change in global ranking for each user.

Example:
Users table:
| user_id | score |
|---------|-------|
| 1       | 100   |
| 2       | 200   |
| 3       | 150   |
Rankings table:
| user_id | old_rank | new_rank |
|---------|----------|----------|
| 1       | 2        | 3        |
| 2       | 1        | 1        |
| 3       | 3        | 2        |

Output:
| user_id | change |
|---------|--------|
| 1       | 1      |
| 2       | 0      |
| 3       | 1      |

Solution:
SELECT user_id, ABS(old_rank - new_rank) AS change
FROM Rankings;
