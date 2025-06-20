"""
1102. Path With Maximum Minimum Value

Given a matrix of integers, return the maximum score of a path from the top-left to the bottom-right, where the score of a path is the minimum value in that path.

Constraints:
- 1 <= A.length, A[0].length <= 100
- 0 <= A[i][j] <= 10^9

Example:
Input: A = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
"""
from typing import List
import heapq

def maximumMinimumPath(A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    heap = [(-A[0][0], 0, 0)]
    visited = set((0, 0))
    while heap:
        val, x, y = heapq.heappop(heap)
        if (x, y) == (m-1, n-1):
            return -val
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(heap, (max(val, -A[nx][ny]), nx, ny))
    return -1

# Example usage:
A = [[5,4,5],[1,2,6],[7,4,6]]
print(maximumMinimumPath(A))  # Output: 4
