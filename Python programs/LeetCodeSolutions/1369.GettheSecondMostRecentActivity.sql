"""
LeetCode 1369. Get the Second Most Recent Activity

Table: UserActivity
+-------------+------+
| Column Name | Type |
+-------------+------+
| username    | varchar |
| activity    | varchar |
| startDate   | date |
| endDate     | date |
+-------------+------+
(username, activity) is the primary key.

Write an SQL query to get the second most recent activity for each user.

Example:
UserActivity table:
| username | activity | startDate  | endDate    |
|----------|----------|------------|------------|
| Alice    | A1       | 2020-01-01 | 2020-01-02 |
| Alice    | A2       | 2020-01-03 | 2020-01-04 |
| Bob      | B1       | 2020-01-02 | 2020-01-03 |
| Bob      | B2       | 2020-01-04 | 2020-01-05 |

Output:
| username | activity | startDate  | endDate    |
|----------|----------|------------|------------|
| Alice    | A1       | 2020-01-01 | 2020-01-02 |
| Bob      | B1       | 2020-01-02 | 2020-01-03 |

"""
SELECT username, activity, startDate, endDate
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY username ORDER BY endDate DESC) AS rn
  FROM UserActivity
) t
WHERE rn = 2;
