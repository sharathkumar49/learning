"""
262. Trips and Users
https://leetcode.com/problems/trips-and-users/

SQL Schema:
Trips table:
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| Id          | int      |
| Client_Id   | int      |
| Driver_Id   | int      |
| City_Id     | int      |
| Status      | enum     |
| Request_at  | date     |
+-------------+----------+
Id is the primary key for this table.
Status is an ENUM type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').

Users table:
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| Users_Id    | int      |
| Banned      | enum     |
| Role        | enum     |
+-------------+----------+
Users_Id is the primary key for this table.
Role is an ENUM type of ('client', 'driver', 'partner').
Banned is an ENUM type of ('Yes', 'No').

Write an SQL query to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". The cancellation rate is calculated by dividing the number of canceled (by client or driver) requests by the total number of requests on that day.

Return the result table in any order.

Solution:
SELECT Request_at AS Day,
       ROUND(SUM(Status != 'completed') / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips t
JOIN Users c ON t.Client_Id = c.Users_Id AND c.Banned = 'No'
JOIN Users d ON t.Driver_Id = d.Users_Id AND d.Banned = 'No'
WHERE Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at;
