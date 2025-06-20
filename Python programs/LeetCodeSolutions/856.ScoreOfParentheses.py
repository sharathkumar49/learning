"""
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string based on the following rule:
- "()" has score 1
- AB has score A + B, where A and B are balanced parentheses strings
- (A) has score 2 * A

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2

Constraints:
- 2 <= s.length <= 50
- s consists of only '(' and ')'.
"""
def scoreOfParentheses(s):
    stack = [0]
    for c in s:
        if c == '(': stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    return stack[0]

# Example usage:
print(scoreOfParentheses("()"))    # Output: 1
print(scoreOfParentheses("(())"))  # Output: 2
print(scoreOfParentheses("()()"))  # Output: 2
