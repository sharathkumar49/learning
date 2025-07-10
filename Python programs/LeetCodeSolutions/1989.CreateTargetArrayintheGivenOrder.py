"""
LeetCode 1989. Create Target Array in the Given Order

Given two arrays nums and index, return the target array after inserting nums[i] at index[i].

Example:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]

Constraints:
- 1 <= nums.length, index.length <= 100
- 0 <= nums[i], index[i] <= nums.length
"""

def createTargetArray(nums, index):
    res = []
    for n, i in zip(nums, index):
        res.insert(i, n)
    return res

# Example usage:
# print(createTargetArray([0,1,2,3,4], [0,1,2,2,1]))  # Output: [0,4,1,3,2]
