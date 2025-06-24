"""
LeetCode 1336. Number of Transactions per Visit

Table: Visits
+-------------+------+
| Column Name | Type |
+-------------+------+
| visit_id    | int  |
| customer_id | int  |
+-------------+------+
visit_id is the primary key.

Table: Transactions
+-------------+------+
| Column Name | Type |
+-------------+------+
| transaction_id | int  |
| visit_id       | int  |
+-------------+------+
transaction_id is the primary key.

Write an SQL query to report the number of transactions per visit for each visit_id.

Example:
Visits table:
| visit_id | customer_id |
|----------|-------------|
| 1        | 23          |
| 2        | 9           |
| 3        | 30          |

Transactions table:
| transaction_id | visit_id |
|----------------|----------|
| 2              | 1        |
| 3              | 1        |
| 9              | 2        |

Output:
| visit_id | transactions_count |
|----------|--------------------|
| 1        | 2                  |
| 2        | 1                  |
| 3        | 0                  |

"""
SELECT v.visit_id, COUNT(t.transaction_id) AS transactions_count
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
GROUP BY v.visit_id;
