"""
LeetCode 2206. Divide Array Into Equal Pairs

Given an array of integers nums with even length, return true if it can be divided into pairs with equal values.

Example:
Input: nums = [3,2,3,2,2,2]
Output: true

Constraints:
- nums.length is even
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def divideArray(nums):
    from collections import Counter
    return all(count % 2 == 0 for count in Counter(nums).values())

# Example usage:
# print(divideArray([3,2,3,2,2,2]))  # Output: true
