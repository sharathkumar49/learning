"""
893. Groups of Special-Equivalent Strings
https://leetcode.com/problems/groups-of-special-equivalent-strings/

You are given an array of strings words. Two strings A and B are special-equivalent if after any number of moves, A == B.
A move consists of choosing two indices i and j with i % 2 == j % 2 and swapping A[i] with A[j].
Return the number of groups of special-equivalent strings from words.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 20
- words[i] consists of lowercase English letters.

Example:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
"""
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        seen = set()
        for word in words:
            even = tuple(sorted(word[::2]))
            odd = tuple(sorted(word[1::2]))
            seen.add((even, odd))
        return len(seen)

# Example usage
if __name__ == "__main__":
    words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
    print(Solution().numSpecialEquivGroups(words))  # Output: 3
