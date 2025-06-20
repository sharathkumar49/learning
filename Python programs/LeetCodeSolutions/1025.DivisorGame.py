"""
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first. On each turn, a player chooses x with 0 < x < N and N % x == 0 and replaces N with N - x. The player who cannot make a move loses.

Return true if Alice wins the game, otherwise false.

Constraints:
- 1 <= N <= 1000

Example:
Input: N = 2
Output: true
Explanation: Alice chooses 1, and Bob has no move.
"""
def divisorGame(N: int) -> bool:
    return N % 2 == 0

# Example usage:
N = 2
print(divisorGame(N))  # Output: True
