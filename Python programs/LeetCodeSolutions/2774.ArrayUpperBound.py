"""
LeetCode 2774. Array Upper Bound

Given nums and x, return the upper bound index for x in nums.

Constraints:
- 1 <= nums.length <= 10^5
"""

def upperBound(nums, x):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] <= x:
            l = m + 1
        else:
            r = m
    return l
# Example usage:
# print(upperBound([1,2,4,4,5], 4))  # Output: 4
