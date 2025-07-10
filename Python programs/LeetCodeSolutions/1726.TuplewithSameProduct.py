"""
LeetCode 1726. Tuple with Same Product

Given an array nums, return the number of tuples (a, b, c, d) such that nums[a] * nums[b] == nums[c] * nums[d] and a, b, c, d are distinct.

Example 1:
Input: nums = [2,3,4,6]
Output: 8

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
"""

def tupleSameProduct(nums):
    from collections import Counter
    n = len(nums)
    prod = Counter()
    for i in range(n):
        for j in range(i+1, n):
            prod[nums[i]*nums[j]] += 1
    res = 0
    for v in prod.values():
        res += v * (v-1) * 4
    return res

# Example usage:
# nums = [2,3,4,6]
# print(tupleSameProduct(nums))  # Output: 8
