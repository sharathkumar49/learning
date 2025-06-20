"""
960. Delete Columns to Make Sorted III
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

You are given an array of n strings strs, all of the same length. Return the minimum number of columns that you should delete to make the rows of the resulting array lexicographically increasing.

Constraints:
- 1 <= strs.length <= 100
- 1 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Example:
Input: strs = ["babca","bbazb"]
Output: 3
"""
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        dp = [1] * m
        for j in range(m):
            for i in range(j):
                if all(strs[k][i] <= strs[k][j] for k in range(n)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return m - max(dp)

# Example usage
if __name__ == "__main__":
    strs = ["babca","bbazb"]
    print(Solution().minDeletionSize(strs))  # Output: 3
