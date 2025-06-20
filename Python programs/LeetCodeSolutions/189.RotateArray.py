"""
189. Rotate Array
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""
def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    rotate(arr, 3)
    print(arr)  # Output: [5,6,7,1,2,3,4]
    arr2 = [-1,-100,3,99]
    rotate(arr2, 2)
    print(arr2) # Output: [3,99,-1,-100]
