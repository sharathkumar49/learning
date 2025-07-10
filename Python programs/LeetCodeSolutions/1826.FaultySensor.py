"""
LeetCode 1826. Faulty Sensor

Given two arrays sensor1 and sensor2, return the index of the faulty sensor, or -1 if not determinable.

Example 1:
Input: sensor1 = [2,3,4,5], sensor2 = [2,1,4,5]
Output: 1

Constraints:
- 1 <= sensor1.length, sensor2.length <= 100
- 1 <= sensor1[i], sensor2[i] <= 100
"""

def badSensor(sensor1, sensor2):
    n = len(sensor1)
    for i in range(n-1):
        if sensor1[i] != sensor2[i]:
            if sensor1[i+1:] == sensor2[i:-1]:
                return 1
            if sensor2[i+1:] == sensor1[i:-1]:
                return 2
            return -1
    return -1

# Example usage:
# sensor1 = [2,3,4,5]
# sensor2 = [2,1,4,5]
# print(badSensor(sensor1, sensor2))  # Output: 1
