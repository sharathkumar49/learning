"""
LeetCode 1270. All People Report to the Given Manager

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| name        | varchar |
| manager_id  | int  |
+-------------+------+
(employee_id) is the primary key for this table.
Each employee has a manager. If manager_id is null, that employee has no manager.

Write an SQL query to find all employees who report to a given manager (directly or indirectly). Return the employee_id and name of these employees.

Example:
Employees table:
| employee_id | name  | manager_id |
|-------------|-------|------------|
| 1           | Alice | 3          |
| 2           | Bob   | 3          |
| 3           | Carol | null       |
| 4           | Dave  | 1          |

If the given manager_id is 3, the result should include Alice, Bob, and Dave.

"""
WITH RECURSIVE subordinates AS (
  SELECT employee_id, name, manager_id
  FROM Employees
  WHERE manager_id = 3
  UNION ALL
  SELECT e.employee_id, e.name, e.manager_id
  FROM Employees e
  JOIN subordinates s ON e.manager_id = s.employee_id
)
SELECT employee_id, name FROM subordinates;
