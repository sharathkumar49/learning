"""
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons. If you burst the i-th balloon, you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then become adjacent.

Return the maximum coins you can collect by bursting the balloons wisely.

Constraints:
- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100
"""
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                        nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])
        return dp[0][n - 1]

# Example usage:
nums = [3,1,5,8]
print(Solution().maxCoins(nums))  # Output: 167
