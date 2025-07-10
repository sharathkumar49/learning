"""
LeetCode 1770. Maximum Score from Performing Multiplication Operations

Given arrays nums and multipliers, return the maximum score after performing operations as described in the problem.

Example 1:
Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14

Constraints:
- 1 <= nums.length, m <= 10^3
- m == multipliers.length
- -1000 <= nums[i], multipliers[i] <= 1000
"""

def maximumScore(nums, multipliers):
    n, m = len(nums), len(multipliers)
    dp = [0]*(m+1)
    for i in range(m-1, -1, -1):
        new_dp = dp[:]
        for left in range(i+1):
            new_dp[left] = max(multipliers[i]*nums[left] + dp[left+1], multipliers[i]*nums[n-1-(i-left)] + dp[left])
        dp = new_dp
    return dp[0]

# Example usage:
# nums = [1,2,3]
# multipliers = [3,2,1]
# print(maximumScore(nums, multipliers))  # Output: 14
