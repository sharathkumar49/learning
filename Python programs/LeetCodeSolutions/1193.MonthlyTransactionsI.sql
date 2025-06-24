"""
1193. Monthly Transactions I (SQL)

Table: Transactions
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| id             | int     |
| country        | varchar |
| state          | enum    |
| amount         | int     |
| trans_date     | date    |
+----------------+---------+
id is the primary key.

Write an SQL query to find the number of transactions and the total amount for each month and country. Return the result table ordered by country and month.

"""
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, COUNT(*) AS trans_count, SUM(amount) AS total_amount
FROM Transactions
GROUP BY month, country
ORDER BY country, month;
