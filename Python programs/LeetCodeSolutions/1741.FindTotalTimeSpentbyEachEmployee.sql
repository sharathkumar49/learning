"""
LeetCode 1741. Find Total Time Spent by Each Employee

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| emp_id      | int  |
| event_day   | date |
| in_time     | int  |
| out_time    | int  |
+-------------+------+
(emp_id, event_day, in_time) is the primary key.

Write an SQL query to find the total time spent by each employee each day.

Example:
Employees table:
| emp_id | event_day | in_time | out_time |
|--------|-----------|---------|----------|
| 1      | 2020-11-28| 4       | 32       |
| 1      | 2020-11-28| 55      | 200      |
| 1      | 2020-12-03| 1       | 42       |
| 2      | 2020-11-28| 3       | 33       |
| 2      | 2020-12-09| 47      | 74       |

Output:
| emp_id | event_day  | total_time |
|--------|------------|------------|
| 1      | 2020-11-28 | 173        |
| 1      | 2020-12-03 | 41         |
| 2      | 2020-11-28 | 30         |
| 2      | 2020-12-09 | 27         |

"""
SELECT emp_id, event_day, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day;
