"""
LeetCode 1450. Number of Students Doing Homework at a Given Time

Given two integer arrays startTime and endTime and an integer queryTime, return the number of students doing their homework at queryTime.

Constraints:
- startTime.length == endTime.length
- 1 <= startTime.length <= 100
- 1 <= startTime[i] <= endTime[i] <= 1000
- 1 <= queryTime <= 1000

Example:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
"""
def busyStudent(startTime, endTime, queryTime):
    return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))

# Example usage:
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
print(busyStudent(startTime, endTime, queryTime))  # Output: 1
