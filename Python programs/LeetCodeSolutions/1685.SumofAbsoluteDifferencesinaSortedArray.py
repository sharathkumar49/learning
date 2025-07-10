"""
LeetCode 1685. Sum of Absolute Differences in a Sorted Array

Given a sorted array nums, return an array answer where answer[i] is the sum of absolute differences between nums[i] and every other element.

Example 1:
Input: nums = [2,3,5]
Output: [4,3,5]

Constraints:
- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def getSumAbsoluteDifferences(nums):
    n = len(nums)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    res = []
    for i, x in enumerate(nums):
        left = x*i - prefix[i]
        right = (prefix[n] - prefix[i+1]) - x*(n-i-1)
        res.append(left + right)
    return res

# Example usage:
# nums = [2,3,5]
# print(getSumAbsoluteDifferences(nums))  # Output: [4,3,5]
