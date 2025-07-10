"""
LeetCode 1661. Average Time of Process per Machine

Table: Activity
+-------------+------+
| Column Name | Type |
+-------------+------+
| machine_id  | int  |
| process_id  | int  |
| activity_type | enum('start', 'end') |
| timestamp   | float |
+-------------+------+
(machine_id, process_id, activity_type) is the primary key for this table.

Write an SQL query to report the average time each machine takes to complete a process, rounded to 3 decimal places.

Example:
Input:
Activity table:
| machine_id | process_id | activity_type | timestamp |
|------------|------------|---------------|-----------|
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
Output:
| machine_id | processing_time |
|------------|----------------|
| 0          | 0.894          |
| 1          | 1.000          |
"""

-- SQL Query:
SELECT machine_id, ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
  SELECT a.machine_id, a.process_id,
         MAX(CASE WHEN a.activity_type = 'start' THEN a.timestamp END) AS start_time,
         MAX(CASE WHEN a.activity_type = 'end' THEN a.timestamp END) AS end_time
  FROM Activity a
  GROUP BY a.machine_id, a.process_id
) t
GROUP BY machine_id;
