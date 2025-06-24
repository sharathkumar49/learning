"""
LeetCode 1357. Apply Discount Every n Orders

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| customer_id | int  |
| order_date  | date |
| price       | int  |
+-------------+------+
order_id is the primary key.

Write an SQL query to report the price of every order after applying a 10% discount to every 3rd order (in order of order_date).

Example:
Orders table:
| order_id | customer_id | order_date | price |
|----------|-------------|------------|-------|
| 1        | 1           | 2020-01-01 | 100   |
| 2        | 2           | 2020-01-02 | 200   |
| 3        | 3           | 2020-01-03 | 300   |
| 4        | 4           | 2020-01-04 | 400   |

Output:
| order_id | price |
|----------|-------|
| 1        | 100   |
| 2        | 200   |
| 3        | 270   |
| 4        | 400   |

"""
SELECT order_id,
       CASE WHEN (ROW_NUMBER() OVER (ORDER BY order_date)) % 3 = 0
            THEN price * 0.9
            ELSE price
       END AS price
FROM Orders;
