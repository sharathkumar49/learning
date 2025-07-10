"""
LeetCode 2176. Count Equal and Divisible Pairs in an Array

Given an array nums and an integer k, return the number of pairs (i, j) such that i < j, nums[i] == nums[j], and (i * j) is divisible by k.

Example:
Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i], k <= 100
"""

def countPairs(nums, k):
    res = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and (i*j)%k == 0:
                res += 1
    return res

# Example usage:
# print(countPairs([3,1,2,2,2,1,3], 2))  # Output: 4
