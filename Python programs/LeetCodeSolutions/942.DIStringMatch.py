"""
942. DI String Match
https://leetcode.com/problems/di-string-match/

Given a string s consisting of only 'I' (increase) and 'D' (decrease), return any permutation of [0, 1, ..., n] that satisfies the 'I' and 'D' pattern in s.

Constraints:
- 1 <= s.length <= 10000
- s[i] is either 'I' or 'D'.

Example:
Input: s = "IDID"
Output: [0,4,1,3,2]
"""
from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        res.append(lo)
        return res

# Example usage
if __name__ == "__main__":
    s = "IDID"
    print(Solution().diStringMatch(s))  # Output: [0,4,1,3,2]
