"""
1066. Campus Bikes II

Given the positions of workers and bikes, assign bikes to workers so that the sum of the Manhattan distances is minimized. Each worker gets one bike. Return the minimum possible sum.

Constraints:
- 1 <= workers.length == bikes.length <= 10
- workers[i].length == bikes[i].length == 2
- 0 <= workers[i][j], bikes[i][j] < 1000

Example:
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
"""
from typing import List
from functools import lru_cache

def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> int:
    n = len(workers)
    @lru_cache(None)
    def dfs(i, mask):
        if i == n:
            return 0
        res = float('inf')
        for j in range(n):
            if not (mask & (1 << j)):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                res = min(res, dist + dfs(i+1, mask | (1 << j)))
        return res
    return dfs(0, 0)

# Example usage:
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
print(assignBikes(workers, bikes))  # Output: 6
