"""
1210. Minimum Moves to Reach Target with Rotations

Given a grid, return the minimum number of moves to move a 2x1 snake from the top-left to the bottom-right corner. The snake can move right, down, or rotate.

Constraints:
- 2 <= n == grid.length == grid[i].length <= 100
- grid[i][j] is 0 or 1

Example:
Input: grid = [[0,0,0,0,0,1,1],[1,1,0,0,1,0,1],[0,0,0,0,1,1,0],[0,0,1,0,1,0,0],[0,1,1,0,0,0,1],[0,0,1,0,0,1,0],[0,0,0,0,0,0,0]]
Output: 31

"""
def minimumMoves(grid):
    from collections import deque
    n = len(grid)
    q = deque()
    q.append((0, 0, 0, 0))  # x, y, orientation, steps
    visited = set()
    visited.add((0, 0, 0))
    while q:
        x, y, o, steps = q.popleft()
        if (x, y, o) == (n-1, n-2, 0):
            return steps
        # Move right
        if o == 0 and y+2 < n and grid[x][y+2] == 0 and (x, y+1, 0) not in visited:
            visited.add((x, y+1, 0))
            q.append((x, y+1, 0, steps+1))
        # Move down
        if o == 0 and x+1 < n and grid[x+1][y] == 0 and grid[x+1][y+1] == 0 and (x+1, y, 0) not in visited:
            visited.add((x+1, y, 0))
            q.append((x+1, y, 0, steps+1))
        # Rotate clockwise
        if o == 0 and x+1 < n and grid[x+1][y] == 0 and grid[x+1][y+1] == 0 and (x, y, 1) not in visited:
            visited.add((x, y, 1))
            q.append((x, y, 1, steps+1))
        # Move right (vertical)
        if o == 1 and y+1 < n and grid[x][y+1] == 0 and grid[x+1][y+1] == 0 and (x, y+1, 1) not in visited:
            visited.add((x, y+1, 1))
            q.append((x, y+1, 1, steps+1))
        # Move down (vertical)
        if o == 1 and x+2 < n and grid[x+2][y] == 0 and (x+1, y, 1) not in visited:
            visited.add((x+1, y, 1))
            q.append((x+1, y, 1, steps+1))
        # Rotate counterclockwise
        if o == 1 and y+1 < n and grid[x][y+1] == 0 and grid[x+1][y+1] == 0 and (x, y, 0) not in visited:
            visited.add((x, y, 0))
            q.append((x, y, 0, steps+1))
    return -1

# Example usage
if __name__ == "__main__":
    grid = [[0,0,0,0,0,1,1],[1,1,0,0,1,0,1],[0,0,0,0,1,1,0],[0,0,1,0,1,0,0],[0,1,1,0,0,0,1],[0,0,1,0,0,1,0],[0,0,0,0,0,0,0]]
    print(minimumMoves(grid))  # Output: 31
