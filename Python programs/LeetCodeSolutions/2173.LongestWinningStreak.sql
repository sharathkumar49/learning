"""
LeetCode 2173. Longest Winning Streak

Table: Matches
+-------------+------+
| Column Name | Type |
+-------------+------+
| match_id    | int  |
| player_id   | int  |
| result      | enum('Win','Lose') |
+-------------+------+
(match_id, player_id) is the primary key.

Write an SQL query to report the longest winning streak for each player.

Example:
Matches table:
| match_id | player_id | result |
|----------|-----------|--------|
| 1        | 1         | Win    |
| 2        | 1         | Win    |
| 3        | 1         | Lose   |
| 4        | 1         | Win    |
| 5        | 1         | Win    |
| 6        | 2         | Lose   |
| 7        | 2         | Win    |

Output:
| player_id | longest_streak |
|-----------|----------------|
| 1         | 2              |
| 2         | 1              |

Solution:
WITH streaks AS (
  SELECT player_id, match_id, result,
         ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_id) -
         ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_id) AS grp
  FROM Matches
)
SELECT player_id, MAX(cnt) AS longest_streak
FROM (
  SELECT player_id, COUNT(*) AS cnt
  FROM streaks
  WHERE result = 'Win'
  GROUP BY player_id, grp
) t
GROUP BY player_id;
