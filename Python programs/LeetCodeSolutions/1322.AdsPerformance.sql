"""
LeetCode 1322. Ads Performance

Table: Ads
+-------------+------+
| Column Name | Type |
+-------------+------+
| ad_id       | int  |
| user_id     | int  |
| action      | enum('Clicked', 'Viewed', 'Ignored') |
+-------------+------+
(ad_id, user_id) is the primary key.

Write an SQL query to report the CTR (Click-Through Rate) of each ad. CTR is Clicks / Views, rounded to 2 decimal places. Return the result table ordered by ad_id.

Example:
Ads table:
| ad_id | user_id | action  |
|-------|---------|---------|
| 1     | 1       | Clicked |
| 2     | 2       | Viewed  |
| 3     | 3       | Ignored |
| 1     | 4       | Viewed  |
| 2     | 5       | Clicked |

Output:
| ad_id | ctr  |
|-------|------|
| 1     | 0.50 |
| 2     | 1.00 |
| 3     | 0.00 |

"""
SELECT ad_id,
       ROUND(SUM(action = 'Clicked') / NULLIF(SUM(action = 'Viewed' OR action = 'Clicked'), 0), 2) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ad_id;
