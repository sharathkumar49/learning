"""
LeetCode 1970. Last Day Where You Can Still Cross

Given a row x col binary matrix, return the last day you can still cross from top to bottom.

Example:
Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2

Constraints:
- 2 <= row, col <= 2 * 10^4
- 1 <= cells.length <= row * col
"""

def latestDayToCross(row, col, cells):
    def canCross(day):
        grid = [[0]*col for _ in range(row)]
        for i in range(day):
            x, y = cells[i]
            grid[x-1][y-1] = 1
        q = [(0, j) for j in range(col) if grid[0][j] == 0]
        seen = set(q)
        for x, y in q:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]==0 and (nx,ny) not in seen:
                    if nx == row-1:
                        return True
                    seen.add((nx,ny))
                    q.append((nx,ny))
        return False
    left, right = 1, len(cells)
    while left < right:
        mid = (left + right + 1) // 2
        if canCross(mid):
            left = mid
        else:
            right = mid - 1
    return left

# Example usage:
# print(latestDayToCross(2, 2, [[1,1],[2,1],[1,2],[2,2]]))  # Output: 2
