"""
1251. Average Selling Price (SQL)

Table: Prices
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| start_date  | date    |
| end_date    | date    |
| price       | int     |
+-------------+---------+
(product_id, start_date, end_date) is the primary key.

Table: UnitsSold
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| purchase_date | date  |
| units       | int     |
+-------------+---------+
(product_id, purchase_date) is the primary key.

Write an SQL query to find the average selling price for each product. Return the result table ordered by product_id.

"""
SELECT u.product_id, 
       ROUND(SUM(u.units * p.price) / SUM(u.units), 2) AS average_price
FROM UnitsSold u
JOIN Prices p ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id
ORDER BY u.product_id;
