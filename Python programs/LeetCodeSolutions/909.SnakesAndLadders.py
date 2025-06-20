"""
909. Snakes and Ladders
https://leetcode.com/problems/snakes-and-ladders/

You are given an n x n integer matrix board where the cells are numbered from 1 to n^2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
Return the least number of moves required to reach the square n^2. If it is not possible, return -1.

Constraints:
- n == board.length == board[i].length
- 2 <= n <= 20
- board[i][j] is either -1 or in the range [1, n^2 - 1]

Example:
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
"""
from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get(s):
            quot, rem = divmod(s-1, n)
            row = n-1 - quot
            col = rem if quot % 2 == 0 else n-1 - rem
            return row, col
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            s, moves = queue.popleft()
            if s == n*n:
                return moves
            for i in range(1, 7):
                nxt = s + i
                if nxt > n*n:
                    continue
                r, c = get(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, moves+1))
        return -1

# Example usage
if __name__ == "__main__":
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    print(Solution().snakesAndLadders(board))  # Output: 4
