"""
LeetCode 1511. Customer Order Frequency

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| customer_id | int  |
| order_date  | date |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to find the customer_id and the number of orders for each customer.

Example:
Input:
Orders table:
| order_id | customer_id | order_date |
|----------|-------------|------------|
| 1        | 1           | 2025-06-01 |
| 2        | 2           | 2025-06-02 |
| 3        | 1           | 2025-06-03 |
Output:
| customer_id | order_count |
|-------------|-------------|
| 1           | 2           |
| 2           | 1           |
"""

-- SQL Query:
SELECT customer_id, COUNT(*) AS order_count
FROM Orders
GROUP BY customer_id;
