"""
LeetCode 1956. Minimum Time For K Virus Variants

Table: Variants
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| time        | int   |
+-------------+-------+
id is the primary key for this table.

Write an SQL query to find the minimum time for each variant.

Example:
Variants table:
| id | time |
|----|------|
| 1  | 10   |
| 2  | 5    |
| 3  | 7    |

Output:
| id | min_time |
|----|----------|
| 1  | 10       |
| 2  | 5        |
| 3  | 7        |
"""

-- SQL Solution
SELECT id, time AS min_time
FROM Variants;
