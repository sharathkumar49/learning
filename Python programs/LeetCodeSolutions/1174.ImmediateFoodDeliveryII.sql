"""
1174. Immediate Food Delivery II (SQL)

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

Write an SQL query to find the percentage of immediate food delivery orders for each customer who has at least one order, rounded to 2 decimal places. Return the result table ordered by customer_id.

"""
SELECT customer_id,
       ROUND(100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*), 2) AS immediate_percentage
FROM Delivery
GROUP BY customer_id
ORDER BY customer_id;
