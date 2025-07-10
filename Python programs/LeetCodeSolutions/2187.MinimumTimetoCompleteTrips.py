"""
LeetCode 2187. Minimum Time to Complete Trips

Given an array time where time[i] is the time taken by the i-th bus to complete one trip, and an integer totalTrips, return the minimum time required to complete totalTrips trips.

Example:
Input: time = [1,2,3], totalTrips = 5
Output: 3

Constraints:
- 1 <= time.length <= 10^5
- 1 <= time[i], totalTrips <= 10^7
"""

def minimumTime(time, totalTrips):
    left, right = 1, min(time) * totalTrips
    while left < right:
        mid = (left + right) // 2
        trips = sum(mid // t for t in time)
        if trips >= totalTrips:
            right = mid
        else:
            left = mid + 1
    return left

# Example usage:
# print(minimumTime([1,2,3], 5))  # Output: 3
