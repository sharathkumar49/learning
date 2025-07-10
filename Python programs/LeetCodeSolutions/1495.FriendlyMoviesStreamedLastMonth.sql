"""
LeetCode 1495. Friendly Movies Streamed Last Month

Table: Movies
+-------------+------+
| Column Name | Type |
+-------------+------+
| movie_id    | int  |
| title       | text |
+-------------+------+
movie_id is the primary key for this table.

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| name        | text |
+-------------+------+
user_id is the primary key for this table.

Table: MovieViews
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| movie_id    | int  |
| view_date   | date |
+-------------+------+
(user_id, movie_id, view_date) is the primary key for this table.

Write an SQL query to find the titles of all movies that have been viewed by at least one user in the last month.

Example:
Input:
Movies table:
| movie_id | title     |
|----------|-----------|
| 1        | MovieA    |
| 2        | MovieB    |
| 3        | MovieC    |
Users table:
| user_id | name      |
|---------|-----------|
| 1       | Alice     |
| 2       | Bob       |
MovieViews table:
| user_id | movie_id | view_date  |
|---------|----------|------------|
| 1       | 1        | 2025-05-15 |
| 2       | 2        | 2025-06-10 |
| 1       | 3        | 2025-06-20 |
Output:
| title  |
|--------|
| MovieB |
| MovieC |
"""

-- SQL Query:
SELECT DISTINCT m.title
FROM Movies m
JOIN MovieViews v ON m.movie_id = v.movie_id
WHERE v.view_date >= DATE('now', '-1 month');
