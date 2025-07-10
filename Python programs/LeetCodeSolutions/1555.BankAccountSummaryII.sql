"""
LeetCode 1555. Bank Account Summary II

Table: Transactions
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| day         | date |
| type        | text |
| amount      | int  |
+-------------+------+
(account_id, day) is the primary key for this table.

Write an SQL query to report the balance of each account at the end of each day.

Example:
Input:
Transactions table:
| account_id | day        | type   | amount |
|------------|------------|--------|--------|
| 1          | 2025-06-01 | Deposit| 100    |
| 1          | 2025-06-02 | Withdraw| 50    |
| 2          | 2025-06-01 | Deposit| 200    |
Output:
| account_id | day        | balance |
|------------|------------|---------|
| 1          | 2025-06-01 | 100     |
| 1          | 2025-06-02 | 50      |
| 2          | 2025-06-01 | 200     |
"""

-- SQL Query:
SELECT account_id, day,
       SUM(CASE WHEN type = 'Deposit' THEN amount ELSE -amount END) OVER (PARTITION BY account_id ORDER BY day) AS balance
FROM Transactions;
