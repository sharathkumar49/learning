"""
LeetCode 1831. Maximum Transaction Each Day

Table: Transactions
+-------------+------+
| Column Name | Type |
+-------------+------+
| transaction_id | int  |
| day           | date |
| amount        | int  |
+-------------+------+
(transaction_id) is the primary key.

Write an SQL query to find the maximum transaction amount for each day.

Example:
Transactions table:
| transaction_id | day        | amount |
|----------------|------------|--------|
| 1              | 2025-06-01 | 100    |
| 2              | 2025-06-01 | 200    |
| 3              | 2025-06-02 | 150    |

Output:
| day        | max_amount |
|------------|------------|
| 2025-06-01 | 200        |
| 2025-06-02 | 150        |

"""
SELECT day, MAX(amount) AS max_amount
FROM Transactions
GROUP BY day;
