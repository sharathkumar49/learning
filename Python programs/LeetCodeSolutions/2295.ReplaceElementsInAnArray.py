"""
LeetCode 2295. Replace Elements in an Array

Given nums, operations, return the array after performing all operations.

Example:
Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
Output: [3,2,7,1]

Constraints:
- 1 <= nums.length, operations.length <= 10^5
"""

def arrayChange(nums, operations):
    pos = {num:i for i,num in enumerate(nums)}
    for old, new in operations:
        i = pos.pop(old)
        nums[i] = new
        pos[new] = i
    return nums

# Example usage:
# print(arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]))  # Output: [3,2,7,1]
