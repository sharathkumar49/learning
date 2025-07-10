"""
LeetCode 1549. The Most Recent Orders for Each Product

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| product_id  | int  |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to find the most recent order for each product.

Example:
Input:
Orders table:
| order_id | order_date | product_id |
|----------|------------|------------|
| 1        | 2025-06-01 | 1          |
| 2        | 2025-06-02 | 1          |
| 3        | 2025-06-03 | 2          |
Output:
| order_id | order_date | product_id |
|----------|------------|------------|
| 2        | 2025-06-02 | 1          |
| 3        | 2025-06-03 | 2          |
"""

-- SQL Query:
SELECT o.order_id, o.order_date, o.product_id
FROM Orders o
JOIN (
    SELECT product_id, MAX(order_date) AS max_date
    FROM Orders
    GROUP BY product_id
) t ON o.product_id = t.product_id AND o.order_date = t.max_date;
