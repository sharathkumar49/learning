"""
LeetCode 1389. Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to create target array under the following rules:
- Initially target array is empty.
- From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
- Repeat the previous step until there are no elements to read in nums and index.

Return the target array.

Constraints:
- 1 <= nums.length, index.length <= 100
- nums.length == index.length
- 0 <= nums[i] <= 100
- 0 <= index[i] <= i

Example:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
"""
def createTargetArray(nums, index):
    target = []
    for n, i in zip(nums, index):
        target.insert(i, n)
    return target

# Example usage:
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums, index))  # Output: [0,4,1,3,2]
