# Microsoft: Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack

if __name__ == "__main__":
    s1 = "()"
    print(is_valid(s1))  # Output: True
    s2 = "()[]{}"
    print(is_valid(s2))  # Output: True
    s3 = "(]"
    print(is_valid(s3))  # Output: False
    s4 = "([)]"
    print(is_valid(s4))  # Output: False
    s5 = "{[]}"
    print(is_valid(s5))  # Output: True
