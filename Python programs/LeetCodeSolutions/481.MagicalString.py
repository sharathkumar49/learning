"""
481. Magical String

A magical string s consists of only '1' and '2' and obeys the following rules:
- The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string itself.
Given an integer n, return the number of '1's in the first n number in the magical string s.

Constraints:
- 1 <= n <= 10^5

Example:
Input: n = 6
Output: 3
"""

class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [3 - s[-1]] * s[i]
            i += 1
        return s[:n].count(1)

# Example usage:
sol = Solution()
print(sol.magicalString(6))  # Output: 3
