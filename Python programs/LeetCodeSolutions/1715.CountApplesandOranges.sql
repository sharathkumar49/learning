"""
LeetCode 1715. Count Apples and Oranges

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| fruit       | enum('apple', 'orange') |
| quantity    | int  |
+-------------+------+
(order_id) is the primary key.

Write an SQL query to count the total number of apples and oranges ordered.

Example:
Orders table:
| order_id | fruit  | quantity |
|----------|--------|----------|
| 1        | apple  | 10       |
| 2        | orange | 5        |
| 3        | apple  | 7        |

Output:
| fruit  | total_quantity |
|--------|----------------|
| apple  | 17             |
| orange | 5              |

"""
SELECT fruit, SUM(quantity) AS total_quantity
FROM Orders
GROUP BY fruit;
