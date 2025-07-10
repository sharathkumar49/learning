"""
LeetCode 1667. Fix Names in a Table

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| name        | varchar |
+-------------+------+
user_id is the primary key for this table.

Write an SQL query to fix the names in the Users table so that only the first character is uppercase and the rest are lowercase.

Example:
Input:
Users table:
| user_id | name  |
|---------|-------|
| 1       | aLice |
| 2       | bOB   |
Output:
| user_id | name  |
|---------|-------|
| 1       | Alice |
| 2       | Bob   |
"""

-- SQL Query:
SELECT user_id, UPPER(LEFT(name, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM Users;
