"""
1205. Monthly Transactions II (SQL)

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

Write an SQL query to find the number of approved transactions and their total amount for each month and country. Return the result table ordered by country and month.

"""
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, COUNT(*) AS approved_count, SUM(amount) AS approved_amount
FROM Transactions
WHERE state = 'approved'
GROUP BY month, country
ORDER BY country, month;
