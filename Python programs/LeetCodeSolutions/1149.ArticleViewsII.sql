"""
1149. Article Views II (SQL)

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

Write an SQL query to find the IDs of all articles viewed by more than one unique viewer. Return the result table sorted by article_id in ascending order.

"""
SELECT article_id
FROM Views
GROUP BY article_id
HAVING COUNT(DISTINCT viewer_id) > 1
ORDER BY article_id;
