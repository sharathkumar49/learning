"""
LeetCode 1783. Grand Slam Titles

Table: Championships
+-------------+------+
| Column Name | Type |
+-------------+------+
| player_id   | int  |
| year        | int  |
| tournament  | varchar |
+-------------+------+
(player_id, year, tournament) is the primary key.

Write an SQL query to find the players who have won all four grand slam tournaments in the same year.

Example:
Championships table:
| player_id | year | tournament |
|-----------|------|------------|
| 1         | 2020 | Wimbledon  |
| 1         | 2020 | US Open    |
| 1         | 2020 | French Open|
| 1         | 2020 | Australian Open|
| 2         | 2020 | Wimbledon  |
| 2         | 2020 | US Open    |

Output:
| player_id | year |
|-----------|------|
| 1         | 2020 |

"""
SELECT player_id, year
FROM Championships
GROUP BY player_id, year
HAVING COUNT(DISTINCT tournament) = 4;
