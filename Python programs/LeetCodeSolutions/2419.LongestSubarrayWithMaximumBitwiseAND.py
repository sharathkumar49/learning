"""
LeetCode 2419. Longest Subarray With Maximum Bitwise AND

Given an array, return the length of the longest subarray with maximum bitwise AND.

Constraints:
- 1 <= nums.length <= 10^5
"""

def longestSubarray(nums):
    m = max(nums)
    return max(len(list(g)) for k, g in __import__('itertools').groupby(nums) if k==m)

# Example usage:
# print(longestSubarray([1,2,3,3,2,2,2]))  # Output: 3
