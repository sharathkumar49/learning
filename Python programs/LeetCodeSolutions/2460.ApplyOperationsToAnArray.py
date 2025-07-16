"""
LeetCode 2460. Apply Operations to an Array

Given an array, apply operations and return the result.

Constraints:
- 1 <= nums.length <= 1000
"""

def applyOperations(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    res = [x for x in nums if x != 0]
    res += [0]*(len(nums)-len(res))
    return res

# Example usage:
# print(applyOperations([1,2,2,1,1,0]))  # Output: [1,4,2,0,0,0]
