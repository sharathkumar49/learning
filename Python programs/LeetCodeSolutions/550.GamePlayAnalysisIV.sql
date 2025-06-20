"""
550. Game Play Analysis IV (SQL)

Table: Activity
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key for this table.
This table shows the activity of players of some game.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.

Write an SQL query to report the fraction of players that logged in again on the day after the first login for each player, rounded to 2 decimal places.

Example:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+------------------+
| fraction         |
+------------------+
| 0.33             |
+------------------+
"""

SELECT ROUND(
    SUM(CASE WHEN EXISTS (
        SELECT 1 FROM Activity a2
        WHERE a2.player_id = a1.player_id
          AND a2.event_date = DATE_ADD(MIN(a1.event_date), INTERVAL 1 DAY)
    ) THEN 1 ELSE 0 END) / COUNT(DISTINCT a1.player_id), 2
) AS fraction
FROM Activity a1
GROUP BY a1.player_id;
