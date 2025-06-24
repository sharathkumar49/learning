"""
1139. Largest 1-Bordered Square

Given a 2D grid of 0s and 1s, return the size of the largest square with a border of 1s.

Constraints:
- 1 <= grid.length <= 100
- 1 <= grid[0].length <= 100
- grid[i][j] is 0 or 1

Example:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 3

"""
def largest1BorderedSquare(grid):
    m, n = len(grid), len(grid[0])
    hor = [[0]*n for _ in range(m)]
    ver = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                hor[i][j] = hor[i][j-1] + 1 if j else 1
                ver[i][j] = ver[i-1][j] + 1 if i else 1
    max_side = 0
    for i in range(m):
        for j in range(n):
            small = min(hor[i][j], ver[i][j])
            while small > 0:
                if ver[i][j-small+1] >= small and hor[i-small+1][j] >= small:
                    max_side = max(max_side, small)
                    break
                small -= 1
    return max_side * max_side

# Example usage
if __name__ == "__main__":
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    print(largest1BorderedSquare(grid))  # Output: 9
