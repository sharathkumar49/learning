"""
585. Investments in 2016 (SQL)
Difficulty: Medium

Table: Insurance
+-------------+------+
| Column Name | Type |
+-------------+------+
| pid         | int  |
| tiv_2015    | float|
| tiv_2016    | float|
| lat         | float|
| lon         | float|
+-------------+------+
pid is the primary key for this table.

Write an SQL query to report the total tiv_2016 of all insurance policies that satisfy:
- Have tiv_2015 value that is the same as one or more other policies.
- Are not located in the same (lat, lon) as any other policy.

Example:
Insurance table:
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+

Result table:
+----------+
| tiv_2016 |
+----------+
| 45.0     |
+----------+

SQL Solution:
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1
) AND (lat, lon) IN (
    SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1
);
