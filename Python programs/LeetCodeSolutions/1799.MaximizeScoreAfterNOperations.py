"""
LeetCode 1799. Maximize Score After N Operations

Given an array nums of length 2n, return the maximum score after n operations as described in the problem.

Example 1:
Input: nums = [1,2,3,4,5,6]
Output: 14

Constraints:
- 1 <= n <= 7
- nums.length == 2 * n
- 1 <= nums[i] <= 10^6
"""

def maxScore(nums):
    from math import gcd
    from functools import lru_cache
    n = len(nums)//2
    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0
        res = 0
        bits = [i for i in range(2*n) if (mask >> i) & 1]
        for i in range(len(bits)):
            for j in range(i+1, len(bits)):
                new_mask = mask ^ (1<<bits[i]) ^ (1<<bits[j])
                res = max(res, dp(new_mask) + gcd(nums[bits[i]], nums[bits[j]]) * (n - bin(mask).count('1')//2 + 1))
        return res
    return dp((1<<(2*n))-1)

# Example usage:
# nums = [1,2,3,4,5,6]
# print(maxScore(nums))  # Output: 14
