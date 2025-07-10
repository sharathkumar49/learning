"""
LeetCode 1853. Convert Date Format

Table: Dates
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| date_id     | int   |
| date_value  | varchar |
+-------------+-------+
date_id is the primary key for this table.

date_value is in the format 'Day Month Year' (e.g., '20th Oct 2052').
Write an SQL query to convert date_value into the format 'YYYY-MM-DD'.

Example:
Dates table:
| date_id | date_value      |
|---------|----------------|
| 1       | 20th Oct 2052  |
| 2       | 6th Jun 1933   |
| 3       | 26th May 1960  |

Output:
| date_id | new_date   |
|---------|------------|
| 1       | 2052-10-20 |
| 2       | 1933-06-06 |
| 3       | 1960-05-26 |

"""

-- SQL Solution
SELECT date_id,
       CONCAT(SUBSTRING(date_value, -4), '-',
              LPAD(CASE SUBSTRING_INDEX(SUBSTRING_INDEX(date_value, ' ', 2), ' ', -1)
                   WHEN 'Jan' THEN '1' WHEN 'Feb' THEN '2' WHEN 'Mar' THEN '3' WHEN 'Apr' THEN '4'
                   WHEN 'May' THEN '5' WHEN 'Jun' THEN '6' WHEN 'Jul' THEN '7' WHEN 'Aug' THEN '8'
                   WHEN 'Sep' THEN '9' WHEN 'Oct' THEN '10' WHEN 'Nov' THEN '11' WHEN 'Dec' THEN '12' END, 2, '0'),
              '-',
              LPAD(SUBSTRING_INDEX(date_value, ' ', 1), 2, '0')) AS new_date
FROM Dates;
