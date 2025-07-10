"""
LeetCode 1968. Array With Elements Not Equal to Average of Neighbors

Given an array nums, return any permutation of nums such that no element is equal to the average of its neighbors.

Example:
Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]

Constraints:
- 3 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

def rearrangeArray(nums):
    nums.sort()
    res = [0]*len(nums)
    l, r = 0, (len(nums)+1)//2
    for i in range(len(nums)):
        if i%2==0:
            res[i] = nums[l]
            l += 1
        else:
            res[i] = nums[r]
            r += 1
    return res

# Example usage:
# print(rearrangeArray([1,2,3,4,5]))  # Output: [1,2,4,5,3]
