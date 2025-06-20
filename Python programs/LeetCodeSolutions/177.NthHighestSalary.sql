"""
177. Nth Highest Salary
https://leetcode.com/problems/nth-highest-salary/

SQL Schema:
Employee table: id, salary

Write a SQL query to get the nth highest salary from the Employee table. If there is no nth highest salary, the query should return null.

Example:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| getNthHighestSalary |
+---------------------+
| 100                 |
+---------------------+
"""
-- SQL Solution
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N-1
  );
END
