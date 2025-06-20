"""
586. Customer Placing the Largest Number of Orders (SQL)
Difficulty: Easy

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_number| int  |
| customer_number | int |
+-------------+------+
order_number is the primary key for this table.

Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.

Example:
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+

Result table:
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+

SQL Solution:
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
