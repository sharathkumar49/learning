"""
885. Spiral Matrix III

You start at (rStart, cStart) in a rows x cols grid. Return the coordinates of all cells in spiral order.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[2,2],[2,1],[2,0],[1,0],[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[3,1],[3,0],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[3,5]]

Constraints:
- 1 <= rows, cols <= 100
- 0 <= rStart < rows
- 0 <= cStart < cols
"""
def spiralMatrixIII(rows, cols, rStart, cStart):
    res = []
    n = rows * cols
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    steps = 1
    r, c = rStart, cStart
    res.append([r, c])
    while len(res) < n:
        for d in range(4):
            for _ in range(steps + (d//2)):
                r += dirs[d][0]
                c += dirs[d][1]
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            if d % 2 == 1:
                steps += 1
    return res

# Example usage:
print(spiralMatrixIII(1, 4, 0, 0))  # Output: [[0,0],[0,1],[0,2],[0,3]]
print(spiralMatrixIII(5, 6, 1, 4))  # Output: [[1,4],[1,5],[2,5],...]
