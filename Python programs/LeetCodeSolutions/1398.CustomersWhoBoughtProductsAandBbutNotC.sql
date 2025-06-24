"""
LeetCode 1398. Customers Who Bought Products A and B but Not C

Table: Orders
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| customer_id | int   |
| product_name| char  |
+-------------+-------+
(customer_id, product_name) is the primary key for this table.

Write an SQL query to report the customer_id's who bought products 'A' and 'B' but did not buy product 'C'.

Example:
Input:
Orders table:
| customer_id | product_name |
|-------------|--------------|
| 1           | A            |
| 1           | B            |
| 1           | C            |
| 2           | A            |
| 2           | B            |
| 3           | A            |
| 3           | B            |
| 3           | D            |
Output:
| customer_id |
|-------------|
| 2           |
| 3           |
"""

--SQL Query:
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0;
