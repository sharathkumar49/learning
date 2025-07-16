"""
LeetCode 2366. Minimum Replacement to Sort the Array

Given nums, return the minimum replacements to sort the array.

Example:
Input: nums = [3,9,3]
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
"""

def minimumReplacement(nums):
    res = 0
    prev = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > prev:
            k = (nums[i]+prev-1)//prev
            res += k-1
            prev = nums[i]//k
        else:
            prev = nums[i]
    return res

# Example usage:
# print(minimumReplacement([3,9,3]))  # Output: 2
