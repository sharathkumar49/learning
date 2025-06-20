"""
922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/

Given an array of integers nums of even length n, half of the integers in nums are odd, and half of the integers are even.
Sort the array so that whenever nums[i] is even, i is even, and whenever nums[i] is odd, i is odd.
Return any answer array that satisfies this condition.

Constraints:
- 2 <= nums.length <= 2 * 10^4
- nums.length is even
- 0 <= nums[i] <= 1000

Example:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
"""
from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        even, odd = 0, 1
        for x in nums:
            if x % 2 == 0:
                res[even] = x
                even += 2
            else:
                res[odd] = x
                odd += 2
        return res

# Example usage
if __name__ == "__main__":
    nums = [4,2,5,7]
    print(Solution().sortArrayByParityII(nums))  # Output: [4,5,2,7]
