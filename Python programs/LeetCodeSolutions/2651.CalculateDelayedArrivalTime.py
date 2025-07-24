"""
LeetCode 2651. Calculate Delayed Arrival Time

Given arrivalTime and delayedTime, return the actual arrival time.

Constraints:
- 1 <= arrivalTime, delayedTime <= 23
"""

def findDelayedArrivalTime(arrivalTime, delayedTime):
    return (arrivalTime + delayedTime) % 24
# Example usage:
# print(findDelayedArrivalTime(15, 5))  # Output: 20
