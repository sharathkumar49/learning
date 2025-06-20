"""
488. Zuma Game

You are playing a variation of the Zuma Game. Given a string board representing the board and a string hand representing the balls in your hand, return the minimum number of balls you need to insert to clear the board. If you cannot clear the board, return -1.

Constraints:
- 1 <= board.length <= 16
- 1 <= hand.length <= 5
- board and hand consist of only the characters 'R', 'Y', 'B', 'G', 'W'.

Example:
Input: board = "WRRBBW", hand = "RB"
Output: -1
"""

from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove(board):
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    return remove(board[:i] + board[j:])
                i = j
            return board
        memo = {}
        def dfs(board, hand):
            if not board:
                return 0
            key = (board, tuple(sorted(hand.items())))
            if key in memo:
                return memo[key]
            res = float('inf')
            for i in range(len(board)+1):
                for c in hand:
                    if hand[c] == 0:
                        continue
                    if i > 0 and board[i-1] == c:
                        continue
                    if i < len(board) and board[i] == c:
                        continue
                    new_board = remove(board[:i] + c + board[i:])
                    hand[c] -= 1
                    temp = dfs(new_board, hand)
                    if temp != -1:
                        res = min(res, 1 + temp)
                    hand[c] += 1
            memo[key] = -1 if res == float('inf') else res
            return memo[key]
        return dfs(board, Counter(hand))

# Example usage:
sol = Solution()
print(sol.findMinStep("WRRBBW", "RB"))  # Output: -1
