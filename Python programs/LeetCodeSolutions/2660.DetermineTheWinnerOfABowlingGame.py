"""
LeetCode 2660. Determine the Winner of a Bowling Game

Given player1 and player2 scores, return the winner.

Constraints:
- 1 <= player1.length == player2.length <= 1000
"""

def isWinner(player1, player2):
    def score(p):
        s = 0
        for i, x in enumerate(p):
            if i > 0 and (p[i-1] == 10 or (i > 1 and p[i-2] == 10)):
                s += 2*x
            else:
                s += x
        return s
    a, b = score(player1), score(player2)
    return 1 if a > b else 2 if b > a else 0
# Example usage:
# print(isWinner([4,10,7,9],[6,5,2,3]))  # Output: 1
