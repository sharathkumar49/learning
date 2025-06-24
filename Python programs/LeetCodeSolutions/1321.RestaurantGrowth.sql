"""
LeetCode 1321. Restaurant Growth

Table: Customer
+-------------+------+
| Column Name | Type |
+-------------+------+
| customer_id | int  |
| name        | varchar |
| visited_on  | date |
| amount      | int  |
+-------------+------+
(customer_id, visited_on) is the primary key.

Write an SQL query to report the average amount spent in a 7-day window for each day, rounded to 2 decimal places. Return the result table ordered by visited_on.

Example:
Customer table:
| customer_id | name | visited_on | amount |
|-------------|------|------------|--------|
| 1           | Jhon | 2019-01-01 | 100    |
| 2           | Daniel| 2019-01-02| 110    |
| 3           | Eva  | 2019-01-03 | 120    |
| 4           | Jhon | 2019-01-04 | 130    |
| 5           | Daniel| 2019-01-05| 140    |
| 6           | Eva  | 2019-01-06 | 150    |
| 7           | Jhon | 2019-01-07 | 160    |
| 8           | Daniel| 2019-01-08| 170    |
| 9           | Eva  | 2019-01-09 | 180    |

Output:
| visited_on | amount | average_amount |
|------------|--------|----------------|
| 2019-01-07 | 860    | 122.86         |
| 2019-01-08 | 980    | 140.00         |
| 2019-01-09 | 1100   | 157.14         |

"""
SELECT visited_on, SUM(amount) AS amount,
       ROUND(SUM(amount) / COUNT(DISTINCT customer_id), 2) AS average_amount
FROM (
  SELECT visited_on, amount, customer_id
  FROM Customer
  WHERE visited_on BETWEEN DATE_SUB(visited_on, INTERVAL 6 DAY) AND visited_on
) t
GROUP BY visited_on
HAVING COUNT(DISTINCT customer_id) = 7
ORDER BY visited_on;
