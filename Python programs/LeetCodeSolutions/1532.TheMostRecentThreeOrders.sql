"""
LeetCode 1532. The Most Recent Three Orders

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| customer_id | int  |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to find the three most recent orders for each customer.

Example:
Input:
Orders table:
| order_id | order_date | customer_id |
|----------|------------|-------------|
| 1        | 2025-06-01 | 1           |
| 2        | 2025-06-02 | 1           |
| 3        | 2025-06-03 | 1           |
| 4        | 2025-06-04 | 2           |
| 5        | 2025-06-05 | 2           |
Output:
| order_id | order_date | customer_id |
|----------|------------|-------------|
| 1        | 2025-06-01 | 1           |
| 2        | 2025-06-02 | 1           |
| 3        | 2025-06-03 | 1           |
| 4        | 2025-06-04 | 2           |
| 5        | 2025-06-05 | 2           |
"""

-- SQL Query:
SELECT order_id, order_date, customer_id
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
    FROM Orders
) t
WHERE rn <= 3;
