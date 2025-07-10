"""
LeetCode 1658. Minimum Operations to Reduce X to Zero

Given an array nums and an integer x, return the minimum number of operations to reduce x to zero by removing elements from the left or right.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= x <= 10^9
"""

def minOperations(nums, x):
    total = sum(nums)
    target = total - x
    n = len(nums)
    left = 0
    curr = 0
    res = -1
    for right in range(n):
        curr += nums[right]
        while left <= right and curr > target:
            curr -= nums[left]
            left += 1
        if curr == target:
            res = max(res, right - left + 1)
    return n - res if res != -1 else -1

# Example usage:
# nums = [1,1,4,2,3]
# x = 5
# print(minOperations(nums, x))  # Output: 2
