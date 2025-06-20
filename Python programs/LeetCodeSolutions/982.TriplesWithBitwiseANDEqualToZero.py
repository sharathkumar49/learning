"""
982. Triples with Bitwise AND Equal To Zero
https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

Given an integer array nums, return the number of AND triples (i, j, k) such that:
- 0 <= i, j, k < nums.length
- nums[i] & nums[j] & nums[k] == 0

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < 2^16

Example:
Input: nums = [2,1,3]
Output: 12
"""
from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = Counter()
        for a in nums:
            for b in nums:
                count[a & b] += 1
        res = 0
        for c in nums:
            for ab, cnt in count.items():
                if ab & c == 0:
                    res += cnt
        return res

# Example usage
if __name__ == "__main__":
    nums = [2,1,3]
    print(Solution().countTriplets(nums))  # Output: 12
