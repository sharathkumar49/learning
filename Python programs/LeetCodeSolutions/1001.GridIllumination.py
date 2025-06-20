"""
1001. Grid Illumination
https://leetcode.com/problems/grid-illumination/

You are given a grid of size n x n, with some lamps placed on it. Each lamp illuminates its row, column, and both diagonals. For each query, return 1 if the cell is illuminated, else 0. After each query, turn off any lamp in the cell or adjacent cells.

Constraints:
- 1 <= n <= 10^9
- 0 <= lamps.length <= 2 * 10^4
- 0 <= queries.length <= 2 * 10^4
- lamps[i].length == 2
- queries[i].length == 2

Example:
Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
"""
from typing import List
from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row = Counter()
        col = Counter()
        diag = Counter()
        anti = Counter()
        lamp_set = set(map(tuple, lamps))
        for x, y in lamp_set:
            row[x] += 1
            col[y] += 1
            diag[x-y] += 1
            anti[x+y] += 1
        res = []
        for x, y in queries:
            if row[x] or col[y] or diag[x-y] or anti[x+y]:
                res.append(1)
            else:
                res.append(0)
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in lamp_set:
                        lamp_set.remove((nx, ny))
                        row[nx] -= 1
                        col[ny] -= 1
                        diag[nx-ny] -= 1
                        anti[nx+ny] -= 1
        return res

# Example usage
if __name__ == "__main__":
    n = 5
    lamps = [[0,0],[4,4]]
    queries = [[1,1],[1,0]]
    print(Solution().gridIllumination(n, lamps, queries))  # Output: [1,0]
