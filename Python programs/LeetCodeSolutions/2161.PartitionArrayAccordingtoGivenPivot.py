"""
LeetCode 2161. Partition Array According to Given Pivot

Given an array nums and an integer pivot, rearrange the array so that all elements less than pivot come before elements equal to pivot, which come before elements greater than pivot. Return the resulting array.

Example:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

Constraints:
- 1 <= nums.length <= 10^5
- -10^6 <= nums[i] <= 10^6
- -10^6 <= pivot <= 10^6
"""

def pivotArray(nums, pivot):
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]
    return less + equal + greater

# Example usage:
# print(pivotArray([9,12,5,10,14,3,10], 10))  # Output: [9,5,3,10,10,12,14]
