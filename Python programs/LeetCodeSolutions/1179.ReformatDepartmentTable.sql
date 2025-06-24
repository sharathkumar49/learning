"""
1179. Reformat Department Table (SQL)

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| revenue     | int     |
| month       | varchar |
+-------------+---------+
id is the primary key.

Write an SQL query to reformat the Department table so that there is a column for each month (Jan, Feb, Mar) and the revenue for that month. Return the result table in any order.

"""
SELECT id,
       SUM(CASE WHEN month = 'Jan' THEN revenue END) AS Jan_Revenue,
       SUM(CASE WHEN month = 'Feb' THEN revenue END) AS Feb_Revenue,
       SUM(CASE WHEN month = 'Mar' THEN revenue END) AS Mar_Revenue
FROM Department
GROUP BY id;
