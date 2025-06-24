"""
1190. Reverse Substrings Between Each Pair of Parentheses

Given a string s, reverse the substrings between each pair of parentheses, starting from the innermost. Return the resulting string with no parentheses.

Constraints:
- 1 <= s.length <= 2000
- s consists of lowercase English letters and parentheses.

Example:
Input: s = "(u(love)i)"
Output: "iloveu"

"""
def reverseParentheses(s):
    stack = ['']
    for c in s:
        if c == '(': stack.append('')
        elif c == ')':
            last = stack.pop()[::-1]
            stack[-1] += last
        else:
            stack[-1] += c
    return stack[0]

# Example usage
if __name__ == "__main__":
    print(reverseParentheses("(u(love)i)"))  # Output: "iloveu"
