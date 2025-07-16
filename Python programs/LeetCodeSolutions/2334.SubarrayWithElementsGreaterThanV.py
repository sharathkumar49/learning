"""
LeetCode 2334. Subarray With Elements Greater Than V

Given nums and v, return the length of the longest subarray with all elements greater than v.

Example:
Input: nums = [1,2,3,4,5], v = 2
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
"""

def longestSubarray(nums, v):
    res = curr = 0
    for num in nums:
        if num > v:
            curr += 1
            res = max(res, curr)
        else:
            curr = 0
    return res

# Example usage:
# print(longestSubarray([1,2,3,4,5], 2))  # Output: 3
