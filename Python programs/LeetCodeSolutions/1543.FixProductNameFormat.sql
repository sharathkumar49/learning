"""
LeetCode 1543. Fix Product Name Format

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| product_name| text |
+-------------+------+
product_id is the primary key for this table.

Write an SQL query to fix the product_name format so that the first letter is uppercase and the rest are lowercase.

Example:
Input:
Products table:
| product_id | product_name |
|------------|--------------|
| 1          | apple        |
| 2          | BANANA       |
| 3          | Orange       |
Output:
| product_id | product_name |
|------------|--------------|
| 1          | Apple        |
| 2          | Banana       |
| 3          | Orange       |
"""

-- SQL Query:
SELECT product_id, UPPER(SUBSTR(product_name, 1, 1)) || LOWER(SUBSTR(product_name, 2)) AS product_name
FROM Products;
