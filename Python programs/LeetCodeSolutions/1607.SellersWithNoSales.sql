"""
LeetCode 1607. Sellers With No Sales

Table: Sales
+-------------+------+
| Column Name | Type |
+-------------+------+
| sale_id     | int  |
| seller_id   | int  |
| product_id  | int  |
| sale_date   | date |
+-------------+------+
sale_id is the primary key for this table.

Table: Sellers
+-------------+------+
| Column Name | Type |
+-------------+------+
| seller_id   | int  |
| name        | varchar |
+-------------+------+
seller_id is the primary key for this table.

Write an SQL query to find the names of sellers who did not make any sales.

Example:
Input:
Sellers table:
| seller_id | name |
|-----------|------|
| 1         | Alice|
| 2         | Bob  |
Sales table:
| sale_id | seller_id | product_id | sale_date |
|---------|-----------|------------|-----------|
| 1       | 1         | 10         | 2020-01-01|
Output:
| name |
|------|
| Bob  |
"""

-- SQL Query:
SELECT s.name
FROM Sellers s
LEFT JOIN Sales sa ON s.seller_id = sa.seller_id
WHERE sa.seller_id IS NULL;
