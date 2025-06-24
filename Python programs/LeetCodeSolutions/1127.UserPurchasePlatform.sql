"""
1127. User Purchase Platform (SQL)

Table: Purchases
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| platform    | enum    |
| purchase_date | date  |
+-------------+---------+
(user_id, platform, purchase_date) is the primary key.

Write an SQL query to find the number of users who made purchases on each platform.

"""
SELECT platform, COUNT(DISTINCT user_id) AS user_count
FROM Purchases
GROUP BY platform;
