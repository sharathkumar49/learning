"""
601. Human Traffic of Stadium (SQL)
Difficulty: Hard

Table: Stadium
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| visit_date  | date |
| people      | int  |
+-------------+------+
id is the primary key for this table.
visit_date is the date of the visit.
people is the number of people who visited the stadium on that day.

Write an SQL query to display the records with three or more consecutive rows (by id) with people >= 100.

Example:
Stadium table:
+----+------------+-------+
| id | visit_date | people|
+----+------------+-------+
| 1  | 2017-01-01 | 10    |
| 2  | 2017-01-02 | 109   |
| 3  | 2017-01-03 | 150   |
| 4  | 2017-01-04 | 99    |
| 5  | 2017-01-05 | 145   |
| 6  | 2017-01-06 | 1455  |
| 7  | 2017-01-07 | 199   |
+----+------------+-------+

Result table:
+----+------------+-------+
| id | visit_date | people|
+----+------------+-------+
| 5  | 2017-01-05 | 145   |
| 6  | 2017-01-06 | 1455  |
| 7  | 2017-01-07 | 199   |
+----+------------+-------+
"""


-- SQL Solution:
SELECT id, visit_date, people
FROM (
  SELECT *,
    LAG(people, 1) OVER (ORDER BY id) AS prev1,
    LAG(people, 2) OVER (ORDER BY id) AS prev2,
    LEAD(people, 1) OVER (ORDER BY id) AS next1,
    LEAD(people, 2) OVER (ORDER BY id) AS next2
  FROM Stadium
) t
WHERE (people >= 100 AND prev1 >= 100 AND prev2 >= 100)
   OR (people >= 100 AND prev1 >= 100 AND next1 >= 100)
   OR (people >= 100 AND next1 >= 100 AND next2 >= 100);
