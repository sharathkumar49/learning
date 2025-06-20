"""
LeetCode 688. Knight Probability in Chessboard

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The probability that the knight remains on the board after it has stopped moving is returned.

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.0625

Constraints:
- 1 <= n <= 25
- 0 <= k <= 100
- 0 <= row, column < n
"""
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dirs = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
    dp = [[[0]*n for _ in range(n)] for _ in range(k+1)]
    dp[0][row][column] = 1
    for step in range(1, k+1):
        for i in range(n):
            for j in range(n):
                for dx, dy in dirs:
                    ni, nj = i+dx, j+dy
                    if 0<=ni<n and 0<=nj<n:
                        dp[step][ni][nj] += dp[step-1][i][j]/8
    return sum(dp[k][i][j] for i in range(n) for j in range(n))

# Example usage
if __name__ == "__main__":
    print(knightProbability(3, 2, 0, 0))  # Output: 0.0625
