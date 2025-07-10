"""
LeetCode 1911. Maximum Alternating Subsequence Sum

Given an integer array nums, return the maximum alternating subsequence sum.

Example:
Input: nums = [4,2,5,3]
Output: 7

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def maxAlternatingSum(nums):
    even = odd = 0
    for x in nums[::-1]:
        even, odd = max(even, odd + x), max(odd, even - x)
    return even

# Example usage:
# print(maxAlternatingSum([4,2,5,3]))  # Output: 7
