"""
LeetCode 1959. Minimum Total Space Wasted With K Resizing

Given an array nums and an integer k, return the minimum total space wasted with at most k resizing operations.

Example:
Input: nums = [10,20,15,30,20], k = 2
Output: 15

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 10^9
- 0 <= k <= min(200, nums.length-1)
"""

def minSpaceWastedKResizing(nums, k):
    n = len(nums)
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, k):
        if i == n: return 0
        res = float('inf')
        mx = 0
        for j in range(i, n):
            mx = max(mx, nums[j])
            res = min(res, mx*(j-i+1)-sum(nums[i:j+1]) + dp(j+1, k-1)) if k else min(res, mx*(j-i+1)-sum(nums[i:j+1]) + (0 if j+1==n else float('inf')))
        return res
    return dp(0, k)

# Example usage:
# print(minSpaceWastedKResizing([10,20,15,30,20], 2))  # Output: 15
