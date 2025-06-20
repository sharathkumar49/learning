"""
875. Koko Eating Bananas

Koko loves to eat bananas. Given piles of bananas and an integer h, return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    while l < r:
        m = (l + r) // 2
        if sum((p + m - 1) // m for p in piles) > h:
            l = m + 1
        else:
            r = m
    return l

# Example usage:
print(minEatingSpeed([3,6,7,11], 8))  # Output: 4
print(minEatingSpeed([30,11,23,4,20], 5))  # Output: 30
