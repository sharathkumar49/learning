"""
LeetCode 1327. List the Products Ordered in a Period

Table: Products
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| product_name| varchar |
+-------------+------+
product_id is the primary key.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| product_id  | int  |
| order_date  | date |
+-------------+------+
(product_id, order_date) is the primary key.

Write an SQL query to list the product names ordered between '2020-02-01' and '2020-02-29'. Return the result table in any order.

Example:
Products table:
| product_id | product_name |
|------------|--------------|
| 1          | Leetcode     |
| 2          | T-shirt      |
| 3          | Book         |

Orders table:
| product_id | order_date   |
|------------|-------------|
| 1          | 2020-02-10   |
| 2          | 2020-01-18   |
| 3          | 2020-02-25   |

Output:
| product_name |
|--------------|
| Leetcode     |
| Book         |

"""
SELECT DISTINCT p.product_name
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29';
