"""
192. Word Frequency
https://leetcode.com/problems/word-frequency/

Write a SQL query to get the frequency of each word in the Words table.

Table: Words
+-------------+------+
| Column Name | Type |
+-------------+------+
| word        | varchar |
+-------------+------+
There is no primary key for this table. Each row contains a single word.

Example:
Words table:
+--------+
| word   |
+--------+
| the    |
| is     |
| the    |
| good   |
| is     |
+--------+

Result table:
+--------+------+
| word   | frequency |
+--------+------+
| the    | 2        |
| is     | 2        |
| good   | 1        |
+--------+------+

Solution:
SELECT word, COUNT(*) AS frequency
FROM Words
GROUP BY word;
