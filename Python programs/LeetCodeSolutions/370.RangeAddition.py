"""
370. Range Addition

You are given an integer length and an array updates where updates[i] = [startIndex, endIndex, inc].
Return the modified array after all updates have been applied.

Constraints:
- 1 <= length <= 10^5
- 0 <= updates.length <= 10^4
- 0 <= startIndex <= endIndex < length
- -1000 <= inc <= 1000
"""
from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc
        for i in range(1, length):
            res[i] += res[i - 1]
        return res

# Example usage:
length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print(Solution().getModifiedArray(length, updates))  # Output: [-2,0,3,5,3]
