"""
494. Target Sum

Given an integer array nums and an integer target, return the number of ways to assign + and - signs to make the sum of nums be target.

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums) <= 1000

Example:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
"""

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for s in dp:
                next_dp[s + num] += dp[s]
                next_dp[s - num] += dp[s]
            dp = next_dp
        return dp[target]

# Example usage:
sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], 3))  # Output: 5
