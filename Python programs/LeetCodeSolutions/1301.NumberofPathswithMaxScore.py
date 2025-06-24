"""
LeetCode 1301. Number of Paths with Max Score

Given a board of characters, return the number of paths from the bottom-right to the top-left with the maximum score. You can only move up, left, or diagonally up-left. Return [max_score, num_paths].

Constraints:
- 2 <= board.length == board[i].length <= 100
- board[i][j] is a digit, 'S', or 'E'

Example:
Input: board = ["E23","2X2","12S"]
Output: [7,1]
"""
def pathsWithMaxScore(board):
    n = len(board)
    MOD = 10**9+7
    dp = [[(-float('inf'), 0) for _ in range(n)] for _ in range(n)]
    dp[-1][-1] = (0, 1)
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if board[i][j] == 'X':
                continue
            for dx, dy in [(1,0),(0,1),(1,1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<n and 0<=nj<n and dp[ni][nj][1]:
                    score = dp[ni][nj][0]
                    if board[i][j] not in 'SE':
                        score += int(board[i][j])
                    if score > dp[i][j][0]:
                        dp[i][j] = (score, dp[ni][nj][1])
                    elif score == dp[i][j][0]:
                        dp[i][j] = (score, (dp[i][j][1]+dp[ni][nj][1])%MOD)
    return [max(0, dp[0][0][0]), dp[0][0][1]]

# Example usage:
board = ["E23","2X2","12S"]
print(pathsWithMaxScore(board))  # Output: [7, 1]
