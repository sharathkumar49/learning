"""
LeetCode 1714. Sum Of Special Evenly-Spaced Elements In Array

Given an integer array nums, an integer queries, and for each query [l, r, d], return the sum of elements nums[i] where l <= i <= r and (i - l) % d == 0.

Example 1:
Input: nums = [1,2,3,4,5], queries = [[0,4,2]]
Output: [9]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= queries.length <= 10^5
- 0 <= l <= r < nums.length
- 1 <= d <= nums.length
"""

def sumOfSpecialElements(nums, queries):
    res = []
    for l, r, d in queries:
        s = 0
        for i in range(l, r+1):
            if (i-l) % d == 0:
                s += nums[i]
        res.append(s)
    return res

# Example usage:
# nums = [1,2,3,4,5]
# queries = [[0,4,2]]
# print(sumOfSpecialElements(nums, queries))  # Output: [9]
