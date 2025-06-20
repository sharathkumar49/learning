"""
871. Minimum Number of Refueling Stops

A car travels from start to target with an infinite tank, but stops only at gas stations. Return the minimum number of refueling stops to reach the target, or -1 if impossible.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2

Constraints:
- 1 <= target, startFuel <= 10^9
- 0 <= stations.length <= 500
- 0 < stations[i][0] < stations[i+1][0] < target
- 1 <= stations[i][1] < 10^9
"""
import heapq

def minRefuelStops(target, startFuel, stations):
    heap = []
    stations.append([target, 0])
    res = prev = 0
    fuel = startFuel
    for loc, cap in stations:
        fuel -= loc - prev
        while heap and fuel < 0:
            fuel += -heapq.heappop(heap)
            res += 1
        if fuel < 0:
            return -1
        heapq.heappush(heap, -cap)
        prev = loc
    return res

# Example usage:
print(minRefuelStops(1, 1, []))  # Output: 0
print(minRefuelStops(100, 1, [[10,100]]))  # Output: -1
print(minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))  # Output: 2
