"""
LeetCode 1308. Running Total for Different Genders

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| gender      | varchar |
| salary      | int  |
+-------------+------+
id is the primary key.

Write an SQL query to report the running total of salary for each gender, ordered by gender and id.

Example:
Employees table:
| id | name | gender | salary |
|----|------|--------|--------|
| 1  | A    | M      | 1000   |
| 2  | B    | F      | 1500   |
| 3  | C    | M      | 1200   |
| 4  | D    | F      | 1300   |

Output:
| id | gender | running_total |
|----|--------|---------------|
| 1  | M      | 1000          |
| 3  | M      | 2200          |
| 2  | F      | 1500          |
| 4  | F      | 2800          |

"""
SELECT id, gender, SUM(salary) OVER (PARTITION BY gender ORDER BY id) AS running_total
FROM Employees
ORDER BY gender, id;
