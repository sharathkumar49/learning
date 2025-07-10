"""
LeetCode 1596. The Most Frequently Ordered Products for Each Customer

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| customer_id | int  |
| product_id  | int  |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to find the most frequently ordered product(s) for each customer.

Example:
Input:
Orders table:
| order_id | customer_id | product_id |
|----------|-------------|------------|
| 1        | 1           | 5          |
| 2        | 1           | 6          |
| 3        | 1           | 5          |
| 4        | 2           | 6          |
Output:
| customer_id | product_id |
|-------------|------------|
| 1           | 5          |
| 2           | 6          |
"""

-- SQL Query:
WITH freq AS (
  SELECT customer_id, product_id, COUNT(*) AS cnt
  FROM Orders
  GROUP BY customer_id, product_id
),
max_freq AS (
  SELECT customer_id, MAX(cnt) AS max_cnt
  FROM freq
  GROUP BY customer_id
)
SELECT f.customer_id, f.product_id
FROM freq f
JOIN max_freq m ON f.customer_id = m.customer_id AND f.cnt = m.max_cnt;
