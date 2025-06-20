"""
972. Equal Rational Numbers
https://leetcode.com/problems/equal-rational-numbers/

Given two strings s and t representing rational numbers, return true if they represent the same number.
A rational number can be in the form "0.5", "2", "0.(52)", "0.5(25)", etc. (where the part in parentheses is a repeating part).

Constraints:
- s and t are strings with 1 <= s.length, t.length <= 20
- s and t are valid rational numbers.

Example:
Input: s = "0.(52)", t = "0.5(25)"
Output: true
"""
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def f(x):
            if '(' not in x:
                return float(x)
            i = x.index('(')
            non_rep = x[:i]
            rep = x[i+1:-1]
            base = float(non_rep)
            mul = 10 ** (len(non_rep.split('.')[-1]) if '.' in non_rep else 0)
            rep_val = int(rep)
            rep_len = len(rep)
            return base + rep_val / (mul * (10**rep_len - 1) / (10**rep_len))
        return abs(f(s) - f(t)) < 1e-9

# Example usage
if __name__ == "__main__":
    s = "0.(52)"
    t = "0.5(25)"
    print(Solution().isRationalEqual(s, t))  # Output: True
