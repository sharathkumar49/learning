"""
LeetCode 2348. Number of Zero-Filled Subarrays

Given nums, return the number of zero-filled subarrays.

Example:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6

Constraints:
- 1 <= nums.length <= 10^5
"""

def zeroFilledSubarray(nums):
    res = cnt = 0
    for num in nums:
        if num == 0:
            cnt += 1
            res += cnt
        else:
            cnt = 0
    return res

# Example usage:
# print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))  # Output: 6
