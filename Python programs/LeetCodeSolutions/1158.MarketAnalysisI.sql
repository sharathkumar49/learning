"""
1158. Market Analysis I (SQL)

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

Write an SQL query to find for each user the join date and the number of orders they made as a buyer in 2019.

"""
SELECT u.user_id, u.join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
