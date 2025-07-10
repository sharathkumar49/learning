"""
LeetCode 1752. Check if Array Is Sorted and Rotated

Given an array nums, return true if it is sorted and rotated.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def check(nums):
    cnt = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            cnt += 1
    return cnt <= 1

# Example usage:
# nums = [3,4,5,1,2]
# print(check(nums))  # Output: True
