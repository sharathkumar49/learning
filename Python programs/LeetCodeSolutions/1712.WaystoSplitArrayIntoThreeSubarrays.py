"""
LeetCode 1712. Ways to Split Array Into Three Subarrays

Given an array nums, return the number of ways to split it into three non-empty contiguous subarrays such that the sum of the first is <= the second, and the second is <= the third.

Example 1:
Input: nums = [1,1,1]
Output: 1

Constraints:
- 3 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^4
"""

def waysToSplit(nums):
    MOD = 10**9 + 7
    n = len(nums)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    res = 0
    j = k = 0
    for i in range(1, n-1):
        j = max(j, i)
        while j < n-1 and prefix[j+1] - prefix[i] < prefix[i]:
            j += 1
        k = max(k, j)
        while k < n-1 and prefix[n] - prefix[k+1] >= prefix[k+1] - prefix[i]:
            k += 1
        res += max(0, k - j)
    return res % MOD

# Example usage:
# nums = [1,1,1]
# print(waysToSplit(nums))  # Output: 1
