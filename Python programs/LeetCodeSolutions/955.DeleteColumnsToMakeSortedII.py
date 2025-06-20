"""
955. Delete Columns to Make Sorted II
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

You are given an array of n strings strs, all of the same length. Return the minimum number of columns that you should delete to ensure that each row is lexicographically less than or equal to the next row.

Constraints:
- 1 <= strs.length <= 100
- 1 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Example:
Input: strs = ["ca","bb","ac"]
Output: 1
"""
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        res = 0
        sorted_rows = [False] * (n-1)
        for j in range(m):
            for i in range(n-1):
                if not sorted_rows[i] and strs[i][j] > strs[i+1][j]:
                    res += 1
                    break
            else:
                for i in range(n-1):
                    if strs[i][j] < strs[i+1][j]:
                        sorted_rows[i] = True
        return res

# Example usage
if __name__ == "__main__":
    strs = ["ca","bb","ac"]
    print(Solution().minDeletionSize(strs))  # Output: 1
