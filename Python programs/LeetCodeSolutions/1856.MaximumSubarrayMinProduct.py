"""
LeetCode 1856. Maximum Subarray Min-Product

Given an array of integers nums, the min-product of a non-empty subarray is defined as the minimum value in the subarray multiplied by the sum of the subarray. Return the maximum min-product of any non-empty subarray. Since the answer may be large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [1,2,3,2]
Output: 14

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^7
"""

def maxSumMinProduct(nums):
    n = len(nums)
    stack = []
    left = [0]*n
    right = [n]*n
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            right[stack[-1]] = i
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    res = 0
    for i in range(n):
        total = prefix[right[i]] - prefix[left[i]+1]
        res = max(res, total * nums[i])
    return res % (10**9+7)

# Example usage:
# nums = [1,2,3,2]
# print(maxSumMinProduct(nums))  # Output: 14
