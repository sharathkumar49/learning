"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Constraints:
- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

Example:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
"""
from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]

# Example usage
if __name__ == "__main__":
    nums = [3,1,2,4]
    print(Solution().sortArrayByParity(nums))  # Output: [2,4,3,1]
