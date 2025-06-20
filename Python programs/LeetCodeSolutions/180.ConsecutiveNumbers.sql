"""
180. Consecutive Numbers
https://leetcode.com/problems/consecutive-numbers/

Write an SQL query to find all numbers that appear at least three times consecutively.

Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | int     |
+-------------+---------+
id is the primary key for this table.

Example:
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+

Result table:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

Solution:
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.num = l2.num AND l2.num = l3.num
  AND l1.id = l2.id - 1 AND l2.id = l3.id - 1;
