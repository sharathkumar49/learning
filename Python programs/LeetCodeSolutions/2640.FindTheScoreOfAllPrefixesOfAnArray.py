"""
LeetCode 2640. Find the Score of All Prefixes of an Array

Given nums, return the score of all prefixes.

Constraints:
- 1 <= nums.length <= 10^5
"""

def findPrefixScore(nums):
    res = []
    mx = total = 0
    for x in nums:
        mx = max(mx, x)
        total += mx + x
        res.append(total)
    return res
# Example usage:
# print(findPrefixScore([2,3,7,5,10]))  # Output: [4, 10, 24, 36, 56]
