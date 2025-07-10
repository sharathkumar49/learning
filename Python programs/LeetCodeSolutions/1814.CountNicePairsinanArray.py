"""
LeetCode 1814. Count Nice Pairs in an Array

Given an array nums, return the number of nice pairs (i, j) such that nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]).

Example 1:
Input: nums = [42,11,1,97]
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

def countNicePairs(nums):
    from collections import Counter
    MOD = 10**9+7
    def rev(x):
        return int(str(x)[::-1])
    count = Counter()
    res = 0
    for x in nums:
        d = x - rev(x)
        res = (res + count[d]) % MOD
        count[d] += 1
    return res

# Example usage:
# nums = [42,11,1,97]
# print(countNicePairs(nums))  # Output: 2
