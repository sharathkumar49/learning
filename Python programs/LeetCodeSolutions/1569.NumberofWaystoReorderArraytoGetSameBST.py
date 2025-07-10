"""
LeetCode 1569. Number of Ways to Reorder Array to Get Same BST

Given an array nums, return the number of ways to reorder it so that the same BST is formed. Return the answer modulo 10^9 + 7.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= nums.length

Example:
Input: nums = [2,1,3]
Output: 1
"""
def numOfWays(nums):
    from math import comb
    def dfs(arr):
        if len(arr) <= 2:
            return 1
        left = [x for x in arr if x < arr[0]]
        right = [x for x in arr if x > arr[0]]
        return comb(len(arr)-1, len(left)) * dfs(left) * dfs(right)
    return (dfs(nums) - 1) % (10**9 + 7)

# Example usage:
nums = [2,1,3]
print(numOfWays(nums))  # Output: 1
