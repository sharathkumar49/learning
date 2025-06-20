"""
877. Stone Game

Alice and Bob play a game with piles of stones. Each turn, a player takes a pile from either end. Return true if Alice can win.

Example 1:
Input: piles = [5,3,4,5]
Output: true

Constraints:
- 2 <= piles.length <= 500
- piles.length is even.
- 1 <= piles[i] <= 500
"""
def stoneGame(piles):
    return True  # Alice always wins for even-length piles

# Example usage:
print(stoneGame([5,3,4,5]))  # Output: True
