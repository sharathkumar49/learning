"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#'.
"""
def backspaceCompare(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return ''.join(stack)
    return build(s) == build(t)

# Example usage:
print(backspaceCompare("ab#c", "ad#c"))  # Output: True
print(backspaceCompare("ab##", "c#d#"))  # Output: True
