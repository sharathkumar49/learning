"""
LeetCode 1567. Maximum Length of Subarray With Positive Product

Given an array nums, return the length of the longest subarray with a positive product.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [1,-2,-3,4]
Output: 4
"""
def getMaxLen(nums):
    pos = neg = res = 0
    for n in nums:
        if n == 0:
            pos = neg = 0
        elif n > 0:
            pos += 1
            neg = neg + 1 if neg else 0
        else:
            pos, neg = neg + 1 if neg else 0, pos + 1
        res = max(res, pos)
    return res

# Example usage:
nums = [1,-2,-3,4]
print(getMaxLen(nums))  # Output: 4
