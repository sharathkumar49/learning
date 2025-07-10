"""
LeetCode 1693. Daily Leads and Partners

Table: DailySales
+-------------+------+
| Column Name | Type |
+-------------+------+
| date_id     | int  |
| make_name   | varchar |
| lead_id     | int  |
| partner_id  | int  |
+-------------+------+
(date_id, make_name, lead_id, partner_id) is the primary key for this table.

Write an SQL query to report the number of unique leads and unique partners for each date_id and make_name.

Example:
Input:
DailySales table:
| date_id | make_name | lead_id | partner_id |
|---------|-----------|---------|------------|
| 20200101| toyota    | 0       | 1          |
| 20200101| toyota    | 1       | 0          |
| 20200101| toyota    | 1       | 2          |
| 20200101| honda     | 2       | 1          |
Output:
| date_id | make_name | unique_leads | unique_partners |
|---------|-----------|--------------|-----------------|
|20200101 | toyota    | 2            | 3               |
|20200101 | honda     | 1            | 1               |
"""

-- SQL Query:
SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
