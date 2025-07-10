"""
LeetCode 1701. Average Waiting Time

Table: Customers
+-------------+------+ 
| Column Name | Type | 
+-------------+------+
| customer_id | int  |
| arrival     | int  |
| time        | int  |
+-------------+------+
customer_id is the primary key for this table.

Write an SQL query to return the average waiting time of all customers. The waiting time of a customer is the time from when they arrive to when they finish their order.

Example:
Customers table:
| customer_id | arrival | time |
|-------------|---------|------|
| 1           | 1       | 2    |
| 2           | 2       | 5    |
| 3           | 3       | 1    |

Output:
| average_waiting_time |
|---------------------|
| 3.66667             |

"""

SELECT
    ROUND(AVG(waiting_time), 5) AS average_waiting_time
FROM (
    SELECT
        arrival,
        time,
        SUM(time) OVER (ORDER BY arrival ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) - arrival AS waiting_time
    FROM Customers
) t;
