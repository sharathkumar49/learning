"""
1260. Shift 2D Grid

Given a 2D grid and an integer k, shift the grid k times. Each shift moves elements to the right, wrapping around.

Constraints:
- 1 <= grid.length <= 50
- 1 <= grid[0].length <= 50
- 0 <= k <= 100

Example:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

"""
def shiftGrid(grid, k):
    m, n = len(grid), len(grid[0])
    flat = sum(grid, [])
    k %= m * n
    flat = flat[-k:] + flat[:-k]
    return [flat[i*n:(i+1)*n] for i in range(m)]

# Example usage
if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    print(shiftGrid(grid, 1))  # Output: [[9,1,2],[3,4,5],[6,7,8]]
