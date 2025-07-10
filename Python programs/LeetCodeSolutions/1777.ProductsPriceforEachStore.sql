"""
LeetCode 1777. Product's Price for Each Store

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| store       | int  |
| price       | int  |
+-------------+------+
(product_id, store) is the primary key.

Write an SQL query to find the price of each product in each store.

Example:
Products table:
| product_id | store | price |
|------------|-------|-------|
| 1          | 1     | 100   |
| 1          | 2     | 200   |
| 2          | 1     | 150   |

Output:
| product_id | store | price |
|------------|-------|-------|
| 1          | 1     | 100   |
| 1          | 2     | 200   |
| 2          | 1     | 150   |

"""
SELECT product_id, store, price
FROM Products;
