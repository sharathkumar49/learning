"""
LeetCode 1673. Find the Most Competitive Subsequence

Given an integer array nums and an integer k, return the most competitive subsequence of length k.

Example 1:
Input: nums = [3,5,2,6], k = 2
Output: [2,6]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
- 1 <= nums[i] <= 10^9
"""

def mostCompetitive(nums, k):
    stack = []
    n = len(nums)
    for i, num in enumerate(nums):
        while stack and len(stack) + n - i > k and stack[-1] > num:
            stack.pop()
        if len(stack) < k:
            stack.append(num)
    return stack

# Example usage:
# nums = [3,5,2,6]
# k = 2
# print(mostCompetitive(nums, k))  # Output: [2,6]
