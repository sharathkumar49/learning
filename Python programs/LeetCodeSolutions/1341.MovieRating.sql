"""
LeetCode 1341. Movie Rating

Table: Movies
+-------------+------+
| Column Name | Type |
+-------------+------+
| movie_id    | int  |
| title       | varchar |
+-------------+------+
movie_id is the primary key.

Table: Users
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| name        | varchar |
+-------------+------+
user_id is the primary key.

Table: MovieRating
+-------------+------+
| Column Name | Type |
+-------------+------+
| movie_id    | int  |
| user_id     | int  |
| rating      | int  |
| created_at  | date |
+-------------+------+
(movie_id, user_id) is the primary key.

Write an SQL query to find the movie with the highest average rating and the user who rated the most movies in February 2020.

Example:
(See LeetCode for full details.)

"""
-- This problem requires aggregation and filtering by date.
-- See LeetCode for full schema and requirements.
