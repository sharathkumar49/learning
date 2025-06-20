"""
1084. Sales Analysis III (SQL)

Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| product_name| varchar |
| unit_price  | int     |
+-------------+---------+
product_id is the primary key for this table.

Table: Sales
+-------------+------+ 
| Column Name | Type |
+-------------+------+
| seller_id   | int  |
| product_id  | int  |
| buyer_id    | int  |
| sale_date   | date |
| quantity    | int  |
| price       | int  |
+-------------+------+
This table has no primary key, it can have repeated rows.
product_id is a foreign key to Product table.

Write an SQL query that reports the names of all the products that were sold in the first quarter of 2019 and their total quantity sold.

Example:
Input:
Product table:
+-------------+--------------+------------+
| product_id  | product_name | unit_price |
+-------------+--------------+------------+
| 1           | S8           | 1000       |
| 2           | G4           | 800        |
| 3           | iPhone       | 1400       |
+-------------+--------------+------------+

Sales table:
+-----------+------------+---------+------------+----------+-------+
| seller_id | product_id | buyer_id| sale_date  | quantity | price |
+-----------+------------+---------+------------+----------+-------+
| 1         | 1          | 1       | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2       | 2019-02-17 | 1        | 800   |
| 2         | 1          | 3       | 2019-06-02 | 1        | 1000  |
| 3         | 3          | 3       | 2019-05-13 | 2        | 2800  |
+-----------+------------+---------+------------+----------+-------+
Output:
+--------------+----------------+
| product_name | total_quantity |
+--------------+----------------+
| S8           | 2              |
| G4           | 1              |
+--------------+----------------+
"""
SELECT p.product_name, SUM(s.quantity) AS total_quantity
FROM Sales s
JOIN Product p ON s.product_id = p.product_id
WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY p.product_name;
