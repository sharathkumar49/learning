"""
LeetCode 1867. Orders With Maximum Quantity

Table: Orders
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| order_id    | int   |
| quantity    | int   |
+-------------+-------+
order_id is the primary key for this table.

Write an SQL query to find the order(s) with the maximum quantity.

Example:
Orders table:
| order_id | quantity |
|----------|----------|
| 1        | 10       |
| 2        | 15       |
| 3        | 15       |

Output:
| order_id | quantity |
|----------|----------|
| 2        | 15       |
| 3        | 15       |
"""

-- SQL Solution
SELECT order_id, quantity
FROM Orders
WHERE quantity = (SELECT MAX(quantity) FROM Orders);
