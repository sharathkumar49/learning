"""
529. Minesweeper

Given a 2D char matrix representing the game board, implement a function to reveal a cell according to the rules of Minesweeper.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 50
- board[i][j] is 'M', 'E', 'B', '1'-'8', or 'X'.
- Click is a list of two integers [row, col].

Example:
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
"""

class Solution:
    def updateBoard(self, board: list, click: list) -> list:
        m, n = len(board), len(board[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        def dfs(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return
            count = 0
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1
            if count:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
                        dfs(nx, ny)
        dfs(click[0], click[1])
        return board

# Example usage:
sol = Solution()
board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(sol.updateBoard(board, click))
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
