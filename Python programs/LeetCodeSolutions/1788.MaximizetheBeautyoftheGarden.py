"""
LeetCode 1788. Maximize the Beauty of the Garden

Given an array flowers and an integer newFlowers, target, full, partial, return the maximum beauty of the garden.

Example 1:
Input: flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
Output: 14

Constraints:
- 1 <= flowers.length <= 10^5
- 1 <= newFlowers, target, full, partial <= 10^5
"""

def maximumBeauty(flowers, newFlowers, target, full, partial):
    flowers = [min(f, target) for f in flowers]
    flowers.sort()
    n = len(flowers)
    pre = [0]*(n+1)
    for i in range(n):
        pre[i+1] = pre[i] + flowers[i]
    res = 0
    for k in range(n+1):
        if k*target > pre[n] + newFlowers:
            break
        left = newFlowers - (k*target - (pre[n] - pre[n-k] if k else 0))
        l, r = flowers[0], target-1
        while l < r:
            m = (l+r+1)//2
            idx = next((i for i in range(n-k) if flowers[i] >= m), n-k)
            need = m*idx - pre[idx]
            if need <= left:
                l = m
            else:
                r = m-1
        res = max(res, k*full + l*partial)
    return res

# Example usage:
# flowers = [1,3,1,1]
# newFlowers = 7
# target = 6
# full = 12
# partial = 1
# print(maximumBeauty(flowers, newFlowers, target, full, partial))  # Output: 14
