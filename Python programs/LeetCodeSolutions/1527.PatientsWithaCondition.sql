"""
LeetCode 1527. Patients With a Condition

Table: Patients
+-------------+------+
| Column Name | Type |
+-------------+------+
| patient_id  | int  |
| patient_name| text |
| conditions  | text |
+-------------+------+
patient_id is the primary key for this table.

Write an SQL query to report the patient_id, patient_name, and conditions of patients who have Type I Diabetes.

Example:
Input:
Patients table:
| patient_id | patient_name | conditions         |
|------------|--------------|-------------------|
| 1          | John         | Diabetes Type I   |
| 2          | Jane         | Healthy           |
| 3          | Alex         | Diabetes Type II  |
Output:
| patient_id | patient_name | conditions       |
|------------|--------------|------------------|
| 1          | John         | Diabetes Type I  |
"""

-- SQL Query:
SELECT *
FROM Patients
WHERE conditions LIKE '%Diabetes Type I%';
