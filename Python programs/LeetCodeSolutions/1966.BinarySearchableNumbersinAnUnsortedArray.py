"""
LeetCode 1966. Binary Searchable Numbers in an Unsorted Array

Given an array nums, return the number of binary searchable numbers.

Example:
Input: nums = [1,3,2,4,5]
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def binarySearchableNumbers(nums):
    n = len(nums)
    left_max = [0]*n
    right_min = [0]*n
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], nums[i])
    right_min[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], nums[i])
    return sum(left_max[i] <= nums[i] <= right_min[i] for i in range(n))

# Example usage:
# print(binarySearchableNumbers([1,3,2,4,5]))  # Output: 3
