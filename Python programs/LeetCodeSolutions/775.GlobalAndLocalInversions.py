"""
775. Global and Local Inversions

You are given an integer array nums of length n. We say that a global inversion is a pair (i, j) where 0 <= i < j < n and nums[i] > nums[j]. A local inversion is a pair (i, i+1) where 0 <= i < n-1 and nums[i] > nums[i+1].
Return true if the number of global inversions is equal to the number of local inversions.

Example 1:
Input: nums = [1,0,2]
Output: true

Example 2:
Input: nums = [1,2,0]
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] < nums.length
- All the elements of nums are unique.
"""
def isIdealPermutation(nums):
    for i, num in enumerate(nums):
        if abs(num - i) > 1:
            return False
    return True

# Example usage:
print(isIdealPermutation([1,0,2]))  # Output: True
print(isIdealPermutation([1,2,0]))  # Output: False
