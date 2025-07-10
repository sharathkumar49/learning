"""
LeetCode 1863. Sum of All Subset XOR Totals

Given an integer array nums, return the sum of all XOR totals for every subset of nums.

Example:
Input: nums = [1,3]
Output: 6

Constraints:
- 1 <= nums.length <= 12
- 1 <= nums[i] <= 20
"""

def subsetXORSum(nums):
    def dfs(i, curr):
        if i == len(nums):
            return curr
        return dfs(i+1, curr) + dfs(i+1, curr ^ nums[i])
    return dfs(0, 0)

# Example usage:
print(subsetXORSum([1,3]))  # Output: 6
