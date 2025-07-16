"""
LeetCode 2242. Maximum Score of a Good Subarray

Given nums and k, return the maximum score of a good subarray.

Example:
Input: nums = [1,4,3,7,4,5], k = 3
Output: 15

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def maximumScore(nums, k):
    n = len(nums)
    left = right = k
    min_val = nums[k]
    res = min_val
    while left > 0 or right < n-1:
        if left == 0:
            right += 1
        elif right == n-1:
            left -= 1
        elif nums[left-1] > nums[right+1]:
            left -= 1
        else:
            right += 1
        min_val = min(min_val, nums[left], nums[right])
        res = max(res, min_val*(right-left+1))
    return res

# Example usage:
# print(maximumScore([1,4,3,7,4,5], 3))  # Output: 15
