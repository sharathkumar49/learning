"""
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Given a string s of '(' and ')', return the minimum number of parentheses that must be added to make the resulting string valid.

Constraints:
- 1 <= s.length <= 1000
- s consists of '(' and ')'

Example:
Input: s = "())"
Output: 1
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = bal = 0
        for c in s:
            if c == '(': bal += 1
            else:
                if bal == 0:
                    res += 1
                else:
                    bal -= 1
        return res + bal

# Example usage
if __name__ == "__main__":
    s = "())"
    print(Solution().minAddToMakeValid(s))  # Output: 1
