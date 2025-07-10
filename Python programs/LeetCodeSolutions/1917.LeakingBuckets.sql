"""
LeetCode 1917. Leaking Buckets

Table: Buckets
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| bucket_id   | int   |
| capacity    | int   |
| leak_rate   | int   |
+-------------+-------+
bucket_id is the primary key for this table.

Write an SQL query to find the remaining capacity of each bucket after 1 hour.

Example:
Buckets table:
| bucket_id | capacity | leak_rate |
|-----------|----------|-----------|
| 1         | 10       | 2         |
| 2         | 5        | 1         |

Output:
| bucket_id | remaining |
|-----------|-----------|
| 1         | 8         |
| 2         | 4         |
"""

-- SQL Solution
SELECT bucket_id, GREATEST(capacity - leak_rate, 0) AS remaining
FROM Buckets;
