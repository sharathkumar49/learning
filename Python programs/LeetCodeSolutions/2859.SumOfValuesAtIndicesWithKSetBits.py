"""
LeetCode 2859. Sum of Values at Indices With K Set Bits

Given nums and k, return the sum of values at indices with k set bits.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= k <= 17
"""

def sumIndicesWithKSetBits(nums, k):
    return sum(val for i, val in enumerate(nums) if bin(i).count('1') == k)
# Example usage:
# print(sumIndicesWithKSetBits([5,10,1,5,2], 1))  # Output: 10
