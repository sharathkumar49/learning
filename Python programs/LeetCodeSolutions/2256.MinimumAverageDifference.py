"""
LeetCode 2256. Minimum Average Difference

Given nums, return the index with the minimum average difference.

Example:
Input: nums = [2,5,3,9,5,3]
Output: 3

Constraints:
- 2 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""

def minimumAverageDifference(nums):
    n = len(nums)
    total = sum(nums)
    left = 0
    min_diff = float('inf')
    idx = -1
    for i in range(n):
        left += nums[i]
        right = total - left
        left_avg = left // (i+1)
        right_avg = right // (n-i-1) if n-i-1 else 0
        diff = abs(left_avg - right_avg)
        if diff < min_diff:
            min_diff = diff
            idx = i
    return idx

# Example usage:
# print(minimumAverageDifference([2,5,3,9,5,3]))  # Output: 3
