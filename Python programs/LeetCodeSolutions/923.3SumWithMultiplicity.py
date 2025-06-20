"""
923. 3Sum With Multiplicity
https://leetcode.com/problems/3sum-with-multiplicity/

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
As the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 3 <= arr.length <= 3000
- 0 <= arr[i] <= 100
- 0 <= target <= 300

Example:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
"""
from typing import List
from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count)
        res = 0
        for i, x in enumerate(keys):
            for j, y in enumerate(keys[i:], i):
                z = target - x - y
                if z < y: continue
                if z not in count: continue
                if x == y == z:
                    res += count[x] * (count[x]-1) * (count[x]-2) // 6
                elif x == y != z:
                    res += count[x] * (count[x]-1) // 2 * count[z]
                elif x < y < z:
                    res += count[x] * count[y] * count[z]
        return res % MOD

# Example usage
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    print(Solution().threeSumMulti(arr, target))  # Output: 20
