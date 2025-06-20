"""
LeetCode 723. Candy Crush

This question is about implementing a basic version of the Candy Crush game.
Given a 2D integer array board representing the board, return the board after no more candies can be crushed.

Example 1:
Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
Output: [[0,0,0,0,114],[0,0,0,0,214],[0,0,0,113,314],[0,0,0,213,414],[0,0,0,313,614],[0,0,0,613,714],[0,1,1,713,1014],[1,1,1,1,0],[4,1,4,4,0],[110,210,310,410,0]]

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 50
- 1 <= board[i][j] <= 2000
"""
from typing import List

def candyCrush(board: List[List[int]]) -> List[List[int]]:
    m, n = len(board), len(board[0])
    changed = True
    while changed:
        crush = [[False]*n for _ in range(m)]
        changed = False
        # Mark horizontal
        for i in range(m):
            for j in range(n-2):
                v = abs(board[i][j])
                if v and v == abs(board[i][j+1]) and v == abs(board[i][j+2]):
                    crush[i][j] = crush[i][j+1] = crush[i][j+2] = True
        # Mark vertical
        for i in range(m-2):
            for j in range(n):
                v = abs(board[i][j])
                if v and v == abs(board[i+1][j]) and v == abs(board[i+2][j]):
                    crush[i][j] = crush[i+1][j] = crush[i+2][j] = True
        # Crush
        for i in range(m):
            for j in range(n):
                if crush[i][j]:
                    board[i][j] = 0
                    changed = True
        # Drop
        for j in range(n):
            idx = m-1
            for i in range(m-1, -1, -1):
                if board[i][j]:
                    board[idx][j] = board[i][j]
                    idx -= 1
            for i in range(idx, -1, -1):
                board[i][j] = 0
    return board

# Example usage
if __name__ == "__main__":
    board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    print(candyCrush(board))
