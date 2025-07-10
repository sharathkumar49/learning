"""
LeetCode 1709. Biggest Window Between Visits

Table: UserVisits
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| visit_date  | date |
+-------------+------+
(user_id, visit_date) is the primary key.

Write an SQL query to find the user_id and the biggest window (in days) between two consecutive visits for each user.

Example:
UserVisits table:
| user_id | visit_date |
|---------|------------|
| 1       | 2021-01-01 |
| 1       | 2021-01-10 |
| 1       | 2021-01-20 |
| 2       | 2021-01-05 |
| 2       | 2021-01-07 |

Output:
| user_id | biggest_window |
|---------|----------------|
| 1       | 10             |
| 2       | 2              |

"""
SELECT user_id,
       MAX(DATEDIFF(visit_date, LAG(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date))) AS biggest_window
FROM UserVisits
GROUP BY user_id;
