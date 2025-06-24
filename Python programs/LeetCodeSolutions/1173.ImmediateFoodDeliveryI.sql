"""
1173. Immediate Food Delivery I (SQL)

Table: Delivery
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| delivery_id | int     |
| customer_id | int     |
| order_date  | date    |
| customer_pref_delivery_date | date |
+-------------+---------+
delivery_id is the primary key.

Write an SQL query to find the percentage of immediate food delivery orders (orders with order_date = customer_pref_delivery_date), rounded to 2 decimal places.

"""
SELECT ROUND(100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*), 2) AS immediate_percentage
FROM Delivery;
