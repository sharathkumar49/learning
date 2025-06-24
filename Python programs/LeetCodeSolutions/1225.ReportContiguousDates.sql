"""
1225. Report Contiguous Dates (SQL)

Table: Failed
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| fail_date   | date    |
+-------------+---------+
fail_date is the primary key.

Write an SQL query to report the start and end of each contiguous period of at least 3 consecutive days where the system failed.

"""
SELECT MIN(fail_date) AS start_date, MAX(fail_date) AS end_date
FROM (
    SELECT fail_date, fail_date - INTERVAL ROW_NUMBER() OVER (ORDER BY fail_date) DAY AS grp
    FROM Failed
) t
GROUP BY grp
HAVING COUNT(*) >= 3;
