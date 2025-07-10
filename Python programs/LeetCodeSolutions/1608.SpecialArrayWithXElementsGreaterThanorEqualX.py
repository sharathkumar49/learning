"""
LeetCode 1608. Special Array With X Elements Greater Than or Equal X

Given an array nums, return the number x such that there are exactly x elements in nums that are greater than or equal to x. If there is no such x, return -1.

Example 1:
Input: nums = [3,5]
Output: 2

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""

def specialArray(nums):
    nums.sort()
    n = len(nums)
    for x in range(n+1):
        cnt = sum(num >= x for num in nums)
        if cnt == x:
            return x
    return -1

# Example usage:
# nums = [3,5]
# print(specialArray(nums))  # Output: 2
