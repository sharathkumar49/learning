"""
891. Sum of Subsequence Widths
https://leetcode.com/problems/sum-of-subsequence-widths/

The width of a sequence is the difference between the maximum and minimum elements in the sequence.
Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= nums.length <= 20000
- 1 <= nums[i] <= 20000

Example:
Input: nums = [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].
Widths are 0, 0, 0, 1, 2, 1, 2.
Sum is 6.
"""
from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i-1] * 2 % MOD
        res = 0
        for i in range(n):
            res = (res + nums[i] * (pow2[i] - pow2[n-1-i])) % MOD
        return res

# Example usage
if __name__ == "__main__":
    nums = [2,1,3]
    print(Solution().sumSubseqWidths(nums))  # Output: 6
