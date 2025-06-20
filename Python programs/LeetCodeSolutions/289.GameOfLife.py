"""
289. Game of Life
https://leetcode.com/problems/game-of-life/

According to the rules of Conway's Game of Life, given a board of m by n cells, return the next state of the board.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""
def gameOfLife(board):
    m, n = len(board), len(board[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    copy = [row[:] for row in board]
    for i in range(m):
        for j in range(n):
            live = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and copy[ni][nj] == 1:
                    live += 1
            if copy[i][j] == 1 and (live < 2 or live > 3):
                board[i][j] = 0
            elif copy[i][j] == 0 and live == 3:
                board[i][j] = 1

# Example usage:
if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    gameOfLife(board)
    print(board)  # Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
