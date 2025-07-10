"""
LeetCode 2149. Rearrange Array Elements by Sign

Given an integer array nums, rearrange the elements by sign so that the positive and negative numbers alternate, starting with positive. Return the resulting array. The input is guaranteed to have the same number of positive and negative numbers.

Example:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Constraints:
- 2 <= nums.length <= 2 * 10^5
- nums.length is even
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers.
"""

def rearrangeArray(nums):
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    res = []
    for p, n in zip(pos, neg):
        res.extend([p, n])
    return res

# Example usage:
# print(rearrangeArray([3,1,-2,-5,2,-4]))  # Output: [3,-2,1,-5,2,-4]
