"""
1241. Number of Comments per Post (SQL)

Table: Submissions
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sub_id      | int     |
| parent_id   | int     |
| sub_type    | varchar |
| sub_date    | date    |
| user_id     | int     |
| content     | varchar |
+-------------+---------+
sub_id is the primary key.

Write an SQL query to find the number of comments per post. Return the result table ordered by post_id in ascending order.

"""
SELECT sub_id AS post_id, COUNT(*) AS number_of_comments
FROM Submissions
WHERE sub_type = 'comment'
GROUP BY parent_id
ORDER BY post_id;
