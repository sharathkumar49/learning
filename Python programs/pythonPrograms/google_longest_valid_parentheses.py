# Google: Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

def longest_valid_parentheses(s):
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

if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))      # Output: 2
    print(longest_valid_parentheses(")()())"))   # Output: 4
