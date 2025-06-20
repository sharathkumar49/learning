"""
974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4

Example:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
"""
from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res = s = 0
        for x in nums:
            s = (s + x) % k
            res += count[s]
            count[s] += 1
        return res

# Example usage
if __name__ == "__main__":
    nums = [4,5,0,-2,-3,1]
    k = 5
    print(Solution().subarraysDivByK(nums, k))  # Output: 7
