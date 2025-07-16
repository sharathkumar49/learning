"""
LeetCode 2369. Check if There Is a Valid Partition for the Array

Given nums, return true if there is a valid partition for the array.

Example:
Input: nums = [4,4,4,5,6]
Output: True

Constraints:
- 2 <= nums.length <= 10^5
"""

def validPartition(nums):
    n = len(nums)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(2, n+1):
        if dp[i-2] and nums[i-2] == nums[i-1]:
            dp[i] = True
        if i > 2 and dp[i-3] and ((nums[i-3] == nums[i-2] == nums[i-1]) or (nums[i-3]+1 == nums[i-2] and nums[i-2]+1 == nums[i-1])):
            dp[i] = True
    return dp[n]

# Example usage:
# print(validPartition([4,4,4,5,6]))  # Output: True
