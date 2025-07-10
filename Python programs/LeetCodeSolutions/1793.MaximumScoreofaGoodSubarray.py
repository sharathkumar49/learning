"""
LeetCode 1793. Maximum Score of a Good Subarray

Given an array nums and an integer k, return the maximum score of a good subarray as described in the problem.

Example 1:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 2 * 10^4
- 0 <= k < nums.length
"""

def maximumScore(nums, k):
    n = len(nums)
    l = r = k
    res = mn = nums[k]
    while l > 0 or r < n-1:
        if l > 0 and (r == n-1 or nums[l-1] > nums[r+1]):
            l -= 1
            mn = min(mn, nums[l])
        else:
            r += 1
            mn = min(mn, nums[r])
        res = max(res, mn * (r - l + 1))
    return res

# Example usage:
# nums = [1,4,3,7,4,5]
# k = 3
# print(maximumScore(nums, k))  # Output: 15
