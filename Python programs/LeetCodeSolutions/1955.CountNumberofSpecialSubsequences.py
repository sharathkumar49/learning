"""
LeetCode 1955. Count Number of Special Subsequences

Given an array nums, return the number of special subsequences. A special subsequence is a sequence of 0s, then 1s, then 2s.

Example:
Input: nums = [0,1,2,2]
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 2
"""

MOD = 10**9+7

def countSpecialSubsequences(nums):
    dp = [0,0,0]
    for x in nums:
        if x == 0:
            dp[0] = (2*dp[0]+1)%MOD
        elif x == 1:
            dp[1] = (2*dp[1]+dp[0])%MOD
        else:
            dp[2] = (2*dp[2]+dp[1])%MOD
    return dp[2]

# Example usage:
# print(countSpecialSubsequences([0,1,2,2]))  # Output: 3
