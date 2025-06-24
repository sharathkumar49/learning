"""
1211. Queries Quality and Percentage (SQL)

Table: Queries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| query_name  | varchar |
| result      | varchar |
| position    | int     |
| rating      | int     |
+-------------+---------+
(query_name, result, position) is the primary key.

Write an SQL query to find the average rating of each query_name for positions 1 to 3, and the percentage of queries with rating > 3 for those positions. Round the average to 2 decimal places and the percentage to 2 decimal places.

"""
SELECT query_name,
       ROUND(AVG(rating), 2) AS quality,
       ROUND(100.0 * SUM(rating > 3) / COUNT(*), 2) AS poor_query_percentage
FROM Queries
WHERE position IN (1,2,3)
GROUP BY query_name;
