"""
LeetCode 1877. Minimize Maximum Pair Sum in Array

Given an array nums of even length, pair up the elements and minimize the maximum pair sum.

Example:
Input: nums = [3,5,2,3]
Output: 7

Constraints:
- 2 <= nums.length <= 10^5
- nums.length is even
- 1 <= nums[i] <= 10^5
"""

def minPairSum(nums):
    nums.sort()
    return max(nums[i] + nums[~i] for i in range(len(nums)//2))

# Example usage:
# print(minPairSum([3,5,2,3]))  # Output: 7
