"""
LeetCode 2219. Maximum Sum of Subarray With Minimum Size

Given nums and k, return the maximum sum of a subarray with at least k elements.

Example:
Input: nums = [1,2,3,4,5], k = 2
Output: 14

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length
- -10^4 <= nums[i] <= 10^4
"""

def maxSubarraySum(nums, k):
    n = len(nums)
    max_sum = float('-inf')
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    for i in range(k, n):
        curr_sum += nums[i]
        curr_sum -= nums[i-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Example usage:
# print(maxSubarraySum([1,2,3,4,5], 2))  # Output: 14
