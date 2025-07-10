"""
LeetCode 1890. Interval Cancellations

Table: Intervals
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| interval_id | int   |
| start       | int   |
| end         | int   |
+-------------+-------+
interval_id is the primary key for this table.

Write an SQL query to find all intervals that are not covered by any other interval.

Example:
Intervals table:
| interval_id | start | end |
|-------------|-------|-----|
| 1           | 1     | 4   |
| 2           | 3     | 6   |
| 3           | 2     | 8   |

Output:
| interval_id |
|-------------|
| 3           |
"""

-- SQL Solution
SELECT a.interval_id
FROM Intervals a
WHERE NOT EXISTS (
    SELECT 1 FROM Intervals b
    WHERE b.start <= a.start AND b.end >= a.end AND b.interval_id != a.interval_id
);
