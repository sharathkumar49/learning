"""
LeetCode 2357. Make Array Zero by Subtracting Equal Amounts

Given nums, return the minimum number of operations to make all elements zero.

Example:
Input: nums = [1,5,0,3,5]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

def minimumOperations(nums):
    return len(set(nums)-{0})

# Example usage:
# print(minimumOperations([1,5,0,3,5]))  # Output: 3
