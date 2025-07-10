"""
LeetCode 2142. The Number of Passengers in Each Bus II

Table: Buses
+-------------+------+
| Column Name | Type |
+-------------+------+
| bus_id      | int  |
| arrival_time| int  |
+-------------+------+
bus_id is the primary key.
Each row contains information about the arrival time of a bus.

Table: Passengers
+----------------+------+
| Column Name    | Type |
+----------------+------+
| passenger_id   | int  |
| arrival_time   | int  |
+----------------+------+
passenger_id is the primary key.
Each row contains information about the arrival time of a passenger.

Write an SQL query to report the number of passengers that can take each bus. A passenger can take a bus if they arrive at the bus station at or before the bus arrives, and they haven't taken any earlier bus.

Example:
Buses table:
| bus_id | arrival_time |
|--------|--------------|
| 1      | 2            |
| 2      | 4            |
| 3      | 7            |
Passengers table:
| passenger_id | arrival_time |
|--------------|--------------|
| 11           | 1            |
| 12           | 5            |
| 13           | 6            |
| 14           | 7            |

Output:
| bus_id | passengers_cnt |
|--------|---------------|
| 1      | 1             |
| 2      | 1             |
| 3      | 2             |

Solution:
WITH ordered_buses AS (
  SELECT bus_id, arrival_time, ROW_NUMBER() OVER (ORDER BY arrival_time) AS rn
  FROM Buses
),
ordered_passengers AS (
  SELECT passenger_id, arrival_time, ROW_NUMBER() OVER (ORDER BY arrival_time) AS rn
  FROM Passengers
),
assignment AS (
  SELECT b.bus_id, p.passenger_id
  FROM ordered_buses b
  LEFT JOIN ordered_passengers p
    ON p.arrival_time <= b.arrival_time
    AND NOT EXISTS (
      SELECT 1 FROM ordered_buses b2
      WHERE b2.arrival_time < b.arrival_time AND p.arrival_time <= b2.arrival_time
    )
)
SELECT bus_id, COUNT(passenger_id) AS passengers_cnt
FROM assignment
GROUP BY bus_id
ORDER BY bus_id;
