"""
LeetCode 1294. Weather Type in Each Country

Table: Countries
+-------------+------+
| Column Name | Type |
+-------------+------+
| country_id  | int  |
| country_name| varchar |
+-------------+------+
country_id is the primary key.

Table: Weather
+-------------+------+
| Column Name | Type |
+-------------+------+
| country_id  | int  |
| weather_type| varchar |
| day         | date |
+-------------+------+
(country_id, day) is the primary key.

Write an SQL query to report the type of weather in each country. Return the result table ordered by country_name and weather_type.

Example:
Countries table:
| country_id | country_name |
|------------|--------------|
| 2          | USA          |
| 3          | Australia    |

Weather table:
| country_id | weather_type | day       |
|------------|--------------|-----------|
| 2          | Sunny        | 2020-01-01|
| 2          | Rainy        | 2020-01-02|
| 3          | Sunny        | 2020-01-01|

Output:
| country_name | weather_type |
|--------------|--------------|
| Australia    | Sunny        |
| USA          | Rainy        |
| USA          | Sunny        |

"""
SELECT c.country_name, w.weather_type
FROM Countries c
JOIN Weather w ON c.country_id = w.country_id
GROUP BY c.country_name, w.weather_type
ORDER BY c.country_name, w.weather_type;
