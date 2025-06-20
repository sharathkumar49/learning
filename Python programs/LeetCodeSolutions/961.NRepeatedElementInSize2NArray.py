"""
961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

You are given an integer array nums with length 2n. The array contains n+1 unique elements, and exactly one of these elements is repeated n times.
Return the element that is repeated n times.

Constraints:
- 2 <= n <= 5000
- nums.length == 2 * n
- 0 <= nums[i] <= 10^4
- Exactly one element is repeated n times.

Example:
Input: nums = [1,2,3,3]
Output: 3
"""
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return -1

# Example usage
if __name__ == "__main__":
    nums = [1,2,3,3]
    print(Solution().repeatedNTimes(nums))  # Output: 3
