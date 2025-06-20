"""
607. Sales Person (SQL)
Difficulty: Easy

Table: SalesPerson
+-------------+------+
| Column Name | Type |
+-------------+------+
| sales_id    | int  |
| name        | varchar |
| salary      | int  |
| commission_rate | int |
| hire_date   | date |
+-------------+------+
sales_id is the primary key for this table.

Table: Company
+-------------+------+
| Column Name | Type |
+-------------+------+
| com_id      | int  |
| name        | varchar |
+-------------+------+
com_id is the primary key for this table.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key for this table.

Write an SQL query to report the names of all the salespersons who did not have any orders related to the company 'RED'.

Example:
SalesPerson table:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+

Company table:
+--------+--------+
| com_id | name   |
+--------+--------+
| 1      | RED    |
| 2      | ORANGE |
| 3      | YELLOW |
| 4      | GREEN  |
+--------+--------+

Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+

Result table:
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+

SQL Solution:
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
