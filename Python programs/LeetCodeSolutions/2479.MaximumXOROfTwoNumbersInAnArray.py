"""
LeetCode 2479. Maximum XOR of Two Numbers in an Array

Given an array, return the maximum XOR of two numbers.

Constraints:
- 2 <= nums.length <= 2*10^5
"""

def maximumXOR(nums):
    res = 0
    for x in nums:
        for y in nums:
            if x != y:
                res = max(res, x^y)
    return res

# Example usage:
# print(maximumXOR([3,10,5,25,2,8]))  # Output: 28
