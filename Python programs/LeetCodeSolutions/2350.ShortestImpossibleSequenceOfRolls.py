"""
LeetCode 2350. Shortest Impossible Sequence of Rolls

Given rolls and k, return the length of the shortest impossible sequence.

Example:
Input: rolls = [1,2,1,2], k = 2
Output: 2

Constraints:
- 1 <= rolls.length <= 10^5
- 1 <= k <= 10^5
"""

def shortestSequence(rolls, k):
    seen = set()
    res = 1
    for r in rolls:
        seen.add(r)
        if len(seen) == k:
            res += 1
            seen.clear()
    return res

# Example usage:
# print(shortestSequence([1,2,1,2], 2))  # Output: 2
