"""
LeetCode 675. Cut Off Trees for Golf Event

You are asked to cut off trees in a forest for a golf event. The forest is represented as a m x n matrix. In the matrix:
- 0 means the cell cannot be walked through.
- 1 means the cell can be walked through.
- A number greater than 1 means a tree of that height stands in that cell.

You can walk up, down, left, or right from a cell, and you must cut off the trees in order from shortest to tallest. Once you cut a tree, the cell becomes walkable (value 1).

Return the minimum steps needed to cut all the trees in order. If it is impossible, return -1.

Example 1:
Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6

Example 2:
Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1

Example 3:
Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6

Constraints:
- m == forest.length
- n == forest[i].length
- 1 <= m, n <= 50
- 0 <= forest[i][j] <= 10^9
- There are at most 200 trees in the forest.
"""
from typing import List
from collections import deque

def cutOffTree(forest: List[List[int]]) -> int:
    if not forest or not forest[0]:
        return -1
    m, n = len(forest), len(forest[0])
    trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
    def bfs(sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return 0
        visited = [[False]*n for _ in range(m)]
        queue = deque([(sx, sy, 0)])
        visited[sx][sy] = True
        while queue:
            x, y, d = queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and forest[nx][ny]:
                    if nx == tx and ny == ty:
                        return d+1
                    visited[nx][ny] = True
                    queue.append((nx, ny, d+1))
        return -1
    sx = sy = res = 0
    for _, tx, ty in trees:
        d = bfs(sx, sy, tx, ty)
        if d == -1:
            return -1
        res += d
        sx, sy = tx, ty
    return res

# Example usage
if __name__ == "__main__":
    print(cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))  # Output: 6
    print(cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))  # Output: -1
    print(cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))  # Output: 6
