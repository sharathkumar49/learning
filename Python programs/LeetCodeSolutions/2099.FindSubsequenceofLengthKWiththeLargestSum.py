"""
LeetCode 2099. Find Subsequence of Length K With the Largest Sum

Given an array nums and an integer k, return the subsequence of length k with the largest sum.

Example:
Input: nums = [2,1,3,3], k = 2
Output: [3,3]

Constraints:
- 1 <= k <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
"""

def maxSubsequence(nums, k):
    idx = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
    idx.sort()
    return [nums[i] for i in idx]

# Example usage:
# print(maxSubsequence([2,1,3,3], 2))  # Output: [3,3]
