"""
182. Duplicate Emails
https://leetcode.com/problems/duplicate-emails/

Write an SQL query to find all duplicate emails in a table named Person.

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key for this table.

Example:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

Result table:
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

Solution:
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
