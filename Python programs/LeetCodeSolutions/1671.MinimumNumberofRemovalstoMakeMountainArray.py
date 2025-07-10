"""
LeetCode 1671. Minimum Number of Removals to Make Mountain Array

Given an array nums, return the minimum number of elements to remove to make it a mountain array.

Example 1:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3

Constraints:
- 3 <= nums.length <= 1000
- 1 <= nums[i] <= 10^9
"""

def minimumMountainRemovals(nums):
    n = len(nums)
    inc = [1]*n
    dec = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                inc[i] = max(inc[i], inc[j]+1)
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                dec[i] = max(dec[i], dec[j]+1)
    res = n
    for i in range(n):
        if inc[i] > 1 and dec[i] > 1:
            res = min(res, n - (inc[i] + dec[i] - 1))
    return res

# Example usage:
# nums = [2,1,1,5,6,2,3,1]
# print(minimumMountainRemovals(nums))  # Output: 3
