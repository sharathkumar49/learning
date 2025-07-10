"""
LeetCode 1708. Largest Subarray Length K

Given an integer array nums and an integer k, return the largest subarray of length k.

Example 1:
Input: nums = [1,4,5,2,3], k = 3
Output: [5,2,3]

Constraints:
- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def largestSubarray(nums, k):
    max_idx = 0
    for i in range(1, len(nums) - k + 1):
        if nums[i] > nums[max_idx]:
            max_idx = i
    return nums[max_idx:max_idx+k]

# Example usage:
# nums = [1,4,5,2,3]
# k = 3
# print(largestSubarray(nums, k))  # Output: [5,2,3]
