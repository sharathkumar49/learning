"""
LeetCode 2200. Find All K-Distant Indices in an Array

Given an array nums, an integer key, and an integer k, return all indices i such that there exists a j with nums[j] == key and abs(i-j) <= k.

Example:
Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
Output: [1,2,3,4,5,6]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i], key <= 1000
- 1 <= k <= nums.length
"""

def findKDistantIndices(nums, key, k):
    res = set()
    n = len(nums)
    for i, x in enumerate(nums):
        if x == key:
            for j in range(max(0, i-k), min(n, i+k+1)):
                res.add(j)
    return sorted(res)

# Example usage:
# print(findKDistantIndices([3,4,9,1,3,9,5], 9, 1))  # Output: [1,2,3,4,5,6]
