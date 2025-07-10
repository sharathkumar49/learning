"""
LeetCode 1789. Primary Department for Each Employee

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| department  | varchar |
| primary_flag| enum('Y', 'N') |
+-------------+------+
(employee_id, department) is the primary key.

Write an SQL query to find the primary department for each employee.

Example:
Employee table:
| employee_id | department | primary_flag |
|-------------|------------|--------------|
| 1           | A          | Y            |
| 1           | B          | N            |
| 2           | B          | Y            |

Output:
| employee_id | department |
|-------------|------------|
| 1           | A          |
| 2           | B          |

"""
SELECT employee_id, department
FROM Employee
WHERE primary_flag = 'Y';
