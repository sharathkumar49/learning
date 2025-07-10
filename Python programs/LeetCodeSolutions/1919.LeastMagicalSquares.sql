"""
LeetCode 1919. Least Magical Squares

Table: Squares
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| square_id   | int   |
| value       | int   |
+-------------+-------+
square_id is the primary key for this table.

Write an SQL query to find the square with the least magical value.

Example:
Squares table:
| square_id | value |
|-----------|-------|
| 1         | 10    |
| 2         | 5     |
| 3         | 7     |

Output:
| square_id | value |
|-----------|-------|
| 2         | 5     |
"""

-- SQL Solution
SELECT square_id, value
FROM Squares
WHERE value = (SELECT MIN(value) FROM Squares);
