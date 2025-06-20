"""
936. Stamping The Sequence
https://leetcode.com/problems/stamping-the-sequence/

You are given two strings stamp and target. Return an array of the index positions where stamp can be placed to form the target by repeatedly stamping. If it is not possible, return an empty array. The answer can be returned in any order.

Constraints:
- 1 <= stamp.length <= target.length <= 1000
- stamp and target consist of lowercase English letters.

Example:
Input: stamp = "abc", target = "ababc"
Output: [0,2]
"""
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        S, T = list(stamp), list(target)
        m, n = len(S), len(T)
        res = []
        changed = True
        visited = [False] * (n - m + 1)
        stars = 0
        while stars < n:
            changed = False
            for i in range(n - m + 1):
                if not visited[i] and self.can_stamp(T, i, S):
                    stars += self.do_stamp(T, i, m)
                    visited[i] = True
                    changed = True
                    res.append(i)
            if not changed:
                return []
        return res[::-1]

    def can_stamp(self, T, i, S):
        for j in range(len(S)):
            if T[i+j] != '*' and T[i+j] != S[j]:
                return False
        return any(T[i+j] != '*' for j in range(len(S)))

    def do_stamp(self, T, i, m):
        count = 0
        for j in range(m):
            if T[i+j] != '*':
                T[i+j] = '*'
                count += 1
        return count

# Example usage
if __name__ == "__main__":
    stamp = "abc"
    target = "ababc"
    print(Solution().movesToStamp(stamp, target))  # Output: [0,2]
