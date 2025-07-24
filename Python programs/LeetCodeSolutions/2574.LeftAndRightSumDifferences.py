"""
LeetCode 2574. Left and Right Sum Differences

Given an array, return an array of left and right sum differences.

Constraints:
- 1 <= nums.length <= 10^5
"""

def leftRightDifference(nums):
    left, right = 0, sum(nums)
    res = []
    for x in nums:
        right -= x
        res.append(abs(left-right))
        left += x
    return res
# Example usage:
# print(leftRightDifference([10,4,8,3]))  # Output: [15,1,11,22]
