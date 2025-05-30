# Microsoft: Find the minimum path sum in a grid
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]

if __name__ == "__main__":
    m = int(input("Rows: "))
    n = int(input("Cols: "))
    grid = [list(map(int, input().split())) for _ in range(m)]
    print("Min path sum:", min_path_sum(grid))
