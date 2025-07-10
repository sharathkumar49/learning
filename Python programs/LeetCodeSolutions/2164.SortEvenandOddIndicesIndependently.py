"""
LeetCode 2164. Sort Even and Odd Indices Independently

Given an array nums, sort the values at even indices in non-decreasing order and the values at odd indices in non-increasing order. Return the resulting array.

Example:
Input: nums = [4,1,2,3]
Output: [2,3,4,1]

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def sortEvenOdd(nums):
    even = sorted(nums[::2])
    odd = sorted(nums[1::2], reverse=True)
    res = []
    for i in range(len(nums)):
        if i % 2 == 0:
            res.append(even[i//2])
        else:
            res.append(odd[i//2])
    return res

# Example usage:
# print(sortEvenOdd([4,1,2,3]))  # Output: [2,3,4,1]
