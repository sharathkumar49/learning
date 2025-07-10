"""
LeetCode 1677. Product's Worth Over Invoices

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| name        | varchar |
+-------------+------+
product_id is the primary key for this table.

Table: Invoices
+-------------+------+
| Column Name | Type |
+-------------+------+
| invoice_id  | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(invoice_id, product_id) is the primary key for this table.

Write an SQL query to report the name and total quantity of each product over all invoices.

Example:
Input:
Products table:
| product_id | name  |
|------------|-------|
| 1          | A     |
| 2          | B     |
Invoices table:
| invoice_id | product_id | quantity |
|------------|------------|----------|
| 1          | 1          | 10       |
| 2          | 1          | 20       |
| 3          | 2          | 30       |
Output:
| name  | total_quantity |
|-------|----------------|
| A     | 30             |
| B     | 30             |
"""

-- SQL Query:
SELECT p.name, SUM(i.quantity) AS total_quantity
FROM Products p
JOIN Invoices i ON p.product_id = i.product_id
GROUP BY p.name;
