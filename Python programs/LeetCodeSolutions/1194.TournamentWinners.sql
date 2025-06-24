"""
1194. Tournament Winners (SQL)

Table: Players
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| player_id   | int     |
| group_id    | int     |
+-------------+---------+
player_id is the primary key.

group_id is the id of the group the player belongs to.

Table: Matches
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| match_id    | int     |
| first_player | int    |
| second_player | int   |
| first_score | int     |
| second_score | int    |
+-------------+---------+
match_id is the primary key.

Write an SQL query to find the winner in each group. The winner is the player with the highest total score in the group. If there is a tie, return the player with the smallest player_id.

"""
SELECT p.group_id, p.player_id
FROM Players p
JOIN (
    SELECT group_id, player_id, SUM(score) AS total_score
    FROM (
        SELECT p.group_id, m.first_player AS player_id, m.first_score AS score
        FROM Players p JOIN Matches m ON p.player_id = m.first_player
        UNION ALL
        SELECT p.group_id, m.second_player AS player_id, m.second_score AS score
        FROM Players p JOIN Matches m ON p.player_id = m.second_player
    ) t
    GROUP BY group_id, player_id
) s ON p.group_id = s.group_id AND p.player_id = s.player_id
JOIN (
    SELECT group_id, MAX(total_score) AS max_score
    FROM (
        SELECT group_id, player_id, SUM(score) AS total_score
        FROM (
            SELECT p.group_id, m.first_player AS player_id, m.first_score AS score
            FROM Players p JOIN Matches m ON p.player_id = m.first_player
            UNION ALL
            SELECT p.group_id, m.second_player AS player_id, m.second_score AS score
            FROM Players p JOIN Matches m ON p.player_id = m.second_player
        ) t
        GROUP BY group_id, player_id
    ) s
    GROUP BY group_id
) m ON s.group_id = m.group_id AND s.total_score = m.max_score
ORDER BY p.group_id, p.player_id;
