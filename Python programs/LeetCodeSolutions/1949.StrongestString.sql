"""
LeetCode 1949. Strongest String

Table: Strings
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| value       | varchar|
+-------------+-------+
id is the primary key for this table.

Write an SQL query to find the string with the maximum length.

Example:
Strings table:
| id | value   |
|----|---------|
| 1  | "abc"   |
| 2  | "abcd"  |
| 3  | "a"     |

Output:
| id | value   |
|----|---------|
| 2  | "abcd"  |
"""

-- SQL Solution
SELECT id, value
FROM Strings
WHERE LENGTH(value) = (SELECT MAX(LENGTH(value)) FROM Strings);
