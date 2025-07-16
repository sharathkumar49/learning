"""
LeetCode 2401. Longest Nice Subarray

Given an array, return the length of the longest nice subarray (no two elements have a set bit in the same position).

Constraints:
- 1 <= nums.length <= 10^5
"""

def longestNiceSubarray(nums):
    res = left = curr = 0
    for right in range(len(nums)):
        while curr & nums[right]:
            curr ^= nums[left]
            left += 1
        curr |= nums[right]
        res = max(res, right-left+1)
    return res

# Example usage:
# print(longestNiceSubarray([1,3,8,48,10]))  # Output: 3
