"""
LeetCode 1303. Find the Team Size

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| team_id     | int  |
+-------------+------+
(employee_id, team_id) is the primary key.

Write an SQL query to find the team size of each team. Return the result table in any order.

Example:
Employee table:
| employee_id | team_id |
|-------------|---------|
| 1           | 8       |
| 2           | 8       |
| 3           | 8       |
| 4           | 7       |
| 5           | 9       |
| 6           | 9       |

Output:
| team_id | team_size |
|---------|-----------|
| 7       | 1         |
| 8       | 3         |
| 9       | 2         |

"""
SELECT team_id, COUNT(employee_id) AS team_size
FROM Employee
GROUP BY team_id;
