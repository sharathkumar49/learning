"""
439. Ternary Expression Parser

Given a string representing a nested ternary expression, evaluate it.

Constraints:
- 1 <= expression.length <= 10000
- expression consists of digits, '?', ':', 'T', 'F'
- It is guaranteed that the given expression is valid and only contains digits 0-9, 'T', 'F', '?', ':'

Example:
Input: expression = "T?2:3"
Output: "2"
"""

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        i = len(expression) - 1
        while i >= 0:
            if expression[i] == '?':
                true_val = stack.pop()
                false_val = stack.pop()
                i -= 1
                stack.append(true_val if expression[i] == 'T' else false_val)
            elif expression[i] != ':':
                stack.append(expression[i])
            i -= 1
        return stack[-1]

# Example usage:
sol = Solution()
print(sol.parseTernary("T?2:3"))  # Output: "2"
