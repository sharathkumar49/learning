"""
LeetCode 1285. Find the Start and End Number of Continuous Ranges

Table: Logs
+-------------+------+
| Column Name | Type |
+-------------+------+
| log_id      | int  |
+-------------+------+
log_id is the primary key.

Write an SQL query to find the start and end number of each continuous range in the table Logs.

Example:
Logs table:
| log_id |
|--------|
| 1      |
| 2      |
| 3      |
| 7      |
| 8      |
| 10     |

Output:
| start_id | end_id |
|----------|--------|
| 1        | 3      |
| 7        | 8      |
| 10       | 10     |

"""
SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM (
  SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
  FROM Logs
) t
GROUP BY grp
ORDER BY start_id;
