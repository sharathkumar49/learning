"""
LeetCode 1821. Find Customers With Positive Revenue this Year

Table: Customers
+-------------+------+
| Column Name | Type |
+-------------+------+
| customer_id | int  |
| year        | int  |
| revenue     | int  |
+-------------+------+
(customer_id, year) is the primary key.

Write an SQL query to find the customer_id of customers with positive revenue in the current year (2025).

Example:
Customers table:
| customer_id | year | revenue |
|-------------|------|---------|
| 1           | 2025 | 100     |
| 2           | 2024 | 200     |
| 3           | 2025 | 0       |

Output:
| customer_id |
|-------------|
| 1           |

"""
SELECT customer_id
FROM Customers
WHERE year = 2025 AND revenue > 0;
