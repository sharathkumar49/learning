"""
LeetCode 2760. Longest Even Odd Subarray With Threshold

Given nums and threshold, return the length of the longest even-odd subarray with all elements <= threshold.

Constraints:
- 1 <= nums.length <= 10^5
"""

def longestAlternatingSubarray(nums, threshold):
    res = cur = 0
    for i, x in enumerate(nums):
        if x > threshold or (i > 0 and (nums[i-1]%2 == x%2)):
            cur = 0
        if x <= threshold and (cur == 0 and x%2 == 0 or cur > 0 and nums[i-1]%2 != x%2):
            cur += 1
            res = max(res, cur)
    return res
# Example usage:
# print(longestAlternatingSubarray([3,2,5,4], 5))  # Output: 3
