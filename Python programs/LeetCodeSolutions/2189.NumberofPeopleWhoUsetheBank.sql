"""
LeetCode 2189. Number of People Who Use the Bank

Table: BankTransactions
+----------------+------+
| Column Name    | Type |
+----------------+------+
| account_id     | int  |
| transaction_id | int  |
| amount         | int  |
+----------------+------+
transaction_id is the primary key.

Write an SQL query to report the number of unique people (account_id) who have used the bank.

Example:
BankTransactions table:
| account_id | transaction_id | amount |
|------------|---------------|--------|
| 1          | 101           | 100    |
| 2          | 102           | 200    |
| 1          | 103           | 50     |

Output:
| people_count |
|--------------|
| 2            |

Solution:
SELECT COUNT(DISTINCT account_id) AS people_count
FROM BankTransactions;
