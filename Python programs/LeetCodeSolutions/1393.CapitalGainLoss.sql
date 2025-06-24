"""
LeetCode 1393. Capital Gain/Loss

Table: Stocks
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key for this table.
operation is an ENUM of the type ('Sell', 'Buy'), and price is the price of the stock at that day.

Write an SQL query to report the Capital gain/loss for each stock.

Example:
Input:
Stocks table:
| stock_name | operation | operation_day | price |
|------------|-----------|---------------|-------|
| Leetcode   | Buy       | 1             | 1000  |
| Leetcode   | Sell      | 5             | 900   |
| Leetcode   | Buy       | 10            | 1000  |
| Leetcode   | Sell      | 15            | 1200  |

Output:
| stock_name | capital_gain_loss |
|------------|------------------|
| Leetcode   | 100              |

"""

--SQL Query:
SELECT stock_name, SUM(
    CASE WHEN operation = 'Sell' THEN price ELSE -price END
) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
