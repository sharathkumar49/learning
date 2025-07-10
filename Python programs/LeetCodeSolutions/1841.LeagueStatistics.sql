"""
LeetCode 1841. League Statistics

Table: Teams
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| team_id     | int   |
| team_name   | varchar |
+-------------+-------+
team_id is the primary key for this table.

Table: Matches
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| match_id    | int   |
| host_team   | int   |
| guest_team  | int   |
| host_goals  | int   |
| guest_goals | int   |
+-------------+-------+
match_id is the primary key for this table.

Write an SQL query to get the league statistics for each team.

Example:
Teams table:
| team_id | team_name |
|---------|-----------|
| 1       | Ajax      |
| 4       | Dynamo    |
| 6       | Zenit     |

Matches table:
| match_id | host_team | guest_team | host_goals | guest_goals |
|----------|-----------|------------|------------|-------------|
| 1        | 1         | 4          | 0          | 1           |
| 2        | 1         | 6          | 3          | 3           |
| 3        | 4         | 1          | 5          | 2           |

Output:
| team_id | team_name | matches_played | points |
|---------|-----------|----------------|--------|
| 1       | Ajax      | 3              | 1      |
| 4       | Dynamo    | 2              | 6      |
| 6       | Zenit     | 1              | 1      |

"""

-- SQL Solution
SELECT t.team_id, t.team_name,
       COUNT(m.match_id) AS matches_played,
       SUM(
         CASE
           WHEN (t.team_id = m.host_team AND m.host_goals > m.guest_goals) OR (t.team_id = m.guest_team AND m.guest_goals > m.host_goals) THEN 3
           WHEN (t.team_id = m.host_team OR t.team_id = m.guest_team) AND m.host_goals = m.guest_goals THEN 1
           ELSE 0
         END
       ) AS points
FROM Teams t
LEFT JOIN Matches m ON t.team_id = m.host_team OR t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name;
