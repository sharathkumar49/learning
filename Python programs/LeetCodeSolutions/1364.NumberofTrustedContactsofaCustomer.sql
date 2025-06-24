"""
LeetCode 1364. Number of Trusted Contacts of a Customer

Table: Contacts
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| contact_id  | int  |
+-------------+------+
(user_id, contact_id) is the primary key.

Write an SQL query to report the number of trusted contacts for each user. A trusted contact is a contact who is also a user.

Example:
Contacts table:
| user_id | contact_id |
|---------|------------|
| 1       | 2          |
| 2       | 3          |
| 3       | 1          |
| 4       | 5          |

Output:
| user_id | trusted_contacts |
|---------|------------------|
| 1       | 1                |
| 2       | 1                |
| 3       | 1                |
| 4       | 0                |

"""
SELECT c.user_id, COUNT(u.user_id) AS trusted_contacts
FROM Contacts c
LEFT JOIN (SELECT DISTINCT user_id FROM Contacts) u ON c.contact_id = u.user_id
GROUP BY c.user_id;
