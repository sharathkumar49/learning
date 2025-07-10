"""
LeetCode 1565. Unique Orders and Customers Per Month

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| customer_id | int  |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to report the number of unique orders and unique customers for each month.

Example:
Input:
Orders table:
| order_id | order_date | customer_id |
|----------|------------|-------------|
| 1        | 2025-06-01 | 1           |
| 2        | 2025-06-02 | 2           |
| 3        | 2025-07-01 | 1           |
Output:
| month | unique_orders | unique_customers |
|-------|---------------|------------------|
| 2025-06 | 2           | 2                |
| 2025-07 | 1           | 1                |
"""

-- SQL Query:
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(DISTINCT order_id) AS unique_orders,
       COUNT(DISTINCT customer_id) AS unique_customers
FROM Orders
GROUP BY month;
