"""
584. Find Customer Referee (SQL)
Difficulty: Easy

Table: Customer
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| referee_id  | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to report the names of the customers who are not referred by the customer with id = 2.

Example:
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+

Result table:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

SQL Solution:
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
