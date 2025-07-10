"""
LeetCode 1795. Rearrange Products Table

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| store1      | int  |
| store2      | int  |
| store3      | int  |
+-------------+------+
(product_id) is the primary key.

Write an SQL query to rearrange the Products table so that each row has product_id, store, and price.

Example:
Products table:
| product_id | store1 | store2 | store3 |
|------------|--------|--------|--------|
| 0          | 95     | 100    | 105    |
| 1          | 70     | 80     | 90     |

Output:
| product_id | store | price |
|------------|-------|-------|
| 0          | store1| 95    |
| 0          | store2| 100   |
| 0          | store3| 105   |
| 1          | store1| 70    |
| 1          | store2| 80    |
| 1          | store3| 90    |

"""
SELECT product_id, 'store1' AS store, store1 AS price FROM Products
UNION ALL
SELECT product_id, 'store2', store2 FROM Products
UNION ALL
SELECT product_id, 'store3', store3 FROM Products;
