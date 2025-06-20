"""
446. Arithmetic Slices II - Subsequence

Given an integer array nums, return the number of all the arithmetic subsequences of nums.
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- The answer may be very large. Return it modulo 10^9 + 7.

Example:
Input: nums = [2,4,6,8,10]
Output: 7
"""

from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = dp[j][diff]
                dp[i][diff] += cnt + 1
                res += cnt
        return res

# Example usage:
sol = Solution()
print(sol.numberOfArithmeticSlices([2,4,6,8,10]))  # Output: 7
