"""
576. Out of Boundary Paths
Difficulty: Medium

There is an m x n grid with a ball. The ball is at position (startRow, startColumn). You are allowed to move the ball up, down, left, or right at any time. Return the number of possible paths to move the ball out of the grid boundary in at most maxMove moves. Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""

def findPaths(m, n, maxMove, startRow, startColumn):
    MOD = 10**9 + 7
    dp = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)]
    for move in range(1, maxMove+1):
        for i in range(m):
            for j in range(n):
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n:
                        dp[move][i][j] = (dp[move][i][j] + dp[move-1][ni][nj]) % MOD
                    else:
                        dp[move][i][j] = (dp[move][i][j] + 1) % MOD
    return dp[maxMove][startRow][startColumn]

# Example usage
if __name__ == "__main__":
    print(findPaths(2,2,2,0,0))  # Output: 6
    print(findPaths(1,3,3,0,1))  # Output: 12
