"""
LeetCode 1587. Bank Account Summary II

Table: Users
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key for this table.

Table: Transactions
+----------------+------+
| Column Name    | Type |
+----------------+------+
| trans_id       | int  |
| account        | int  |
| amount         | int  |
+----------------+------+
trans_id is the primary key for this table.

Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Example:
Input:
Users table:
| account | name |
|---------|------|
| 900001  | Alice|
| 900002  | Bob  |
Transactions table:
| trans_id | account | amount |
|----------|---------|--------|
| 1        | 900001  | 7000   |
| 2        | 900001  | 7000   |
| 3        | 900002  | 4000   |
Output:
| name  | balance |
|-------|---------|
| Alice | 14000   |
"""

-- SQL Query:
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
