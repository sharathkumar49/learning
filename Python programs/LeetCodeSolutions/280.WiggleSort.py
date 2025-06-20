"""
280. Wiggle Sort
https://leetcode.com/problems/wiggle-sort/

Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4

Example 1:
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]

Example 2:
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]
"""
def wiggleSort(nums):
    for i in range(1, len(nums)):
        if (i % 2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1]):
            nums[i], nums[i-1] = nums[i-1], nums[i]

# Example usage:
if __name__ == "__main__":
    arr = [3,5,2,1,6,4]
    wiggleSort(arr)
    print(arr)  # Output: [3,5,1,6,2,4]
    arr2 = [6,6,5,6,3,8]
    wiggleSort(arr2)
    print(arr2) # Output: [6,6,5,6,3,8]
