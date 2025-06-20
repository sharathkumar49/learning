"""
619. Biggest Single Number (SQL)
Difficulty: Easy

Table: MyNumbers
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
num is the primary key for this table.

A single number is a number that appears only once in the table. Write an SQL query to report the largest single number. If there is no single number, report null.

Example:
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+

Result table:
+-----+
| num |
+-----+
| 6   |
+-----+

SQL Solution:
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(*) = 1
);
