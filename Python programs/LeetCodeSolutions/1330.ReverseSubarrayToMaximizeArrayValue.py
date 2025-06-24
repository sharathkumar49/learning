"""
LeetCode 1330. Reverse Subarray To Maximize Array Value

Given an array nums, you can reverse one subarray to maximize the sum of absolute differences between adjacent elements. Return the maximum possible value.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 10^5

Example:
Input: nums = [2,3,1,5,4]
Output: 10
"""
def maxValueAfterReverse(nums):
    n = len(nums)
    base = sum(abs(nums[i] - nums[i-1]) for i in range(1, n))
    res = base
    for i in range(1, n-1):
        res = max(res, base + abs(nums[0] - nums[i+1]) - abs(nums[i] - nums[i+1]))
        res = max(res, base + abs(nums[-1] - nums[i-1]) - abs(nums[i] - nums[i-1]))
    min2, max2 = float('inf'), float('-inf')
    for i in range(1, n):
        x, y = nums[i-1], nums[i]
        min2 = min(min2, max(x, y))
        max2 = max(max2, min(x, y))
    res = max(res, base + 2 * (max2 - min2))
    return res

# Example usage:
nums = [2,3,1,5,4]
print(maxValueAfterReverse(nums))  # Output: 10
