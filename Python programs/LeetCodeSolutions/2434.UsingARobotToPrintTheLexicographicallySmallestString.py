"""
LeetCode 2434. Using a Robot to Print the Lexicographically Smallest String

Given a string, use a robot to print the lexicographically smallest string.

Constraints:
- 1 <= s.length <= 10^5
"""

def robotWithString(s):
    from collections import Counter
    cnt = Counter(s)
    stack = []
    res = []
    min_char = min(cnt)
    for c in s:
        stack.append(c)
        cnt[c] -= 1
        while stack and min(cnt.elements()) >= stack[-1]:
            res.append(stack.pop())
    while stack:
        res.append(stack.pop())
    return ''.join(res)

# Example usage:
# print(robotWithString("zza"))  # Output: "azz"
