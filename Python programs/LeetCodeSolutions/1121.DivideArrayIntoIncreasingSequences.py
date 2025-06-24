"""
1121. Divide Array Into Increasing Sequences

Given an integer array nums, return true if you can divide it into one or more subsequences such that each subsequence is strictly increasing and all elements are used.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [1,2,3,4,5]
Output: true
"""
from typing import List
from collections import Counter

def canDivideIntoSubsequences(nums: List[int]) -> bool:
    n = len(nums)
    max_freq = max(Counter(nums).values())
    return n >= max_freq * (n // max_freq)

# Example usage:
nums = [1,2,3,4,5]
print(canDivideIntoSubsequences(nums))  # Output: True
