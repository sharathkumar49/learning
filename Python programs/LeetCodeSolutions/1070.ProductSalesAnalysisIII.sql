"""
1070. Product Sales Analysis III (SQL)

Table: Sales
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
sale_id is the primary key of this table.
Each row of this table shows a sale on the product product_id in a certain year.

Write an SQL query that reports the product_id and total quantity for every product_id in the Sales table.

Example:
Input:
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Output:
+------------+---------------+
| product_id | total_quantity|
+------------+---------------+
| 100        | 22            |
| 200        | 15            |
+------------+---------------+
"""
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id;
