"""
LeetCode 2205. The Number of Users That Are Eligible for Discount

Table: Purchases
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| user_id     | int      |
| time_stamp  | datetime |
| amount      | int      |
+-------------+----------+
(user_id, time_stamp) is the primary key.
Each row contains the user id, purchase time, and amount.

Write a function to calculate number of users who will be eligible for a discount if they have purchased items in an interval of time.

Example:
Input: 
Purchases table:
+---------+---------------------+--------+
| user_id | time_stamp         | amount |
+---------+---------------------+--------+
| 1       | 2022-04-20 09:03:00| 100    |
| 1       | 2022-04-20 09:05:00| 200    |
| 2       | 2022-04-20 09:10:00| 150    |
+---------+---------------------+--------+
start_date = 2022-04-20 09:00:00
end_date = 2022-04-20 09:07:00
min_amount = 200

Output: 1

Solution:
CREATE FUNCTION getUserIDs(start_date DATE, end_date DATE, min_amount INT)
RETURNS INT
BEGIN
    RETURN (
        SELECT COUNT(DISTINCT user_id) 
        FROM Purchases
        WHERE time_stamp BETWEEN start_date AND end_date
        AND amount >= min_amount
    );
END
