"""
1164. Product Price at a Given Date (SQL)

Table: Products
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| start_date   | date    |
| end_date     | date    |
| price        | int     |
+--------------+---------+
(product_id, start_date, end_date) is the primary key.

Write an SQL query to find the price of each product on 2019-08-16. If the product was not available on that day, report null.

"""
SELECT product_id, price
FROM Products
WHERE '2019-08-16' BETWEEN start_date AND end_date
UNION
SELECT product_id, NULL AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id FROM Products WHERE '2019-08-16' BETWEEN start_date AND end_date
);
