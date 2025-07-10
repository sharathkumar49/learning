"""
LeetCode 1731. The Number of Employees Which Report to Each Employee

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| name        | varchar |
| reports_to  | int  |
+-------------+------+
(employee_id) is the primary key.

Write an SQL query to find the number of employees who report to each employee.

Example:
Employees table:
| employee_id | name | reports_to |
|-------------|------|------------|
| 1           | John | null       |
| 2           | Dan  | 1          |
| 3           | James| 1          |
| 4           | Amy  | 2          |

Output:
| employee_id | reports_count |
|-------------|---------------|
| 1           | 2             |
| 2           | 1             |

"""
SELECT reports_to AS employee_id, COUNT(*) AS reports_count
FROM Employees
WHERE reports_to IS NOT NULL
GROUP BY reports_to;
