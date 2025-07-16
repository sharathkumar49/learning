"""
LeetCode 2260. Minimum Consecutive Cards to Pick Up

Given cards, return the minimum number of consecutive cards to pick up to have a pair.

Example:
Input: cards = [3,4,2,3,4,7]
Output: 2

Constraints:
- 1 <= cards.length <= 10^5
- 1 <= cards[i] <= 10^6
"""

def minimumCardPickup(cards):
    last = {}
    res = float('inf')
    for i, c in enumerate(cards):
        if c in last:
            res = min(res, i - last[c] + 1)
        last[c] = i
    return res if res != float('inf') else -1

# Example usage:
# print(minimumCardPickup([3,4,2,3,4,7]))  # Output: 2
