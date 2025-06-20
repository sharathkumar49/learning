"""
978. Longest Turbulent Subarray
https://leetcode.com/problems/longest-turbulent-subarray/

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
A subarray is turbulent if the comparison sign flips between each adjacent pair.

Constraints:
- 1 <= arr.length <= 4 * 10^4
- 0 <= arr[i] <= 10^9

Example:
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
"""
from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        inc = dec = res = 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            res = max(res, inc, dec)
        return res

# Example usage
if __name__ == "__main__":
    arr = [9,4,2,10,7,8,8,1,9]
    print(Solution().maxTurbulenceSize(arr))  # Output: 5
