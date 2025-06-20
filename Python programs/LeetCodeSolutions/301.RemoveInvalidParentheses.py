"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid. Return all possible results. You may return the answer in any order.

Constraints:
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '('
  and ')'.
- At most 20 parentheses will be removed.
"""
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        def isValid(st):
            count = 0
            for c in st:
                if c == '(': count += 1
                if c == ')': count -= 1
                if count < 0: return False
            return count == 0
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i+1:])
            level = next_level

# Example usage:
s = "()())()"
print(Solution().removeInvalidParentheses(s))  # Output: ["(())()", "()()()"]
