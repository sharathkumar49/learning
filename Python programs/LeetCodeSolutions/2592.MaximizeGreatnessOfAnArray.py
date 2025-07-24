"""
LeetCode 2592. Maximize Greatness of an Array

Given an array, maximize its greatness by rearrangement.

Constraints:
- 1 <= nums.length <= 10^5
"""

def maximizeGreatness(nums):
    nums.sort()
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[j] < nums[i]:
            j += 1
    return j
# Example usage:
# print(maximizeGreatness([1,3,5,2,1,3,1]))  # Output: 4
