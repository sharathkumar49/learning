"""
LeetCode 2501. Longest Square Streak in an Array

Given an array, return the length of the longest square streak.

Constraints:
- 1 <= nums.length <= 10^5
"""

def longestSquareStreak(nums):
    s = set(nums)
    res = -1
    for x in nums:
        cnt = 0
        while x in s:
            cnt += 1
            x *= x
        if cnt > 1:
            res = max(res, cnt)
    return res

# Example usage:
# print(longestSquareStreak([4,2,16,256]))  # Output: 4
