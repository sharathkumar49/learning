"""
522. Longest Uncommon Subsequence II

Given a list of strings strs, return the length of the longest uncommon subsequence among them. If no such subsequence exists, return -1.

Constraints:
- 1 <= strs.length <= 50
- 1 <= strs[i].length <= 10
- strs[i] consists of lowercase English letters.

Example:
Input: strs = ["aba","cdc","eae"]
Output: 3
"""

def is_subsequence(a, b):
    it = iter(b)
    return all(c in it for c in a)

class Solution:
    def findLUSlength(self, strs: list) -> int:
        strs.sort(key=len, reverse=True)
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)
        return -1

# Example usage:
sol = Solution()
print(sol.findLUSlength(["aba","cdc","eae"]))  # Output: 3
