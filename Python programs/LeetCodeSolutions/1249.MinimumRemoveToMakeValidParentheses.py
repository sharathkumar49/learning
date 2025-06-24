"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters, return the minimum string after removing the minimum number of invalid parentheses.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '(', ')' or a lowercase English letter.

Example:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"

"""
def minRemoveToMakeValid(s):
    s = list(s)
    stack = []
    for i, c in enumerate(s):
        if c == '(': stack.append(i)
        elif c == ')':
            if stack: stack.pop()
            else: s[i] = ''
    for i in stack:
        s[i] = ''
    return ''.join(s)

# Example usage
if __name__ == "__main__":
    print(minRemoveToMakeValid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
