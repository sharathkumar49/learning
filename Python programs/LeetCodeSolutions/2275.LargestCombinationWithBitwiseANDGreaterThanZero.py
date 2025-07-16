"""
LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero

Given candidates, return the size of the largest combination with bitwise AND > 0.

Example:
Input: candidates = [16,17,71,62,12,24,14]
Output: 4

Constraints:
- 1 <= candidates.length <= 10^5
- 1 <= candidates[i] <= 10^7
"""

def largestCombination(candidates):
    res = 0
    for i in range(24):
        cnt = sum((c>>i)&1 for c in candidates)
        res = max(res, cnt)
    return res

# Example usage:
# print(largestCombination([16,17,71,62,12,24,14]))  # Output: 4
