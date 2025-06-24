"""
1212. Team Scores in Football Tournament (SQL)

Table: Teams
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| team_id     | int     |
| team_name   | varchar |
+-------------+---------+
team_id is the primary key.

Table: Matches
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| match_id    | int     |
| host_team   | int     |
| guest_team  | int     |
| host_goals  | int     |
| guest_goals | int     |
+-------------+---------+
match_id is the primary key.

Write an SQL query to find the total number of goals for each team. Return the result table ordered by team_id.

"""
SELECT t.team_id, t.team_name, COALESCE(SUM(m.host_goals * (t.team_id = m.host_team) + m.guest_goals * (t.team_id = m.guest_team)), 0) AS num_goals
FROM Teams t
LEFT JOIN Matches m ON t.team_id = m.host_team OR t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name
ORDER BY t.team_id;
