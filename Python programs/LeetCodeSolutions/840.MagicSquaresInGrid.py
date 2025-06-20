"""
840. Magic Squares In Grid

Given a grid of integers, return the number of 3x3 magic square subgrids.

Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1

Constraints:
- 1 <= grid.length, grid[0].length <= 10
- 0 <= grid[i][j] <= 15
"""
def numMagicSquaresInside(grid):
    def is_magic(i, j):
        s = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        if sorted(s) != list(range(1, 10)):
            return False
        return (sum(grid[i][j:j+3]) == sum(grid[i+1][j:j+3]) == sum(grid[i+2][j:j+3]) ==
                sum(grid[i][j] for i in range(i, i+3)) == sum(grid[i][j+1] for i in range(i, i+3)) == sum(grid[i][j+2] for i in range(i, i+3)) ==
                grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j])
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m-2):
        for j in range(n-2):
            if is_magic(i, j):
                count += 1
    return count

# Example usage:
print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))  # Output: 1
