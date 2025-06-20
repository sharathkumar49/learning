"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(n log(n)) time complexity and with the smallest space complexity possible.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
"""
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        return merge_sort(nums)

# Example usage
if __name__ == "__main__":
    nums = [5,2,3,1]
    print(Solution().sortArray(nums))  # Output: [1,2,3,5]
