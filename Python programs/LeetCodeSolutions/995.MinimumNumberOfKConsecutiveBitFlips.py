"""
995. Minimum Number of K Consecutive Bit Flips
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

Given a binary array nums and an integer k, return the minimum number of flips required to make all elements 1. If it is not possible, return -1. A flip consists of choosing a subarray of length k and flipping all bits in it.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= k <= nums.length

Example:
Input: nums = [0,1,0], k = 1
Output: 2
"""
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        flip = 0
        is_flipped = [0] * n
        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]
            if nums[i] == flip:
                if i + k > n:
                    return -1
                is_flipped[i] = 1
                flip ^= 1
                res += 1
        return res

# Example usage
if __name__ == "__main__":
    nums = [0,1,0]
    k = 1
    print(Solution().minKBitFlips(nums, k))  # Output: 2
