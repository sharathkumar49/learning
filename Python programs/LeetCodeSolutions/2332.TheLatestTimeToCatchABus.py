"""
LeetCode 2332. The Latest Time to Catch a Bus

Given buses, passengers, and capacity, return the latest time to catch a bus.

Example:
Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
Output: 16

Constraints:
- 1 <= buses.length, passengers.length <= 10^5
"""

def latestTimeCatchTheBus(buses, passengers, capacity):
    buses.sort()
    passengers = set(passengers)
    times = sorted(passengers)
    idx = 0
    for bus in buses:
        cnt = 0
        while idx < len(times) and times[idx] <= bus and cnt < capacity:
            idx += 1
            cnt += 1
    t = bus
    while t in passengers:
        t -= 1
    return t

# Example usage:
# print(latestTimeCatchTheBus([10,20], [2,17,18,19], 2))  # Output: 16
