"""
LeetCode 2308. Minimum Sum of Mountain Triplets

Given nums, return the minimum sum of a mountain triplet.

Example:
Input: nums = [1,2,3,4,5]
Output: 6

Constraints:
- 3 <= nums.length <= 10^5
"""

def minimumSum(nums):
    n = len(nums)
    left = [float('inf')]*n
    right = [float('inf')]*n
    for i in range(1, n):
        left[i] = min(left[i-1], nums[i-1])
    for i in range(n-2, -1, -1):
        right[i] = min(right[i+1], nums[i+1])
    res = float('inf')
    for i in range(1, n-1):
        if left[i] < nums[i] < right[i]:
            res = min(res, left[i]+nums[i]+right[i])
    return res if res != float('inf') else -1

# Example usage:
# print(minimumSum([1,2,3,4,5]))  # Output: 6
