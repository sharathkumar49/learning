# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses are broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]

# Example usage
nums = [2,7,9,3,1]
print("Max money robbed:", rob(nums))  # Output: 12
