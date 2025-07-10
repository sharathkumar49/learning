"""
LeetCode 1618. Maximum Font to Fit a Sentence in a Screen

Table: Fonts
+-------------+------+
| Column Name | Type |
+-------------+------+
| font_id     | int  |
| font_size   | int  |
| width       | int  |
+-------------+------+
font_id is the primary key for this table.

Table: Screens
+-------------+------+
| Column Name | Type |
+-------------+------+
| screen_id   | int  |
| width       | int  |
+-------------+------+
screen_id is the primary key for this table.

Write an SQL query to find the maximum font size that can be used to fit a sentence in each screen.

Example:
Input:
Fonts table:
| font_id | font_size | width |
|---------|-----------|-------|
| 1       | 12        | 8     |
| 2       | 14        | 9     |
Screens table:
| screen_id | width |
|-----------|-------|
| 1         | 100   |
| 2         | 80    |
Output:
| screen_id | font_size |
|-----------|-----------|
| 1         | 14        |
| 2         | 12        |
"""

-- SQL Query:
SELECT s.screen_id, MAX(f.font_size) AS font_size
FROM Screens s
JOIN Fonts f ON f.width * 10 <= s.width
GROUP BY s.screen_id;
