"""
LeetCode 1843. Suspension Bridges

Table: Bridges
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| bridge_id   | int   |
| city1       | varchar |
| city2       | varchar |
| length      | int   |
+-------------+-------+
bridge_id is the primary key for this table.

Write an SQL query to find the city that is connected to the most other cities by bridges.

Example:
Bridges table:
| bridge_id | city1 | city2 | length |
|-----------|-------|-------|--------|
| 1         | A     | B     | 100    |
| 2         | A     | C     | 200    |
| 3         | B     | C     | 150    |

Output:
| city  |
|-------|
| A     |

"""

-- SQL Solution
SELECT city
FROM (
  SELECT city1 AS city, COUNT(DISTINCT city2) AS cnt FROM Bridges GROUP BY city1
  UNION ALL
  SELECT city2 AS city, COUNT(DISTINCT city1) AS cnt FROM Bridges GROUP BY city2
) t
GROUP BY city
ORDER BY SUM(cnt) DESC, city
LIMIT 1;
