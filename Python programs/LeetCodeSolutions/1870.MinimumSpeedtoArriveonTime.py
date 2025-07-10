"""
LeetCode 1870. Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time you have to reach the office, and an integer array dist, where dist[i] is the distance of the i-th train ride. Return the minimum positive integer speed (in km/h) that all trains must travel at for you to reach the office on time, or -1 if it is impossible.

Example:
Input: dist = [1,3,2], hour = 6
Output: 1

Constraints:
- 1 <= dist.length <= 10^5
- 1 <= dist[i] <= 10^5
- 1 <= hour <= 10^9
"""

import math

def minSpeedOnTime(dist, hour):
    left, right = 1, 10**7
    res = -1
    while left <= right:
        mid = (left + right) // 2
        time = 0
        for d in dist[:-1]:
            time += math.ceil(d / mid)
        time += dist[-1] / mid
        if time <= hour:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

# Example usage:
# print(minSpeedOnTime([1,3,2], 6))  # Output: 1
