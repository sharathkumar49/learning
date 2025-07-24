"""
LeetCode 2682. Find the Losers of the Circular Game

Given n and k, return the list of losers in the circular game.

Constraints:
- 1 <= n, k <= 50
"""

def circularGameLosers(n, k):
    seen = set()
    i = 0
    step = 1
    while i not in seen:
        seen.add(i)
        i = (i + step * k) % n
        step += 1
    return sorted([x+1 for x in range(n) if x not in seen])
# Example usage:
# print(circularGameLosers(5, 2))  # Output: [4,5]
