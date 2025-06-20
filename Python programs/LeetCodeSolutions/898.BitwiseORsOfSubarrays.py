"""
898. Bitwise ORs of Subarrays
https://leetcode.com/problems/bitwise-ors-of-subarrays/

Given an integer array arr, return the number of different results that can be obtained by taking the bitwise OR of every possible subarray of arr.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^9

Example:
Input: arr = [0]
Output: 1
"""
from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for x in arr:
            cur = {x | y for y in cur} | {x}
            res |= cur
        return len(res)

# Example usage
if __name__ == "__main__":
    arr = [0]
    print(Solution().subarrayBitwiseORs(arr))  # Output: 1
