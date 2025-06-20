"""
305. Number of Islands II

You are given an empty 2D binary grid of size m x n. The grid starts with all 0's (representing water). You are also given an array positions, where positions[i] = [row_i, col_i] is the position to add a land (1) at position (row_i, col_i). Return an array of the number of islands after each addLand operation.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:
- 1 <= m, n, positions.length <= 10^4
- 1 <= m * n <= 10^4
- positions[i].length == 2
- 0 <= row_i < m
- 0 <= col_i < n

"""
from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx == rooty:
                return False
            if rank[rootx] < rank[rooty]:
                parent[rootx] = rooty
            else:
                parent[rooty] = rootx
                if rank[rootx] == rank[rooty]:
                    rank[rootx] += 1
            return True
        res = []
        count = 0
        for r, c in positions:
            if (r, c) in parent:
                res.append(count)
                continue
            parent[(r, c)] = (r, c)
            rank[(r, c)] = 0
            count += 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in parent:
                    if union((r, c), (nr, nc)):
                        count -= 1
            res.append(count)
        return res

# Example usage:
m, n = 3, 3
positions = [[0,0],[0,1],[1,2],[2,1]]
print(Solution().numIslands2(m, n, positions))  # Output: [1,1,2,3]
