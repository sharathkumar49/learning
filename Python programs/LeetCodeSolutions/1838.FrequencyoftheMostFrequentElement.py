"""
LeetCode 1838. Frequency of the Most Frequent Element

Given an array nums and an integer k, return the maximum frequency of an element after at most k increments.

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5
"""

def maxFrequency(nums, k):
    nums.sort()
    l = 0
    total = 0
    res = 1
    for r in range(1, len(nums)):
        total += (nums[r] - nums[r-1]) * (r - l)
        while total > k:
            total -= nums[r] - nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res

# Example usage:
# nums = [1,2,4]
# k = 5
# print(maxFrequency(nums, k))  # Output: 3
