"""
LeetCode 2084. Drop Type 1 Orders for Customers With Type 2 Orders

Table: Orders
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| order_id    | int   |
| customer_id | int   |
| type        | int   |
+-------------+-------+
order_id is the primary key for this table.

Write an SQL query to delete all type 1 orders for customers who have at least one type 2 order.

Example:
Orders table:
| order_id | customer_id | type |
|----------|-------------|------|
| 1        | 1           | 1    |
| 2        | 1           | 2    |
| 3        | 2           | 1    |

After deletion, Orders table:
| order_id | customer_id | type |
|----------|-------------|------|
| 2        | 1           | 2    |
| 3        | 2           | 1    |
"""

-- SQL Solution
DELETE FROM Orders
WHERE type = 1 AND customer_id IN (SELECT customer_id FROM Orders WHERE type = 2);
