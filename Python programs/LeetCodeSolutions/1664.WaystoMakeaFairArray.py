"""
LeetCode 1664. Ways to Make a Fair Array

Given an array nums, return the number of ways to make the array fair by removing exactly one element.

Example 1:
Input: nums = [2,1,6,4]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def waysToMakeFair(nums):
    n = len(nums)
    odd = [0]*(n+1)
    even = [0]*(n+1)
    for i in range(n):
        odd[i+1] = odd[i]
        even[i+1] = even[i]
        if i % 2 == 0:
            even[i+1] += nums[i]
        else:
            odd[i+1] += nums[i]
    res = 0
    for i in range(n):
        if odd[i] + even[n] - even[i+1] == even[i] + odd[n] - odd[i+1]:
            res += 1
    return res

# Example usage:
# nums = [2,1,6,4]
# print(waysToMakeFair(nums))  # Output: 1
