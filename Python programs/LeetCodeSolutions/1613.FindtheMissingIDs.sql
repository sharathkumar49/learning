"""
LeetCode 1613. Find the Missing IDs

Table: Customers
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
+-------------+------+
id is the primary key for this table.

Write an SQL query to find the missing customer IDs in the range from 1 to the maximum id present in the table.

Example:
Input:
Customers table:
| id |
|----|
| 1  |
| 2  |
| 4  |
| 6  |
Output:
| ids |
|-----|
| 3   |
| 5   |
"""

-- SQL Query:
WITH RECURSIVE nums AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n+1 FROM nums WHERE n < (SELECT MAX(id) FROM Customers)
)
SELECT n AS ids
FROM nums
WHERE n NOT IN (SELECT id FROM Customers);
