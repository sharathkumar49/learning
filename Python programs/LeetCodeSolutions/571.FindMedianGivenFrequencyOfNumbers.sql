"""
571. Find Median Given Frequency of Numbers (SQL)
Difficulty: Hard

Table: Numbers
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
| frequency   | int  |
+-------------+------+
num is the primary key for this table.
Each row of this table indicates that number num appears frequency times.

Write an SQL query to report the median of all numbers.

Example:
Numbers table:
+-----+-----------+
| num | frequency |
+-----+-----------+
| 0   | 7         |
| 1   | 1         |
| 2   | 3         |
+-----+-----------+

Result table:
+--------+
| median |
+--------+
| 0      |
+--------+

SQL Solution:
WITH ordered AS (
  SELECT num, frequency, SUM(frequency) OVER (ORDER BY num) AS cum_freq
  FROM Numbers
),
info AS (
  SELECT SUM(frequency) AS total FROM Numbers
)
SELECT MIN(num) AS median
FROM ordered, info
WHERE cum_freq >= (total + 1) / 2;
