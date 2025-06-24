"""
1126. Active Businesses (SQL)

Table: Events
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| business_id | int     |
| event_type  | enum    |
| occur_date  | date    |
+-------------+---------+
(business_id, event_type, occur_date) is the primary key.

Write an SQL query to find the number of businesses that were active on each day. A business is active if it has at least one event on that day.

"""
SELECT occur_date, COUNT(DISTINCT business_id) AS active_businesses
FROM Events
GROUP BY occur_date;
