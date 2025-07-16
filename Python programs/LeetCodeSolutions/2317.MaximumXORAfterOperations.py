"""
LeetCode 2317. Maximum XOR After Operations

Given nums, return the maximum XOR value after performing operations.

Example:
Input: nums = [3,2,4,6]
Output: 7

Constraints:
- 1 <= nums.length <= 10^5
"""

def maximumXOR(nums):
    res = 0
    for num in nums:
        res |= num
    return res

# Example usage:
# print(maximumXOR([3,2,4,6]))  # Output: 7
