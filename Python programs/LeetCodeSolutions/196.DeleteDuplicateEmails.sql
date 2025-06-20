"""
196. Delete Duplicate Emails
https://leetcode.com/problems/delete-duplicate-emails/

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only the smallest id for each email.

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
| 2  | b@b.com |
| 3  | a@b.com |
+----+---------+

After running your SQL query, the above Person table should have the following rows:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | b@b.com |
+----+---------+

Solution:
DELETE p1 FROM Person p1
JOIN Person p2
ON p1.email = p2.email AND p1.id > p2.id;
