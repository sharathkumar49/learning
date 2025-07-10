"""
LeetCode 1907. Count Salutes

Table: Employees
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| direction   | char  |
+-------------+-------+
id is the primary key for this table.

direction is either 'L' (left) or 'R' (right). Each employee salutes every employee they pass. Return the total number of salutes.

Example:
Employees table:
| id | direction |
|----|-----------|
| 1  | R         |
| 2  | L         |
| 3  | R         |
| 4  | L         |

Output:
| salutes |
|---------|
| 4       |
"""

-- SQL Solution
SELECT SUM(r.cnt) AS salutes
FROM (
    SELECT COUNT(*) AS cnt
    FROM Employees e1, Employees e2
    WHERE e1.direction = 'R' AND e2.direction = 'L' AND e1.id < e2.id
) r;
