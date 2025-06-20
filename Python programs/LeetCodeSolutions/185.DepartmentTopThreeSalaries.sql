"""
185. Department Top Three Salaries
https://leetcode.com/problems/department-top-three-salaries/

Write an SQL query to find the top three salaries in each department. If there are less than three salaries, return all of them.

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| departmentId| int     |
+-------------+---------+
id is the primary key for this table.

Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key for this table.

Example:
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
+----+-------+--------+--------------+

Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+

Result table:
+------------+-------+--------+
| Department | Name  | Salary |
+------------+-------+--------+
| IT         | Max   | 90000  |
| IT         | Joe   | 85000  |
| IT         | Randy | 85000  |
| Sales      | Henry | 80000  |
| Sales      | Sam   | 60000  |
+------------+-------+--------+

Solution:
SELECT d.name AS Department, e.name AS Name, e.salary AS Salary
FROM (
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk <= 3;
