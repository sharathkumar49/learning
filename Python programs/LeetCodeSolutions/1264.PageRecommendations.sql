"""
LeetCode 1264. Page Recommendations

Table: Friends
+-------------+------+
| Column Name | Type |
+-------------+------+
| user1_id    | int  |
| user2_id    | int  |
+-------------+------+
(user1_id, user2_id) is a pair of friends.

Table: Likes
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| page_id     | int  |
+-------------+------+
(user_id, page_id) shows that user_id likes page_id.

Write an SQL query to recommend pages to each user. A page should be recommended to a user if:
- The user does not already like the page.
- At least one of their friends likes the page.

Return result table in any order.

Example:
Friends table:
| user1_id | user2_id |
|----------|----------|
| 1        | 2        |
| 1        | 3        |
| 2        | 3        |

Likes table:
| user_id | page_id |
|---------|---------|
| 1       | 88      |
| 2       | 23      |
| 3       | 24      |
| 3       | 56      |
| 2       | 77      |
| 1       | 24      |

Output:
| user_id | page_id |
|---------|---------|
| 1       | 23      |
| 1       | 77      |
| 2       | 24      |
| 2       | 56      |
| 3       | 88      |
| 3       | 77      |

"""
SELECT DISTINCT f.user1_id AS user_id, l.page_id
FROM Friends f
JOIN Likes l ON f.user2_id = l.user_id
WHERE (f.user1_id, l.page_id) NOT IN (SELECT user_id, page_id FROM Likes)
UNION
SELECT DISTINCT f.user2_id AS user_id, l.page_id
FROM Friends f
JOIN Likes l ON f.user1_id = l.user_id
WHERE (f.user2_id, l.page_id) NOT IN (SELECT user_id, page_id FROM Likes);
