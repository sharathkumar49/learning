"""
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/

Given an integer array nums and an integer k, return the number of good subarrays of nums. A good subarray is a subarray with exactly k different integers.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i], k <= nums.length

Example:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
"""
from typing import List
from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k):
            count = Counter()
            res = i = 0
            for j, x in enumerate(nums):
                if count[x] == 0:
                    k -= 1
                count[x] += 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1
            return res
        return atMostK(k) - atMostK(k-1)

# Example usage
if __name__ == "__main__":
    nums = [1,2,1,2,3]
    k = 2
    print(Solution().subarraysWithKDistinct(nums, k))  # Output: 7
