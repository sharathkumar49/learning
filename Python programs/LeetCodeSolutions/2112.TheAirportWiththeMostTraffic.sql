"""
LeetCode 2112. The Airport With the Most Traffic

Table: Flights
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| airport     | varchar|
| traffic     | int   |
+-------------+-------+
id is the primary key for this table.

Write an SQL query to return the airport with the most traffic.

Example:
Flights table:
| id | airport | traffic |
|----|---------|---------|
| 1  | JFK     | 100     |
| 2  | LAX     | 200     |
| 3  | JFK     | 150     |

Output:
| airport |
|---------|
| JFK     |
"""

-- SQL Solution
SELECT airport
FROM Flights
GROUP BY airport
ORDER BY SUM(traffic) DESC
LIMIT 1;
