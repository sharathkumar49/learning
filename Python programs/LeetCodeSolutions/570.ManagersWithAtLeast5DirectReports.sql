"""
570. Managers with at Least 5 Direct Reports (SQL)
Difficulty: Medium

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| name        | varchar |
| department  | varchar |
| managerId   | int  |
+-------------+------+
id is the primary key for this table.
managerId is the id of the manager. If managerId is null, then the employee does not have a manager.

Write an SQL query to report the managers with at least 5 direct reports.

Example:
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+

Result table:
+-------+
| name  |
+-------+
| John  |
+-------+
"""
-- SQL Solution:
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);
