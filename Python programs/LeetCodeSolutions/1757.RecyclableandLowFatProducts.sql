"""
LeetCode 1757. Recyclable and Low Fat Products

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| low_fats    | enum('Y', 'N') |
| recyclable  | enum('Y', 'N') |
+-------------+------+
(product_id) is the primary key.

Write an SQL query to find the ids of products that are both low fat and recyclable.

Example:
Products table:
| product_id | low_fats | recyclable |
|------------|----------|------------|
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |

Output:
| product_id |
|------------|
| 1          |
| 3          |

"""
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
