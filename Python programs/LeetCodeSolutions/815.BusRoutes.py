"""
815. Bus Routes

You are given a list routes where routes[i] is a bus route that the i-th bus repeats forever. Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

Constraints:
- 1 <= routes.length <= 500
- 1 <= routes[i].length <= 10^5
- All the values of routes[i] are unique.
- sum(routes[i].length) <= 10^5
- 0 <= routes[i][j] < 10^6
- source, target < 10^6
"""
from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
    visited_stops = set([source])
    visited_routes = set()
    queue = deque([(source, 0)])
    while queue:
        stop, buses = queue.popleft()
        for route_i in stop_to_routes[stop]:
            if route_i in visited_routes:
                continue
            visited_routes.add(route_i)
            for next_stop in routes[route_i]:
                if next_stop == target:
                    return buses + 1
                if next_stop not in visited_stops:
                    visited_stops.add(next_stop)
                    queue.append((next_stop, buses + 1))
    return -1

# Example usage:
print(numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))  # Output: 2
print(numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))  # Output: -1
