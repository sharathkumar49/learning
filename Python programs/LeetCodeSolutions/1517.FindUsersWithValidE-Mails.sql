"""
LeetCode 1517. Find Users With Valid E-Mails

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| name        | text |
| mail        | text |
+-------------+------+
user_id is the primary key for this table.

Write an SQL query to find the users with valid emails. A valid email has the format name@domain.com.

Example:
Input:
Users table:
| user_id | name | mail           |
|---------|------|----------------|
| 1       | a    | a@leetcode.com |
| 2       | b    | b@.com         |
| 3       | c    | c@leetcode.com |
Output:
| user_id | name | mail           |
|---------|------|----------------|
| 1       | a    | a@leetcode.com |
| 3       | c    | c@leetcode.com |
"""

-- SQL Query:
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';
