"""
LeetCode 2375. Construct Smallest Number From DI String

Given a string s of 'D' and 'I', construct the smallest number following the pattern.

Constraints:
- 1 <= s.length <= 10^5
"""

def smallestNumber(s):
    n = len(s)
    res = []
    stack = []
    for i in range(n+1):
        stack.append(str(i+1))
        if i == n or s[i] == 'I':
            while stack:
                res.append(stack.pop())
    return ''.join(res)

# Example usage:
# print(smallestNumber("IIIDIDDD"))  # Output: "123549876"
