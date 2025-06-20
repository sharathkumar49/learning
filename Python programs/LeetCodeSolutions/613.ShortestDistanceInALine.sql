"""
613. Shortest Distance in a Line (SQL)
Difficulty: Easy

Table: Point
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
+-------------+------+
x is the primary key for this table.

Write an SQL query to report the shortest distance between any two points in the line. Round the result to 2 decimal places.

Example:
Point table:
+----+
| x  |
+----+
| -1 |
| 0  |
| 2  |
+----+

Result table:
+----------+
| shortest |
+----------+
| 1.00     |
+----------+
"""

-- SQL Solution:
SELECT ROUND(MIN(ABS(p1.x - p2.x)), 2) AS shortest
FROM Point p1, Point p2
WHERE p1.x != p2.x;
