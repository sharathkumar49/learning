"""
LeetCode 1950. Maximum of Minimum Values in All Subarrays

Given an array nums, return an array res where res[i] is the maximum of minimum values of all subarrays of length i+1.

Example:
Input: nums = [1,2,3,2]
Output: [3,2,1,1]

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def maxOfMin(nums):
    n = len(nums)
    res = [0]*n
    stack = []
    left = [-1]*n
    right = [n]*n
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            right[stack.pop()] = i
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    for i in range(n):
        l = right[i] - left[i] - 1
        res[l-1] = max(res[l-1], nums[i])
    for i in range(n-2, -1, -1):
        res[i] = max(res[i], res[i+1])
    return res

# Example usage:
# print(maxOfMin([1,2,3,2]))  # Output: [3,2,1,1]
