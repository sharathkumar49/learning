"""
LeetCode 1421. NPV Queries

Table: Transactions
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
+---------------+---------+
id is the primary key for this table.
state is an ENUM of type ('approved', 'declined').

Write an SQL query to report the net present value (NPV) for each country. NPV is defined as the sum of the amounts for approved transactions minus the sum of the amounts for declined transactions.

Example:
Input:
Transactions table:
| id | country | state     | amount |
|----|---------|-----------|--------|
| 1  | US      | approved  | 100    |
| 2  | US      | declined  | 200    |
| 3  | US      | approved  | 200    |
| 4  | US      | declined  | 100    |
| 5  | CA      | approved  | 200    |
Output:
| country | npv |
|---------|-----|
| US      | 0   |
| CA      | 200 |
"""

--SQL Query:
SELECT country, SUM(CASE WHEN state = 'approved' THEN amount ELSE -amount END) AS npv
FROM Transactions
GROUP BY country;
