"""
944. Delete Columns to Make Sorted
https://leetcode.com/problems/delete-columns-to-make-sorted/

You are given an array of n strings strs, all of the same length. Return the minimum number of columns that you should delete so that each remaining column is in non-decreasing sorted order.

Constraints:
- n == strs.length
- 1 <= n <= 100
- 1 <= strs[i].length <= 1000
- strs[i] consists of lowercase English letters.

Example:
Input: strs = ["cba","daf","ghi"]
Output: 1
"""
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(strs[i][j] > strs[i+1][j] for i in range(len(strs)-1)) for j in range(len(strs[0])))

# Example usage
if __name__ == "__main__":
    strs = ["cba","daf","ghi"]
    print(Solution().minDeletionSize(strs))  # Output: 1
