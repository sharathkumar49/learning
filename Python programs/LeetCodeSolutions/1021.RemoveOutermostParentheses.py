"""
1021. Remove Outermost Parentheses

A valid parentheses string is a non-empty string consisting only of '(' and ')'.
Given a valid parentheses string S, remove the outermost parentheses of every primitive string in the primitive decomposition of S.

Constraints:
- 1 <= S.length <= 10^5
- S[i] is '(' or ')'

Example:
Input: S = "(()())(())"
Output: "()()()"
Explanation: The outermost parentheses of each primitive string are removed.
"""
def removeOuterParentheses(S: str) -> str:
    res = []
    opened = 0
    for c in S:
        if c == '(': 
            if opened > 0:
                res.append(c)
            opened += 1
        else:
            opened -= 1
            if opened > 0:
                res.append(c)
    return ''.join(res)

# Example usage:
S = "(()())(())"
print(removeOuterParentheses(S))  # Output: "()()()"
