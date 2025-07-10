"""
LeetCode 1468. Calculate Salaries

Table: Employees
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | text |
| salary      | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to calculate the average, minimum, and maximum salary for all employees.

Example:
Input:
Employees table:
| id | name | salary |
|----|------|--------|
| 1  | A    | 1000   |
| 2  | B    | 2000   |
| 3  | C    | 3000   |
Output:
| average_salary | min_salary | max_salary |
|---------------|------------|------------|
| 2000          | 1000       | 3000       |
"""

-- SQL Query:
SELECT AVG(salary) AS average_salary, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM Employees;
