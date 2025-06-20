"""
1045. Customers Who Bought All Products (SQL)

Table: Customer
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| customer_id | int   |
| product_key | int   |
+-------------+-------+
This table has no primary key, it may contain duplicates.
product_key is a foreign key to Product table.

Table: Product
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| product_key | int   |
+-------------+-------+
product_key is the primary key for this table.

Write an SQL query to report the customer ids from the Customer table who bought all the products in the Product table.

Example:
Input:
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
Output:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
"""
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
