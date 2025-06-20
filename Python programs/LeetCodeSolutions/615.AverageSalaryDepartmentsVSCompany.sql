"""
615. Average Salary: Departments VS Company (SQL)
Difficulty: Hard

Table: Salary
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| employee_id | int  |
| amount      | int  |
| pay_date    | date |
+-------------+------+
id is the primary key for this table.

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| employee_id | int  |
| department_id | int |
+-------------+------+
employee_id is the primary key for this table.

Write an SQL query to find the department id(s) where the average salary is higher than the company's average salary in May 2013. The result should have columns department_id and average_salary, rounded to 2 decimal places.

Example:
Salary table:
+----+-------------+--------+------------+
| id | employee_id | amount | pay_date   |
+----+-------------+--------+------------+
| 1  | 1           | 9000   | 2013-05-23 |
| 2  | 2           | 6000   | 2013-05-23 |
| 3  | 3           | 10000  | 2013-05-23 |
| 4  | 1           | 8000   | 2013-06-23 |
| 5  | 2           | 6000   | 2013-06-23 |
| 6  | 3           | 10000  | 2013-06-23 |
+----+-------------+--------+------------+

Employee table:
+-------------+--------------+
| employee_id | department_id|
+-------------+--------------+
| 1           | 1            |
| 2           | 2            |
| 3           | 2            |
+-------------+--------------+

Result table:
+--------------+----------------+
| department_id| average_salary |
+--------------+----------------+
| 1            | 9000.00        |
+--------------+----------------+
"""

-- SQL Solution:
WITH MaySalary AS (
  SELECT s.employee_id, e.department_id, s.amount
  FROM Salary s
  JOIN Employee e ON s.employee_id = e.employee_id
  WHERE s.pay_date BETWEEN '2013-05-01' AND '2013-05-31'
),
CompanyAvg AS (
  SELECT ROUND(AVG(amount), 2) AS avg_salary FROM MaySalary
)
SELECT department_id, ROUND(AVG(amount), 2) AS average_salary
FROM MaySalary
GROUP BY department_id
HAVING AVG(amount) > (SELECT avg_salary FROM CompanyAvg);
