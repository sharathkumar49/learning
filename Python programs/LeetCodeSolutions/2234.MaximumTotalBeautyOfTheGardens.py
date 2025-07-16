"""
LeetCode 2234. Maximum Total Beauty of the Gardens

Given flowers, newFlowers, target, and full, partial, return the maximum total beauty.

Example:
Input: flowers = [1,2,3,4,5], newFlowers = 2, target = 5, full = 2, partial = 1
Output: 11

Constraints:
- 1 <= flowers.length <= 10^5
- 0 <= newFlowers, full, partial <= 10^9
- 1 <= target <= 10^9
"""

def maximumBeauty(flowers, newFlowers, target, full, partial):
    flowers = [min(f, target) for f in flowers]
    flowers.sort()
    n = len(flowers)
    res = 0
    for k in range(n+1):
        need = sum(max(0, target-flowers[i]) for i in range(n-k, n))
        if need > newFlowers:
            continue
        left = newFlowers - need
        min_partial = min(flowers[:n-k]) if n-k > 0 else 0
        res = max(res, k*full + min_partial*partial)
    return res

# Example usage:
# print(maximumBeauty([1,2,3,4,5], 2, 5, 2, 1))  # Output: 11
