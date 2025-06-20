"""
LeetCode 743. Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from u to v.

Return the time it takes for all the n nodes to receive the signal. If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= u, v <= n
- 0 <= w <= 100
"""
from typing import List
import heapq

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = [[] for _ in range(n+1)]
    for u, v, w in times:
        graph[u].append((v, w))
    heap = [(0, k)]
    dist = {}
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(heap, (d+w, nei))
    return max(dist.values()) if len(dist) == n else -1

# Example usage
if __name__ == "__main__":
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # Output: 2
    print(networkDelayTime([[1,2,1]], 2, 1))  # Output: 1
