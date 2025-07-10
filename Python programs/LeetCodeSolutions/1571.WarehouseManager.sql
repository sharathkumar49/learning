"""
LeetCode 1571. Warehouse Manager

Table: Boxes
+-------------+------+
| Column Name | Type |
+-------------+------+
| box_id      | int  |
| warehouse   | text |
| product     | text |
| units       | int  |
+-------------+------+
box_id is the primary key for this table.

Write an SQL query to report the number of units in each warehouse.

Example:
Input:
Boxes table:
| box_id | warehouse | product | units |
|--------|-----------|---------|-------|
| 1      | W1        | P1      | 10    |
| 2      | W1        | P2      | 20    |
| 3      | W2        | P1      | 15    |
Output:
| warehouse | total_units |
|-----------|-------------|
| W1        | 30          |
| W2        | 15          |
"""

-- SQL Query:
SELECT warehouse, SUM(units) AS total_units
FROM Boxes
GROUP BY warehouse;
