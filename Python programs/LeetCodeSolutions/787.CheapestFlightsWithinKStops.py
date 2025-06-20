"""
787. Cheapest Flights Within K Stops

There are n cities and flights[i] = [from_i, to_i, price_i] represents a flight from city from_i to city to_i with price price_i. Given n, flights, src, dst, and k, return the cheapest price from src to dst with at most k stops. If no such route exists, return -1.

Example 1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= from_i, to_i, src, dst < n
- 1 <= price_i <= 10^4
- 0 <= k <= n - 1
"""
import heapq
from collections import defaultdict

def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    heap = [(0, src, 0)]
    while heap:
        cost, u, stops = heapq.heappop(heap)
        if u == dst:
            return cost
        if stops > k:
            continue
        for v, w in graph[u]:
            heapq.heappush(heap, (cost + w, v, stops + 1))
    return -1

# Example usage:
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500
