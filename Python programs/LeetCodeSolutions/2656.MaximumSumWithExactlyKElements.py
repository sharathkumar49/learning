"""
LeetCode 2656. Maximum Sum With Exactly K Elements

Given nums and k, return the maximum sum with exactly k elements.

Constraints:
- 1 <= nums.length, k <= 10^5
"""

def maximizeSum(nums, k):
    m = max(nums)
    return sum(m+i for i in range(k))
# Example usage:
# print(maximizeSum([1,2,3,4,5], 3))  # Output: 18
