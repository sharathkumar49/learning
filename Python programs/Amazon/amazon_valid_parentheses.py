# Amazon: Valid Parentheses
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in mapping.values():
            stack.append(c)
        elif c in mapping:
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    s = input("Enter string: ")
    print("Valid:", is_valid(s))
