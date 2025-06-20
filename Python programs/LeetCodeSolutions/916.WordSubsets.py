"""
916. Word Subsets
https://leetcode.com/problems/word-subsets/

You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
Return a list of all words in words1 that are universal (i.e., every word in words2 is a subset of it).

Constraints:
- 1 <= words1.length, words2.length <= 10^4
- 1 <= words1[i].length, words2[i].length <= 10
- words1[i] and words2[i] consist only of lowercase English letters.

Example:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
"""
from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        bmax = Counter()
        for b in words2:
            bmax |= Counter(b)
        res = []
        for a in words1:
            if not bmax - Counter(a):
                res.append(a)
        return res

# Example usage
if __name__ == "__main__":
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    print(Solution().wordSubsets(words1, words2))  # Output: ["facebook","google","leetcode"]
