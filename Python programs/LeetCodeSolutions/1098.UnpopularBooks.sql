"""
1098. Unpopular Books (SQL)

Table: Books
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| name           | varchar |
+----------------+---------+
book_id is the primary key for this table.

Table: Orders
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| order_id       | int     |
| book_id        | int     |
| quantity       | int     |
| dispatch_date  | date    |
+----------------+---------+
order_id is the primary key for this table.
book_id is a foreign key to Books table.

Write an SQL query to find the books that have not been ordered in the last 1 month.

Example:
Input:
Books table:
+---------+--------------------+
| book_id | name               |
+---------+--------------------+
| 1       | "Kalila And Demna" |
| 2       | "28 Letters"       |
| 3       | "The Hobbit"       |
+---------+--------------------+
Orders table:
+----------+---------+----------+---------------+
| order_id | book_id | quantity | dispatch_date |
+----------+---------+----------+---------------+
| 1        | 1       | 2        | 2018-06-01    |
| 2        | 2       | 1        | 2018-06-02    |
| 3        | 3       | 1        | 2018-05-15    |
+----------+---------+----------+---------------+
Output:
+---------+--------------------+
| book_id | name               |
+---------+--------------------+
| 3       | "The Hobbit"       |
+---------+--------------------+
"""
SELECT b.book_id, b.name
FROM Books b
LEFT JOIN Orders o ON b.book_id = o.book_id AND o.dispatch_date > DATE_SUB('2019-06-23', INTERVAL 1 MONTH)
WHERE o.book_id IS NULL;
