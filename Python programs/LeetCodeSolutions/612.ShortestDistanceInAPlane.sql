"""
612. Shortest Distance in a Plane (SQL)
Difficulty: Medium

Table: Point
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
+-------------+------+
(x, y) is the primary key for this table.

Write an SQL query to report the shortest distance between any two points in the plane. Round the result to 2 decimal places.

Example:
Point table:
+----+----+
| x  | y  |
+----+----+
| -1 | -1 |
| 0  | 0  |
| -1 | 0  |
+----+----+

Result table:
+----------+
| shortest |
+----------+
| 1.00     |
+----------+

"""

-- SQL Solution:
SELECT ROUND(MIN(SQRT(POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))), 2) AS shortest
FROM Point p1, Point p2
WHERE NOT (p1.x = p2.x AND p1.y = p2.y);
