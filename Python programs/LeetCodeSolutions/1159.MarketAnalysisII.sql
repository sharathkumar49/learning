"""
1159. Market Analysis II (SQL)

Table: Users
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| join_date   | date    |
| favorite_brand | int  |
+-------------+---------+
user_id is the primary key.

Table: Orders
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| order_id    | int     |
| order_date  | date    |
| item_id     | int     |
| buyer_id    | int     |
| seller_id   | int     |
+-------------+---------+
order_id is the primary key.

Table: Items
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| item_id     | int     |
| item_brand  | int     |
+-------------+---------+
item_id is the primary key.

Write an SQL query to find the percentage of users who made at least one order in 2019. Round the result to 2 decimal places.

"""
SELECT ROUND(100.0 * COUNT(DISTINCT o.buyer_id) / (SELECT COUNT(*) FROM Users), 2) AS percentage_users
FROM Orders o
WHERE YEAR(o.order_date) = 2019;
