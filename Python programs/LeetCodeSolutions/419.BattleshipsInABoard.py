"""
419. Battleships in a Board

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board. Battleships can only be placed horizontally or vertically.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is either '.' or 'X'.
- There are no adjacent battleships.
"""
from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                    count += 1
        return count

# Example usage:
board = [
  ["X",".",".","X"],
  [".",".",".","X"],
  [".",".",".","X"]
]
print(Solution().countBattleships(board))  # Output: 2
