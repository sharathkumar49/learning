"""
999. Available Captures for Rook
https://leetcode.com/problems/available-captures-for-rook/

On an 8 x 8 chessboard, given the board as a 2D char array, return the number of pawns the rook can capture in one move.

Constraints:
- board.length == 8
- board[i].length == 8
- board[i][j] is '.', 'R', 'B', or 'p'
- There is exactly one 'R' on the board.

Example:
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
"""
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
        res = 0
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x, y
            while 0 <= nx+dx < 8 and 0 <= ny+dy < 8:
                nx += dx
                ny += dy
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == 'p':
                    res += 1
                    break
        return res

# Example usage
if __name__ == "__main__":
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(Solution().numRookCaptures(board))  # Output: 3
