"""
LeetCode 2183. Count Array Pairs Divisible by K

Given an array nums and an integer k, return the number of pairs (i, j) such that i < j and (nums[i] * nums[j]) is divisible by k.

Example:
Input: nums = [1,2,3,4,5], k = 2
Output: 7

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], k <= 10^5
"""

def countPairs(nums, k):
    from math import gcd
    from collections import Counter
    c = Counter()
    res = 0
    for x in nums:
        g = gcd(x, k)
        for y in c:
            if (g * y) % k == 0:
                res += c[y]
        c[g] += 1
    return res

# Example usage:
# print(countPairs([1,2,3,4,5], 2))  # Output: 7
