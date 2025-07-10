"""
LeetCode 1755. Closest Subsequence Sum

Given an array nums and an integer goal, return the minimum absolute difference between the sum of any subsequence and the goal.

Example 1:
Input: nums = [5,-7,3,5], goal = 6
Output: 0

Constraints:
- 1 <= nums.length <= 40
- -10^7 <= nums[i] <= 10^7
- -10^9 <= goal <= 10^9
"""

def minAbsDifference(nums, goal):
    from bisect import bisect_left
    def get_sums(arr):
        res = {0}
        for x in arr:
            res |= {x + s for s in res}
        return sorted(res)
    n = len(nums)
    left, right = nums[:n//2], nums[n//2:]
    sums_left = get_sums(left)
    sums_right = get_sums(right)
    res = float('inf')
    for s in sums_left:
        t = goal - s
        idx = bisect_left(sums_right, t)
        if idx < len(sums_right):
            res = min(res, abs(s + sums_right[idx] - goal))
        if idx > 0:
            res = min(res, abs(s + sums_right[idx-1] - goal))
    return res

# Example usage:
# nums = [5,-7,3,5]
# goal = 6
# print(minAbsDifference(nums, goal))  # Output: 0
