"""
LeetCode 1581. Customer Who Visited but Did Not Make Any Transactions

Table: Visits
+-------------+------+
| Column Name | Type |
+-------------+------+
| visit_id    | int  |
| customer_id | int  |
+-------------+------+
visit_id is the primary key for this table.

Table: Transactions
+----------------+------+
| Column Name    | Type |
+----------------+------+
| transaction_id | int  |
| visit_id       | int  |
+----------------+------+
transaction_id is the primary key for this table.

Write an SQL query to find the customer_id of customers who visited but did not make any transactions.

Example:
Input:
Visits table:
| visit_id | customer_id |
|----------|-------------|
| 1        | 23          |
| 2        | 9           |
| 3        | 30          |
| 4        | 54          |
| 5        | 96          |
Transactions table:
| transaction_id | visit_id |
|----------------|----------|
| 2              | 5        |
| 3              | 1        |
Output:
| customer_id |
|-------------|
| 9           |
| 30          |
| 54          |
"""

-- SQL Query:
SELECT DISTINCT v.customer_id
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL;
