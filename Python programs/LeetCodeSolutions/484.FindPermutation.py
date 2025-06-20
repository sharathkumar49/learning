"""
484. Find Permutation

Given a string s consisting of only 'D' and 'I', return any permutation of the first n positive integers that satisfy the given input string.

Constraints:
- 1 <= s.length < 10^5
- s consists only of characters 'I' or 'D'.

Example:
Input: s = "IDID"
Output: [1,2,3,4,5]
"""

class Solution:
    def findPermutation(self, s: str) -> list:
        n = len(s) + 1
        res = list(range(1, n+1))
        i = 0
        while i < len(s):
            if s[i] == 'D':
                j = i
                while j < len(s) and s[j] == 'D':
                    j += 1
                res[i:j+1] = reversed(res[i:j+1])
                i = j
            else:
                i += 1
        return res

# Example usage:
sol = Solution()
print(sol.findPermutation("IDID"))  # Output: [1, 2, 3, 4, 5]
