"""
LeetCode 2026. Low-Quality Problems

Table: Problems
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| problem_id  | int   |
| quality     | int   |
+-------------+-------+
problem_id is the primary key for this table.
quality is 0 for low-quality, 1 for high-quality.

Write an SQL query to return the number of low-quality problems.

Example:
Problems table:
| problem_id | quality |
|------------|---------|
| 1          | 0       |
| 2          | 1       |
| 3          | 0       |

Output:
| low_quality_count |
|------------------|
| 2                |
"""

-- SQL Solution
SELECT COUNT(*) AS low_quality_count
FROM Problems
WHERE quality = 0;
