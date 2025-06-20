"""
620. Not Boring Movies (SQL)
Difficulty: Easy

Table: Cinema
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| movie       | varchar |
| description | varchar |
| rating      | float |
+-------------+------+
id is the primary key for this table.

Write an SQL query to report the movies with an odd-numbered id and a description that is not "boring". Return the result sorted by rating in descending order.

Example:
Cinema table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |
+----+------------+-------------+--------+

Result table:
+----+------------+-------------+--------+
| id | movie      | description | rating |
+----+------------+-------------+--------+
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |
+----+------------+-------------+--------+

SQL Solution:
SELECT *
FROM Cinema
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC;
