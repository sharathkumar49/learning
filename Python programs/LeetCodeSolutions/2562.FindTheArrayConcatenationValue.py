"""
LeetCode 2562. Find the Array Concatenation Value

Given an array, return the concatenation value after operations.

Constraints:
- 1 <= nums.length <= 10^5
"""

def findTheArrayConcVal(nums):
    res = 0
    i, j = 0, len(nums)-1
    while i <= j:
        if i == j:
            res += nums[i]
        else:
            res += int(str(nums[i])+str(nums[j]))
        i += 1
        j -= 1
    return res
# Example usage:
# print(findTheArrayConcVal([7,52,2,4]))  # Output: 596
