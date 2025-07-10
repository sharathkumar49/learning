"""
LeetCode 1747. Leetflex Banned Words

Table: Messages
+-------------+------+
| Column Name | Type |
+-------------+------+
| message_id  | int  |
| content     | varchar |
+-------------+------+
(message_id) is the primary key.

Table: BannedWords
+-------------+------+
| Column Name | Type |
+-------------+------+
| word        | varchar |
+-------------+------+
(word) is the primary key.

Write an SQL query to find the message_id of all messages containing any banned word.

Example:
Messages table:
| message_id | content         |
|------------|----------------|
| 1          | "hello world"   |
| 2          | "leetflex"      |
| 3          | "banned word"   |

BannedWords table:
| word    |
|---------|
| leetflex|
| banned  |

Output:
| message_id |
|------------|
| 2          |
| 3          |

"""
SELECT DISTINCT m.message_id
FROM Messages m
JOIN BannedWords b
ON m.content LIKE CONCAT('%', b.word, '%');
