# Google: Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False
    return not stack

if __name__ == "__main__":
    print(is_valid("()"))      # Output: True
    print(is_valid("()[]{}"))  # Output: True
    print(is_valid("(]"))      # Output: False
