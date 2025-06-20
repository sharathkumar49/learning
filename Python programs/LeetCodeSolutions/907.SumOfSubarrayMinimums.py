"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 3 * 10^4
- 1 <= arr[i] <= 3 * 10^4

Example:
Input: arr = [3,1,2,4]
Output: 17
"""
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = 0
        dot = 0
        for i, x in enumerate(arr):
            count = 1
            while stack and stack[-1][0] >= x:
                y, c = stack.pop()
                count += c
                dot -= y * c
            stack.append((x, count))
            dot += x * count
            res = (res + dot) % MOD
        return res

# Example usage
if __name__ == "__main__":
    arr = [3,1,2,4]
    print(Solution().sumSubarrayMins(arr))  # Output: 17
