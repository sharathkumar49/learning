"""
LeetCode 1407. Top Travellers

Table: Users
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| name        | varchar|
+-------------+-------+
id is the primary key for this table.

Table: Rides
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| user_id     | int   |
| distance    | int   |
+-------------+-------+
id is the primary key for this table.
user_id is a foreign key to Users table.

Write an SQL query to report the distance travelled by each user. If a user did not travel any distance, their distance should be 0. Order the result table by travelled_distance in descending order, and by name in ascending order in case of a tie.

Example:
Input:
Users table:
| id | name    |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Alex    |
| 4  | Donald  |
| 7  | Lee     |
| 13 | Jonathan|
| 19 | Elvis   |
Rides table:
| id | user_id | distance |
|----|---------|----------|
| 1  | 1       | 120      |
| 2  | 2       | 317      |
| 3  | 3       | 222      |
| 4  | 7       | 100      |
| 5  | 13      | 312      |
| 6  | 19      | 50       |
| 7  | 7       | 120      |
| 8  | 19      | 400      |
| 9  | 7       | 230      |
Output:
| name    | travelled_distance |
|---------|-------------------|
| Elvis   | 450               |
| Lee     | 450               |
| Bob     | 317               |
| Jonathan| 312               |
| Alex    | 222               |
| Alice   | 120               |
| Donald  | 0                 |
"""

--SQL Query:
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
