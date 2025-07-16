"""
LeetCode 2341. Maximum Number of Pairs in Array

Given nums, return the maximum number of pairs and the number of leftover elements.

Example:
Input: nums = [1,3,2,1,3,2,2]
Output: [3,1]

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def numberOfPairs(nums):
    from collections import Counter
    c = Counter(nums)
    pairs = sum(v//2 for v in c.values())
    leftovers = sum(v%2 for v in c.values())
    return [pairs, leftovers]

# Example usage:
# print(numberOfPairs([1,3,2,1,3,2,2]))  # Output: [3,1]
