# 20. Valid Parentheses (Recursive)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

def isValid(s):
    def helper(s, stack):
        if not s:
            return not stack
        char = s[0]
        if char in '([{':
            return helper(s[1:], stack + [char])
        if not stack:
            return False
        if char == ')' and stack[-1] != '(': return False
        if char == ']' and stack[-1] != '[': return False
        if char == '}' and stack[-1] != '{': return False
        return helper(s[1:], stack[:-1])
    return helper(s, [])

# Example usage
s = "([{}])"
print("Is valid (recursive):", isValid(s))  # Output: True
