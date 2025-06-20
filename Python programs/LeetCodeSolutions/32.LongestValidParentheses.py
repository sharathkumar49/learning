# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
# Input: s = "(()"
# Output: 2
#
# Example 2:
# Input: s = ")()())"
# Output: 4
#
# Example 3:
# Input: s = ""
# Output: 0
#
# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.

def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == '(': stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# Example usage
s = ")()())"
print("Longest valid parentheses:", longestValidParentheses(s))  # Output: 4
