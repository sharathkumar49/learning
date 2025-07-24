"""
LeetCode 2587. Rearrange Array to Maximize Prefix Score

Given an array, rearrange to maximize prefix score.

Constraints:
- 1 <= nums.length <= 10^5
"""

def maxScore(nums):
    nums.sort(reverse=True)
    s = res = 0
    for x in nums:
        s += x
        if s > 0:
            res += 1
        else:
            break
    return res
# Example usage:
# print(maxScore([2,-1,0,1,-3,3,-3]))  # Output: 6
