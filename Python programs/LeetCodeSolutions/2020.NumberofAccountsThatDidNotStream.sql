"""
LeetCode 2020. Number of Accounts That Did Not Stream

Table: Accounts
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| account_id  | int   |
+-------------+-------+
account_id is the primary key for this table.

Table: Streams
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| account_id  | int   |
+-------------+-------+
account_id is a foreign key to Accounts.

Write an SQL query to return the number of accounts that did not stream any content.

Example:
Accounts table:
| account_id |
|------------|
| 1          |
| 2          |
| 3          |

Streams table:
| account_id |
|------------|
| 1          |
| 2          |

Output:
| accounts_count |
|---------------|
| 1             |
"""

-- SQL Solution
SELECT COUNT(*) AS accounts_count
FROM Accounts
WHERE account_id NOT IN (SELECT account_id FROM Streams);
