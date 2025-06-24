"""
1148. Article Views I (SQL)

Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
(article_id, view_date) is the primary key for this table.

Write an SQL query to find all the authors that viewed at least one of their own articles. Return the result table sorted by id in ascending order.

"""
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
