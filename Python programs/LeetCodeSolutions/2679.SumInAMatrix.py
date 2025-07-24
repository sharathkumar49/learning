"""
LeetCode 2679. Sum in a Matrix

Given a matrix, return the maximum sum by picking one element from each row.

Constraints:
- 1 <= nums.length, nums[0].length <= 50
"""

def matrixSum(nums):
    for row in nums:
        row.sort()
    return sum(max(row[i] for row in nums) for i in range(len(nums[0])))
# Example usage:
# print(matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]]))  # Output: 15
