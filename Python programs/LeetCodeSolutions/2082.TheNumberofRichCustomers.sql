"""
LeetCode 2082. The Number of Rich Customers

Table: Customers
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| id          | int   |
| wealth      | int   |
+-------------+-------+
id is the primary key for this table.

Write an SQL query to return the number of customers with wealth > 1000000.

Example:
Customers table:
| id | wealth |
|----|--------|
| 1  | 500000 |
| 2  | 2000000|
| 3  | 1500000|

Output:
| rich_count |
|------------|
| 2          |
"""

-- SQL Solution
SELECT COUNT(*) AS rich_count
FROM Customers
WHERE wealth > 1000000;
