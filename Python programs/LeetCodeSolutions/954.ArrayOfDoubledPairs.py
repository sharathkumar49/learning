"""
954. Array of Doubled Pairs
https://leetcode.com/problems/array-of-doubled-pairs/

Given an integer array arr of even length, return true if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Constraints:
- 2 <= arr.length <= 3 * 10^4
- arr.length is even
- -10^5 <= arr[i] <= 10^5

Example:
Input: arr = [3,1,3,6]
Output: false
"""
from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2*x] < count[x]:
                return False
            count[2*x] -= count[x]
        return True

# Example usage
if __name__ == "__main__":
    arr = [3,1,3,6]
    print(Solution().canReorderDoubled(arr))  # Output: False
