"""
LeetCode 1683. Invalid Tweets

Table: Tweets
+-------------+------+
| Column Name | Type |
+-------------+------+
| tweet_id    | int  |
| content     | varchar |
+-------------+------+
tweet_id is the primary key for this table.

Write an SQL query to find the tweet_id of tweets with content longer than 15 characters.

Example:
Input:
Tweets table:
| tweet_id | content         |
|----------|-----------------|
| 1        | Vote for Biden! |
| 2        | Let us make...  |
Output:
| tweet_id |
|----------|
| 2        |
"""

-- SQL Query:
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
