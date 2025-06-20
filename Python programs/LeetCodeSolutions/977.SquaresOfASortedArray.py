"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)

# Example usage
if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(Solution().sortedSquares(nums))  # Output: [0,1,9,16,100]
